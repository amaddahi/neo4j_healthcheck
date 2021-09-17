from bin import globals

def check_size():

    global logs_directory
    global data_directory

    run_shell("df -H -P -l ","Disk Utilization",1)
    db('call apoc.monitor.store();',"Neo4j Store Size")
    run_shell("grep 'Total size' " + logs_directory + "/debug.log","Database/Index Size History",1)
    run_shell("du -h -d1 " + data_directory +   "/databases/graph.db" ,"Database Size",1)
    run_shell("du -h -d1 " + data_directory +   "/databases/graph.db/*tran*" ,"Transaction Logs",1)
