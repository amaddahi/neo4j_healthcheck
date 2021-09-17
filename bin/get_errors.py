from bin import globals

def get_errors():

        global logs_directory

        error_keep_list=["Deprecated index providers","Caused by","o.n.c.c.c.RaftMachine", "o.n.c.c.c.s.RaftState","o.n.c.c.c.s.RaftLogShipper","o.n.c.c.c.m.RaftMembershipChanger","o.n.c.c.c.m.RaftMembershipManager","o.n.c.m.RaftOutbound","o.n.k.i.c.MonitorGc","o.n.c.d.HazelcastCoreTopologyService","o.n.c.c.c.m.MembershipWaiterLifecycle","o.n.k.AvailabilityGuard","o.n.i.p.PageCache","o.n.c.i.ClusterBinder","o.n.k.i.DatabaseHealth","o.n.c.c.s.s.CoreStateDownloader","o.n.c.c.IdentityModule","GetOperation","ERROR","WARN","o.n.k.i.f.GraphDatabaseFacadeFactory"]


        print ("###################################################################")
        print ("")
        print ("Interesting Messages in Debug.log")
        print ("")

        debug_file = logs_directory + "/debug.log"
        f = open(debug_file, "r")
        lines = f.readlines()
        f.close()

        debug_filtered_file = logs_directory + "/filtered_debug.log"
        f = open(debug_filtered_file, "w")

        for line in lines:
            for error in error_keep_list:
                if (error in line) and ('Failed to load') not in line:
                     f.write("----> " + line)
        f.close()

        f = open(debug_filtered_file, "r")
        lines = f.readlines()
        f.close()

        line_count=len(lines)
        i=0
        for line in lines:
              i=i+1
              if i >= (line_count - 100 ):
                   print(line , end = '')
