from bin import globals

def host_db_check():

    global dbms_mode
    global bin_directory
    global logs_directory
    global conf_directory


    run_shell(
        "echo Uptime: `uptime | awk ' BEGIN { FS = \"up \" } { print $2}' | awk ' BEGIN { FS = \",\" } { print $1 $2 }'` ","",1)

    db('call apoc.monitor.kernel();',"Neo4j Kernel")

    #if neo4j_home is not None:
    if logs_directory is not None:
        run_shell("grep 'Operating System' " + logs_directory + "/debug.log | head -1","Host Operating System + Number of cpu cores",1)

    check_size()

    run_shell("top -n 5 -l 1 ","Processes",1)

    run_shell("exec 2> /dev/null ; vmstat -S k 1 10  ","vmstat",1)

    run_shell(
        "exec 2> /dev/null ; netstat -an | head -5 ; if [ $? != 0 ] ; then netstat -an | head -5; fi ","netstats",1)

    #run_shell("exec 2> /dev/null ; ps -ae --forest","Process Tree",1)

    if logs_directory is not None:
        run_shell("cd " + logs_directory + " ; cat debug.log.7 debug.log.6 debug.log.5 debug.log.4 debug.log.3 debug.log.2 debug.log.1 debug.log | grep -i 'o.n.b.i.BackupImpl' " ,"Neo4j Backups",0)

        run_shell(" grep -i 'INFO' " + logs_directory + "/query.log | sort -k4nr,4  | cut -c1-280 | head -10  ","Neo4j Top 10 Slowest Queries",1)

        run_shell(" grep -i 'Detected VM stop-the-world pause' " +
              logs_directory + "/debug.log | sort -k10 -r | head -10 ","Neo4j Top 10 Longest GC pauses(3.4+)",1)

        run_shell(" grep -n -i blocked " + logs_directory +
              "/debug.log | sort -r -n -k 11 | head -10","Neo4j Top 10 Longest GC pauses (< 3.4) ",1)

        db('call apoc.meta.stats() yield nodeCount as n, relCount as r with  n, r with (2.0*r/((n-1)*n)) as value return round(100 * value)/100;',"Neo4j Node Density ")

        db('call dbms.listQueries();',"Neo4j Active Queries ")

        db('call dbms.listQueries() yield query, elapsedTimeMillis, queryId, username where elapsedTimeMillis > 60000  and NOT query contains toLower(\"LOAD\") with query, collect(queryId)  as q call dbms.killQueries(q) yield queryId return query, queryId;', "Neo4j Active Long Running Queries ( > 60s )")

        run_shell( bin_directory + "/neo4j-admin memrec ","Recommended Memory Settings",1)

        run_shell("grep -v '^#\' " + conf_directory + "/neo4j.conf | sed -e  '/^$/d' | sort ","Non-default Neo4j.conf settings",1)

    get_config_recommendation()


    #if neo4j_home is not None:
    if bin_directory is not None:
        if ((dbms_mode == "CORE") or (dbms_mode == "READ_REPLICA")):
           db('CALL dbms.cluster.role();',"Neo4j Causal Cluster Instance Role")
           db('CALL dbms.cluster.overview();',"Neo4j Causal Cluster Overview")
           db('CALL dbms.cluster.routing.getServers() ;',"Neo4j Causal Cluster Routing")



        db('call apoc.monitor.tx();',"Neo4j Transaction")
        db('call apoc.monitor.locks(100);',"Neo4j Locks")

        get_errors()


    print ("###################################################################")

    #print ("")
    #print ("Most recent system state changes")
    #print ("================================")
