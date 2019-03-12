<pre>

Usage:   neo4j_health [ optional args ]

Purpose: Report and plot various statistics about the database/cluster as well as its current state

Inputs:
	[ -i | --interval    ]  <Min|H|D|W|Y>
	[ -p | --periods     ]  <nn>
	[ -s | --startdate   ]  <yyyy-mm-dd>
	[ -e | --enddate     ]  <yyyy-mm-dd>
	[ -l | --dbcheck     ]  <True|False>
	[ -m | --metric      ]  <"transaction"|"page_cache"|"bolt"|"causal_clustering"|
				"cypher"|"check_point"|"object"|"network"|"server"|
				"jvm_gc"|"jvm_memory"|"jvm_thread"|"log_rotation"|
				"all"|"none">

	o:  If no options are specified, metrics will be aggregated hourly over the last 24 hours of available data
	o:  Only specify startdate or enddate (not both) when also specifying interval and periods argumments
	o:  If interval and periods are both not specified, daily aggregation will be performed by default
	o:  If no metric category is specified, it will report on "ALL" metrics
	o:  To running host/online-db  healthchecks, use "--dbcheck=True"
	o:  To avoid running historical metric reporint, use "--metric none"

               Examples:
               =========
               --startdate 2019-01-01 --enddate 2019-01-11  --metric transaction
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

$neo4j_health -m transaction -s '2019-01-01' -e '2019-02-02' -i W


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
tx.terminated_write-ps_Max           0           1           1           1           1


Dependencies:
	o Export NEO4J_HOME
	o Export DB_USER
	o Export DB_PWD
	o APOC
	o Python2 or Python3
	o Pandas - sudo pip install pandas
	o ConfigObj - sudo pip install configobj
</pre>

