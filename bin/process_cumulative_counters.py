from bin import globals
from bin import get_metric_category_abbr
from bin import get_filenames
import re
import pandas as pd

def run(interval, df, metric_category):

    filenames = get_filenames.run(metric_category)

    if globals.debug:
         print("metric_category:  " + metric_category)

    (metric_category_abbr, db_category_abbr) = get_metric_category_abbr.run(metric_category)


    for file in filenames:
        if metric_category in ('transaction','object','cypher','log_rotation','jvm_gc'):
               file_token_name = file[3]
        else:
               file_token_name = file[0]

        if metric_category not in ('store'):
            x1 = re.sub(db_category_abbr + metric_category + '.', metric_category_abbr, file_token_name)
        else:
            x1 = file[0]

        if globals.debug:
            print ( "x1 = re.sub( " + db_category_abbr + metric_category + '. ,' + metric_category_abbr + ',' + file_token_name )
            print(db_category_abbr)
            print(metric_category)
            print(metric_category_abbr)
            print(file_token_name)
            print("x1:" + x1)

        val_label = re.sub('.csv', '', x1)
        if globals.debug:
            print("val_label-after ->  re.sub('.csv', '', x1):"  + val_label)
        val_label = val_label + file[2]
        if globals.debug:
            print("val_label after addin file[2]:"  + val_label)

        if globals.debug:
             print(" ")
             print("metric_category_abbr:" + metric_category_abbr)
             print("db_category_abbr:" + db_category_abbr)
             #print("database:" + database)
             #print("file_type:" + file_type)
             print("x1:" + x1)
             print("val_label:"  + val_label)
             print(" ")
             print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        # this is to address the warning when using df[val_label][df[val_label] < 0] = 0
        pd.set_option('mode.chained_assignment', None)

        if globals.debug:
            print (">>>> Inside cumulative counter:")
            print ("-------------------------------")
            print (print(list(df)))

        #add a counter for total
        if file[1] == 1:  # obtain rate of change per second between two points in time

            #if( metric_category == 'bolt' ):
                   #df[val_label] = df[val_label].diff().fillna(0)
            #else:

                   #df[val_label] = (df[val_label].diff()).fillna(0)
                   df[val_label] = (df[val_label].diff()/globals.metrics_csv_interval).fillna(0)
                   #df[val_label] = np.ceil(df[val_label].diff()/globals.metrics_csv_interval).fillna(0).astype(int)
                   #df[val_label] = np.ceil(df[val_label].diff()).fillna(0).astype(int)

                   df[val_label][df[val_label] < 0] = 0

        elif ((file[1] == 0) and ( metric_category == 'jvm_memory' )):
            df["heap_size-mb"]= df['vm.memory.pool.code_cache-mb'] +            \
                             df['vm.memory.pool.compressed_class_space-mb'] +   \
                             df['vm.memory.pool.g1_eden_space-mb'] +            \
                             df['vm.memory.pool.g1_old_gen-mb'] +                       \
                             df['vm.memory.pool.metaspace-mb']/(1024*1024)

            df[val_label]=df[val_label]/(1024*1024)
            df[val_label][df[val_label] < 0] = 0

        elif ((file[1] == 0) and ( metric_category == 'store' )):
            #print(df.head(10))
            #print(val_label)
            df[val_label]=df[val_label]/(1024*1024)

    return df
