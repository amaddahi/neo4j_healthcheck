from bin import globals
from bin import merge_rotated_files
from bin import inspect_file_start
from bin import get_metric_category_abbr
import re
import os

def run(filenames, metric_category):

    if globals.debug:
         print (">>>> Inside merge_csv_files.py")
         print ("------------------------------")
         #  neo4j.ingestion.test.ids_in_use.node.csv', 1, '-ps', 'neo4j.ids_in_use.node.csv

    check_point_duration_metric_filetmp=False
    all_metric_filetmp = metric_category + ".all_metrics_epoch"
    i = 1

    #
    #append historical rotated files into metric.csv.rotated file
    #

    merge_rotated_files.run(metric_category,filenames)

    #
    # Different metric files can have different start/end times.  This module will align their start/end times with naming convention metrics.csv.final
    #

    inspect_file_start.run(metric_category)

    # Rename the data index lables/titles to match its file name
    #
    # merge/paste all metric files for a specific category into a single file
    #
    #
    for file in filenames:
        filetmp_x = globals.working_directory + "/filetmp_x"
        filetmp_i = globals.working_directory + "/filetmp_i"
        metrics_file = globals.metrics_directory + "/" + file[0] + ".final"
        metrics_concat_file = globals.working_directory + "/" + file[0] + ".cat"

        if globals.debug:
            print(">>Inside merge_csv_files.. ")
            print("metrics_file: " + metrics_file)
            print("metrics_concat_file: " + metrics_concat_file)
            print(" ")
            exit
       
        # differentiate between database specific metrics and the rest where metric name is <neo4j.dbname.metric>

        dot_count=file[0].count(".")
        if metric_category in ('count','operation','transaction','object','cypher','log_rotation','check_point','jvm_thread'):
                file_type = file[0].split('.')[dot_count-2]    #  Assumes neo4j. + database + .category + .csv ( neo4j. + dbname + .ids_in_use.node + .csv)
        elif metric_category in ('store','jvm_gc'):
                file_type = file[0].split('.')[dot_count-3]    #  Assumes neo4j. + database + .category        ( neo4j.   dbname + .store.size.total.csv )
        else:
                file_type = file[0].split('.')[1]

        # neo4j.db.operation.count.create.csv
        # neo4j.neo4j.transaction.tx_size_native.csv

        if globals.debug:
            print(">>Inside merge_csv_files.. file_type==: " + file_type)

        if file_type == "thread":
            file_type = "jvm_thread"
        elif file_type == "memory":
            file_type = "jvm_memory"
        elif file_type == "gc":
            file_type = "jvm_memory"
        elif file_type == "ids_in_use":
            file_type = "object"
     
        #print (file_type)

        (metric_category_abbr, db_category_abbr) = get_metric_category_abbr.run(file_type)

        #
        # Rename column index names
        #

        #metric_category_abbr:ckp.
        #db_category_abbr:neo4j.
        #database:testdb1
        #file_type:check_point
        #string1:neo4j.testdb1.check_point.
        #file[0]:neo4j.testdb1.check_point.events.csv
        #column Name:neo4j.check_point.events

        if file_type in ( 'transaction','object','cypher','log','jvm_thread'):
             string1 = db_category_abbr + globals.database + '.' + file_type + "."
             if file_type in ('transaction','cypher','log_rotation','jvm_gc'):
                  val_label = re.sub(
                      '', '', (re.sub('.csv', '', (re.sub(string1, metric_category_abbr, file[0])))))
             else:  #log_rotation
                 val_label = re.sub(
                     '', '', (re.sub('.csv', '', (re.sub(string1, metric_category_abbr, file[3])))))
        elif file_type in ('jvm_memory','check_point'):
             string1 = db_category_abbr + file_type + "."
             val_label=re.sub('', '', (re.sub('.csv', '', (re.sub(string1, metric_category_abbr, file[3])))))
             if globals.debug:
                 print(" ")
                 print("file[0]:" + file[0])
                 print("file[3]:" + file[3])
                 print("db_category_abbr:" + db_category_abbr + " file_type: "  + file_type  )
                 print("string1:" + string1)
                 print("metric_category_abbr:" + metric_category_abbr)
                 print("column Name:" + val_label)
                 print(" ")

        elif file_type in ('count','store'):
             string1 = db_category_abbr + file_type + "."
             #print("----------------------------")
             #print(file[0])
             #print(db_category_abbr)
             #print(file_type)
             #print(string1)
             #print(  "re.sub(" + string1 + " , " + metric_category_abbr + " , " + file[0]+")")
             #print(re.sub(string1, metric_category_abbr, file[0]))
             #print((re.sub('.csv', '', (re.sub(string1, metric_category_abbr, file[0])))))
             #val_label = re.sub( '', '', (re.sub('.csv', '', (re.sub(string1, metric_category_abbr, file[0])))))
             val_label = re.sub('', '', (re.sub('.csv', '',file[0] )))
             #print(val_label)
             #print("----------------------------")
             #exit(0)
        else:
             string1 = db_category_abbr + file_type + "."
             val_label = re.sub(
                  '', '', (re.sub('.csv', '', (re.sub(string1, metric_category_abbr, file[0])))))

        #Filename--->file[0]:neo4j.test2.store.size.total.csv
        #file[3]:neo4j.store.size.total.csv
        #db_category_abbr:neo4j. || database: test2 || file_type: store
        #metric_category_abbr: store.
        #string1: neo4j.store.
        #column_Name: neo4j.test2.store.size.total

        #Filename--->file[0]:neo4j.neo4j.store.size.total.csv
        #file[3]:neo4j.store.size.total.csv
        #db_category_abbr:neo4j. || database: neo4j || file_type: store
        #metric_category_abbr: store.
        #string1: neo4j.store.
        #column_Name: neo4j.store.size.total


        # Add per second (-ps) to the column names if needed


        if globals.debug:
             print(" ")
             print("Filename--->file[0]:" + file[0])
             if metric_category not in ('operation','bolt','page_cache','server'):
                print("file[3]:" + file[3])
             print("db_category_abbr:" + db_category_abbr + " || database: " + globals.database + " || file_type: " + file_type  )
             #print("database:" + database)
             #print("file_type:" + file_type)
             print("metric_category_abbr: " + metric_category_abbr)
             print("string1: " + string1)
             print("column_Name: " + val_label)
             print(" ")

        # Add per second (-ps) to the column names if needed
        val_label = val_label + file[2]

        #Filename--->file[0]:neo4j.neo4j.transaction.peak_concurrent.csv
        #file[3]:neo4j.transaction.peak_concurrent.csv
        #db_category_abbr:neo4j. || database: neo4j || file_type: transaction
        #metric_category_abbr:tx.
        #string1:neo4j.neo4j.transaction.
        #column Name:tx.peak_concurrent

        #exit(0)

        #
        file_ascii=file[0] + ".ascii"

        # clean up any potential binary non-printable data (might show up as result of transfering files between different host systems)
        #
        cmd="sed $'s/[^[:print:]\t]//g'  " + metrics_file  + " > " + file_ascii
        os.system(cmd)
        #cmd="(head -1 " + metrics_file  + " | sed $'s/[^[:print:]\t]//g'  | sed 's/^t/date/g'  && cat `ls -1r " +  metrics_file + "* ` | grep -v '^t'  ) > filename1 && mv filename1 " + metrics_concat_file
        cmd="(head -1 " + file_ascii  + " | sed 's/^t/date/g'  && cat `ls -1r " +  file_ascii + "* ` | grep -v '^t'  ) > filename1 && mv filename1 " + metrics_concat_file
        os.system(cmd)

        # rename the label from value to custom label name
        #
        cmd = "cut -d, -f1,2 " + metrics_concat_file + " | sed 's/count/value/g' |  sed 's/value/" + val_label + "/g'  > " + metrics_file
        os.system(cmd)

        #
        # concat metric files column by column for each metric category
        #
        # 0 = Non-cumulative event counter
        # 1 = Cumulative event counter
        # 2 = Cumulative Time event counter(ms)
        # 3 = special case for handling check_point_duration_time as it is logged only when checkpoint occurs (i.e. every 15 minutes or every 100K transactions - depending on the configuration) and not every 3 seconds(default for csv_metric_interval)

        if file[1] != 3:
            if i == 1:
                os.system("cp " + metrics_file + " " + all_metric_filetmp)
            elif i > 1:
                cmd = "cut -d, -f2  " + metrics_file + "  | paste -d,  " + all_metric_filetmp + "   - > tmpfile ;  mv tmpfile " + all_metric_filetmp
                os.system(cmd)
            os.system("rm " + metrics_file)
            i += 1
        else:
            check_point_duration_metric_filetmp=metrics_file

        os.system("rm " + metrics_concat_file)
        os.system("rm " + file_ascii)

    return all_metric_filetmp, check_point_duration_metric_filetmp
#
