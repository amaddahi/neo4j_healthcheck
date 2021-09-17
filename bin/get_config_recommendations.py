from bin import globals

def get_config_recommendation():


    if conf_directory is not None:
       config_file = '/tmp/file.out'
       f = open(config_file, "r")
       lines = f.readlines()
       f.close()

       config_on_list=[]
       #config_list=["dbms.memory.pagecache.size","dbms.memory.heap.max_size","dbms.memory.heap.initial_size","causal_clustering.enable_pre_voting","dbms.backup.enabled"]
       #config_list=["dbms.memory.pagecache.size","dbms.memory.heap.max_size","dbms.memory.heap.initial_size","causal_clustering.enable_pre_voting"]
       config_list=["dbms.memory.pagecache.size","dbms.memory.heap.max_size","dbms.memory.heap.initial_size","causal_clustering.enable_pre_voting","causal_clustering.leader_election_timeout","causal_clustering.refuse_to_be_leader","causal_clustering.enable_pre_voting","dbms.tx_log.rotation.retention_policy","dbms.connector.bolt.thread_pool_max_size","causal_clustering.multi_dc_license","dbms.checkpoint.iops.limit","dbms.security.procedures.unrestricted"]

       for cfg in config_list:
          for line in lines:
            if cfg in line:
               config_on_list.append(cfg)
               print(config_on_list)


       config_off_list = list(set(config_list) - set(list(config_on_list)))

       os.system("grep 'dbms.mode' /tmp/file.out > /tmp/neo4j.tmp")
       config = ConfigObj('/tmp/neo4j.tmp')
       dbms_mode=config.get('dbms.mode')

       print(' ')
       for item in sorted(config_off_list):
                 if "causal_clustering" not in item:
                      print("[WARNING]:  Please set the following in neo4j.conf: (" + item + ")" )

       if dbms_mode=="CORE":
           if 'causal_clustering.enable_pre_voting' in config_off_list:
                 print("[WARNING]:  Please set the following in neo4j.conf: (causal_clustering.enable_pre_voting)" )
       print(' ')
    return

