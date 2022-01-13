from bin import globals

def run(value):
    print ("""

Usage:   nj_perf [ optional args ]

Purpose: Report and plot various statistics about the database/cluster as well as its current state

Inputs:
        [ -i | --interval              ]  <S|Min|H|D|W|Y>
        [ -p | --periods               ]  <nn>
        [ -s | --startdate             ]  <yyyy-mm-dd HH:MM:SS>
        [ -e | --enddate               ]  <yyyy-mm-dd HH:MM:SS>
        [ -c | --checkdb               ]
        [ -d | --display_precision     ]
        [ -b | --bolt_port             ]
        [ -v | --verbose               ]
        [ -r | --admin_report_dir      ]
        [ -m | --metric                ]  <"store"|"count"|"transaction"|"page_cache"|"bolt"|"causal_clustering"|
                                           "cypher"|"check_point"|"object"|"network"|"server"|
                                           "jvm_gc"|"jvm_memory"|"jvm_thread"|"log_rotation"|
                                           "all"|"none">

        o:  If no options are specified, metrics will be aggregated hourly over the last 24 hours of available data
        o:  Only specify startdate or enddate (not both) when also specifying interval and periods argumments
        o:  If interval and periods are both not specified, daily aggregation will be performed by default
        o:  If no metric category is specified, it will report on "ALL" metrics
        o:  To avoid running host/online-db  healthchecks, use "--checkdb=false"
        o:  To avoid running historical metric reporint, use "--metric none"
        o:  Additionally, --checkdb option will report on the following:

               Uptime
               Neo4j Kernel
               Database Restarts:
               Disk Utilization
               Neo4j Store Size
               Database/Index Size History
               Transaction Logs
               Host Processes
               vmstat
               netstats
               Neo4j Top 10 Slowest Queries
               Neo4j Top 10 Longest GC pauses
               Neo4j Node Density
               Neo4j Active Queries
               Neo4j Active Long Running Queries ( > 60s )
               Neo4j Transactions
               Neo4j Locks
               Non-default Neo4j.conf settings
               Recommended Configuration Settings
               Interesting Errors

         Examples:
               =========

               -i S -s '2019-03-29 04:42:45' -e '2019-03-29 04:43:15' -d
                    # Report aggregation on 30 seconds between 04:42:14 and 04:43:15 hours

               --startdate 2019-01-01 --enddate 2019-01-11  --metric transaction -b 7617 -c
                    # Report on ten individual days, starting on 2019-01-01

               --interval D   --periods 7  --startdate 2019-01-01  --metric all
                    # Report on seven individual days, starting on 2019-01-01

               --interval D   --periods 7  --enddate 2019-01-01 --metric cypher

                    # Report on seven individual days, starting on 2008-01-01

               --interval W  --periods 4  --startdate 2019-01-01
                    # Report on four one-week periods

               --interval W  --periods 4  --enddate 2019-01-01
                    # Report on four one-week periods

               --interval Y -periods 2  --startdate 2018-01-01

Outputs:   Sample output ....

$nj_perf -m transaction -s '2019-01-01' -e '2019-02-02' -i W

date                        2019-01-06  2019-01-13  2019-01-20  2019-01-27  2019-02-03
tx.peak_concurrent_Avg             239         239         239         239         239
tx.peak_concurrent_Max             239         239         239         239         239
tx.started-ps_Avg                  425         433         448         444         446
tx.started-ps_Max                 1651        1732        1802        1447        1376
tx.active_Avg                        8           6           7           7           8
tx.active_Max                      273         266         272         261         226
tx.active_read_Avg                   5           4           4           5           5
tx.active_read_Max                 231         233         216         220         203
tx.active_write_Avg                  3           3           3           3           4
tx.active_write_Max                239         236         245         237         226
tx.committed-ps_Avg                327         366         396         390         379
tx.committed-ps_Max               1650        1731        1800        1449        1374
tx.committed_read-ps_Avg           236         304         347         340         318
tx.committed_read-ps_Max          1650        1731        1800        1449        1374
tx.committed_write-ps_Avg           91          63          49          51          62
tx.committed_write-ps_Max          499         546         520         462         377
tx.rollbacks-ps_Avg                 99          68          53          55          67
tx.rollbacks-ps_Max                412         406         369         357         351
tx.rollbacks_read-ps_Avg            99          68          53          55          67
tx.rollbacks_read-ps_Max           412         406         369         357         351
tx.rollbacks_write-ps_Avg            1           1           1           1           1
tx.rollbacks_write-ps_Max            1           1           1          11           1
tx.terminated-ps_Avg                 1           1           1           1           1
tx.terminated-ps_Max               196         159         216         198         221
tx.terminated_read-ps_Avg            1           1           1           1           1
tx.terminated_read-ps_Max          196         159         216         198         221
tx.terminated_write-ps_Avg           0           1           1           1           1
tx.terminated_write-ps_Max



Dependencies:

        o Export NEO4J_HOME
        o Export DB_USER
        o Export DB_PWD
        o APOC
        o Python2 or Python3
        o Pandas
        o ConfigObj
        o Matplotlib

        Enabling cvs metrics:

        o Set the following in neo4j.conf and restart the instance.
        o When setting the query threshold value, please set this appropriately to what makes sense for your environment.
        A value of zero will capture and log all successfully completed queries in the query.log file.

        dbms.logs.query.parameter_logging_enabled=true
        dbms.logs.query.time_logging_enabled=true
        dbms.logs.query.allocation_logging_enabled=true
        dbms.logs.query.page_logging_enabled=true
        dbms.logs.query.enabled=true
        dbms.logs.query.threshold=0

        metrics.enabled=true
        metrics.neo4j.enabled=true
        metrics.neo4j.tx.enabled=true
        metrics.neo4j.pagecache.enabled=true
        metrics.neo4j.counts.enabled=true
        metrics.neo4j.network.enabled=true
        metrics.csv.enabled=true
        metrics.csv.interval=3s
        metrics.csv.rotation.size=10M
        dbms.track_query_allocation=true
        dbms.track_query_cpu_time=true


Python Installation Instructions(Ubuntu):

        o sudo apt install unzip
        o sudo apt-get install software-properties-common
        o sudo apt-add-repository universe
        o sudo apt-get update

        # Python2
        o sudo apt-get install python-pip
        o sudo pip install pandas
        o sudo pip install configobj
        o sudo pip install matplotlib

        # Python3
        o sudo apt-get install python3-pip
        o sudo pip3 install pandas
        o sudo pip3 install configobj
        o sudo pip3 install matplotlib

Instructions to run the script:

        1) Download the script
        2) chmod +x nj_perf
        3) ensure the python along with its dependencies as outline above are installed
        4) Run the script.   If [ -c | --checkdb ] option is optionally used, then ensure DB_USER, DB_PASSWD as well as NEO4J_HOME are also set.
           The script does expect to run an analysis of stats in the metrics directory.
           As such, cvs metrics also needs to have been enabled and contain some data for proper analysis.  By default, the script will
           look for the metrics directory in the current working directory, and if not found, it will then look under the
           directory specified by NEO4j_HOME.


""")

    if value == 'interval':
        print (' ')
        print ('Example:  --interval <H|D|W|Y> ')
        print (' ')
    if value == 'query':
        print (' ')
        print ('Example:  [-r | --admin_report_directory } <DirectoryPath> ')
        print (' ')
    if value == 'metric_category':
        print ("""

        Example:  --metric  ["transaction"|"page_cache"|"bolt"|"causal_clustering"|"cypher"|"check_point"|"object"|"network"|"server"|"jvm_gc"|"jvm_memory"|"jvm_thread"|"log_rotation"|"all"]

        """)

    if value == 'dates':
        print("""

         o:  Only specify startdate or enddate (not both) when also specifying interval and periods argumments
         o:  If interval and periods are both not specified, daily aggregation will be performed by default

               Examples:
               =========
               --startdate 2019-01-01 --enddate 2019-01-11
                    # Report on ten individual days, starting on 2019-01-01

               --interval D   --periods 7  --startdate 2019-01-01
                    # Report on seven individual days, starting on 2019-01-01

               --interval D   --periods 7  --enddate 2019-01-01
                    # Report on seven individual days, starting on 2008-01-01

               --interval W  --periods 4  --startdate 2019-01-01
                    # Report on four one-week periods

               --interval W  --periods 4  --enddate 2019-01-01
                    # Report on four one-week periods

               --interval Y -periods 2  --startdate 2018-01-01
                    # Report on two years, starting at the beginning of year



""")