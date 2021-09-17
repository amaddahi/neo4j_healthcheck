from bin import globals
import os


def run(metric_category):
    #print (">>> Inside get_filenames.run")
    #print ("metric_category-->" + metric_category)
    #print ("-----------")
    #print(" ")
    if metric_category == 'operation':
        filenames = [
            ["neo4j.db.operation.count.create.csv", 0, ""],
            ["neo4j.db.operation.count.drop.csv", 0, ""],
            ["neo4j.db.operation.count.failed.csv", 0, ""],
            ["neo4j.db.operation.count.recovered.csv", 0, ""],
            ["neo4j.db.operation.count.start.csv", 0, ""],
            ["neo4j.db.operation.count.stop.csv", 0, ""]
        ]
    elif metric_category == 'server':
        filenames = [
            ["neo4j.server.threads.jetty.all.csv", 0, ""],
            ["neo4j.server.threads.jetty.idle.csv", 0, ""]
        ]
    elif metric_category == 'query':
        filenames = [
            ["neo4j.long_running_queries.csv", 0, ""]
        ]
    elif metric_category == 'log_rotation':
        filenames = [
            ["neo4j." + globals.database + ".log.rotation_events.csv", 0, "", "neo4j.log_rotation.events.csv"]
            #["neo4j." + globals.database + ".log.rotation.total_time.csv", 2, "", "neo4j.log.rotation.total_time.csv"]
    ]
    elif metric_category == 'causal_clustering':
        filenames = [
            ["neo4j.causal_clustering.catchup.tx_pull_requests_received.csv",1,""],
            ["neo4j.causal_clustering.core.append_index.csv",1,""],
            ["neo4j.causal_clustering.core.commit_index.csv",1,""],
            #["neo4j.causal_clustering.core.dropped_messages.csv",1,""],     # TODO: configurable
            ["neo4j.causal_clustering.core.in_flight_cache.element_count.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.hits.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.max_bytes.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.max_elements.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.misses.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.total_bytes.csv",1,""],
            ["neo4j.causal_clustering.core.is_leader.csv",0,""],    # either 0 or 1
            ["neo4j.causal_clustering.core.leader_not_found.csv",1,""],
            ["neo4j.causal_clustering.core.message_processing_delay.csv",0,""],                     # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.append_entries_request.csv",0,""], # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.append_entries_response.csv",0,""],# calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.csv",0,""],                     # CuC or CuT calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.election_timeout.csv",0,""],
            ["neo4j.causal_clustering.core.message_processing_timer.heartbeat.csv",0,""],           # CuC or CuT calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.heartbeat_response.csv",0,""],  # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.heartbeat_timeout.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.log_compaction_info.csv",0,""], # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.new_batch_request.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.new_entry_request.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.pre_vote_request.csv",0,""],    # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.pre_vote_response.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.prune_request.csv",0,""],       # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.vote_request.csv",0,""],        # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.vote_response.csv",0,""],       # calls/second,milliseconds
            #["neo4j.causal_clustering.core.queue_sizes.csv",0,""],          #TODO: configurable
            ["neo4j.causal_clustering.core.replication_attempt.csv",1,""],
            ["neo4j.causal_clustering.core.replication_fail.csv",1,""],
            ["neo4j.causal_clustering.core.replication_new.csv",1,""],
            ["neo4j.causal_clustering.core.replication_success.csv",1,""],
            ["neo4j.causal_clustering.core.term.csv",1,""],
            ["neo4j.causal_clustering.core.tx_retries.csv",0,""]
        ]
    elif metric_category == 'network':
        filenames = [
            ["neo4j.network.master_network_store_writes.csv", 0, ""],
            ["neo4j.network.master_network_tx_writes.csv", 0, ""],
            ["neo4j.network.slave_network_tx_writes.csv", 0, ""]
        ]


    elif metric_category == 'store':
        filenames = [
            #["neo4j." + globals.database + ".store.size.database.csv", 0, "", "neo4j.store.size.database.csv"],
            #["neo4j." + globals.database + ".store.size.total.csv", 0, "", "neo4j.store.size.total.csv"]
            ["neo4j." + globals.database + ".store.size.database.csv", 0, "", ""],
            ["neo4j." + globals.database + ".store.size.total.csv", 0, "", ""]
        ]

    elif metric_category == 'count':
        filenames = [
            ["neo4j." + globals.database + ".neo4j.count.node.csv" ,0,"", ""],
            ["neo4j." + globals.database + ".neo4j.count.relationship.csv", 0, "", ""]
        ]
    elif metric_category == 'object':
        filenames = [
            ["neo4j." + globals.database + ".ids_in_use.node.csv", 1, "-ps", "neo4j.ids_in_use.node.csv"],
            ["neo4j." + globals.database + ".ids_in_use.property.csv", 1, "-ps", "neo4j.ids_in_use.property.csv"],
            ["neo4j." + globals.database + ".ids_in_use.relationship.csv", 1, "-ps", "neo4j.ids_in_use.relationship.csv"],
            ["neo4j." + globals.database + ".ids_in_use.relationship_type.csv", 1, "-ps", "neo4j.ids_in_use.relationship_type.csv"]
        ]

    elif metric_category == 'transaction':
        filenames = [
            ["neo4j." + globals.database + ".transaction.peak_concurrent.csv", 0, "", "neo4j.transaction.peak_concurrent.csv"],
            ["neo4j." + globals.database + ".transaction.started.csv", 1, "-ps", "neo4j.transaction.started.csv"],
            ["neo4j." + globals.database + ".transaction.active.csv", 0, "-ps", "neo4j.transaction.active.csv"],
            ["neo4j." + globals.database + ".transaction.active_read.csv", 0, "-ps", "neo4j.transaction.active_read.csv"],
            ["neo4j." + globals.database + ".transaction.active_write.csv", 0, "-ps", "neo4j.transaction.active_write.csv"],
            ["neo4j." + globals.database + ".transaction.committed.csv", 1, "-ps", "neo4j.transaction.committed.csv"],
            ["neo4j." + globals.database + ".transaction.committed_read.csv", 1, "-ps", "neo4j.transaction.committed_read.csv"],
            ["neo4j." + globals.database + ".transaction.committed_write.csv", 1, "-ps", "neo4j.transaction.committed_write.csv"],
            ["neo4j." + globals.database + ".transaction.rollbacks.csv", 1, "-ps", "neo4j.transaction.rollbacks.csv"],
            ["neo4j." + globals.database + ".transaction.rollbacks_read.csv", 1, "-ps", "neo4j.transaction.rollbacks_read.csv"],
            ["neo4j." + globals.database + ".transaction.rollbacks_write.csv", 1, "-ps", "neo4j.transaction.rollbacks_write.csv"],
            ["neo4j." + globals.database + ".transaction.terminated.csv", 1, "-ps", "neo4j.transaction.terminated.csv"],
            ["neo4j." + globals.database + ".transaction.terminated_read.csv", 1, "-ps", "neo4j.transaction.terminated_read.csv"],
            ["neo4j." + globals.database + ".transaction.terminated_write.csv", 1, "-ps", "neo4j.transaction.terminated_write.csv"]
       ]

    elif metric_category == 'bolt':
        filenames = [
            ["neo4j.bolt.accumulated_processing_time.csv", 2, ""],
            ["neo4j.bolt.accumulated_queue_time.csv", 2, ""],
            ["neo4j.bolt.messages_done.csv", 1, "-ps"],
            ["neo4j.bolt.messages_received.csv", 1, "-ps"],
            ["neo4j.bolt.messages_failed.csv",1, "-ps"],
            ["neo4j.bolt.messages_started.csv", 1, "-ps"],
            ["neo4j.bolt.connections_closed.csv", 1, "-ps"],
            ["neo4j.bolt.connections_opened.csv", 1, "-ps"],
            ["neo4j.bolt.connections_running.csv", 0, "-ps"],
            ["neo4j.bolt.connections_idle.csv", 0, "-ps"],
            ["neo4j.bolt.sessions_started.csv", 1, "-ps"]
        ]
    elif metric_category == 'bolt2':
        filenames = [
            ["neo4j.bolt.accumulated_queue_time.csv", 2, ""],
            ["neo4j.bolt.messages_done.csv", 1, "-ps"]
        ]
    elif metric_category == 'cypher':
        filenames = [
            ["neo4j." + globals.database + ".cypher.replan_events.csv", 1, "-ps", "neo4j.cypher.replan_events.csv"],
            ["neo4j." + globals.database + ".cypher.replan_wait_time.csv", 2, "", "neo4j.cypher.replan_wait_time.csv"]
        ]

    elif metric_category == 'page_cache':
        filenames = [
            ["neo4j.page_cache.hit_ratio.csv", 0, ""],
            ["neo4j.page_cache.page_faults.csv", 1, "-ps"],
            ["neo4j.page_cache.hits.csv", 1, "-ps"],
            ["neo4j.page_cache.flushes.csv", 1, "-ps"],
            ["neo4j.page_cache.eviction_exceptions.csv", 1, "-ps"],
            ["neo4j.page_cache.evictions.csv", 1, "-ps"],
            ["neo4j.page_cache.pins.csv", 1, "-ps"],
            ["neo4j.page_cache.unpins.csv", 1, "-ps"]
        ]
    elif metric_category == 'check_point':
        filenames = [
            # collected at checkpoint times only and thus far less frequently collected than other datapointsk
            ["neo4j." + globals.database + ".check_point.events.csv", 0, "", "neo4j.check_point.events.csv"],
            ["neo4j." + globals.database + ".check_point.duration.csv", 3, "", "neo4j.check_point.check_point_duration.csv"],
            ["neo4j." + globals.database + ".check_point.total_time.csv", 2, "", "neo4j.check_point.total_time.csv"]
        ]


    elif metric_category == 'jvm_thread':
        filenames = [
            ["neo4j.vm.thread.total.csv", 0, "", "vm.thread.count.csv","vm.thread.count"],
            ["neo4j.vm.thread.count.csv", 0, "", "vm.thread.total.csv","vm.thread.total"]
        ]
    elif metric_category == 'jvm_gc2':
        filenames = [
            #["vm.gc.time.g1_young_generation.csv", 2, ""],
            #["vm.gc.time.g1_old_generation.csv", 2, ""]
       ]
    elif metric_category == 'jvm_gc':
        filenames = [
            ["neo4j.vm.gc.count.g1_old_generation.csv", 0, "", "vm.gc.count.g1_old_generation.csv"],
            ["neo4j.vm.gc.count.g1_young_generation.csv", 1, "-ps","vm.gc.count.g1_young_generation.csv"],
            ["neo4j.vm.gc.time.g1_old_generation.csv", 2, "" , "vm.gc.time.g1_old_generation.csv"],
            ["neo4j.vm.gc.time.g1_young_generation.csv",2,"","vm.gc.time.g1_young_generation.csv"]
        ]
    elif metric_category == 'jvm_memory':
        filenames = [
            #neo4j.vm.file.descriptors.count.csv
            #neo4j.vm.file.descriptors.maximum.csv
            #neo4j.vm.heap.committed.csv
            #neo4j.vm.heap.max.csv
            #neo4j.vm.heap.used.csv
            #neo4j.vm.memory.pool.codeheap_'non-nmethods'.csv
            #neo4j.vm.memory.pool.codeheap_'non-profiled_nmethods'.csv
            #neo4j.vm.memory.pool.codeheap_'profiled_nmethods'.csv
            #neo4j.vm.pause_time.csv
            #["vm.memory.pool.code_cache.csv", 0, "-mb"],
            ["neo4j.vm.memory.buffer.direct.capacity.csv", 0, "-mb","vm.memory.buffer.direct.capacity.csv"],
            ["neo4j.vm.memory.buffer.direct.count.csv", 0, "", "vm.memory.buffer.direct.count.csv"],
            ["neo4j.vm.memory.buffer.direct.used.csv", 0,"-mb","vm.memory.buffer.direct.used.csv"],
            ["neo4j.vm.memory.buffer.mapped.capacity.csv", 0,"-mb","vm.memory.buffer.mapped.capacity.csv" ],
            ["neo4j.vm.memory.buffer.mapped.count.csv", 0,"","vm.memory.buffer.mapped.count.csv"],
            ["neo4j.vm.memory.buffer.mapped.used.csv", 0,"-mb","vm.memory.buffer.mapped.used.csv"],
            ["neo4j.vm.memory.pool.compressed_class_space.csv",0,"-mb","vm.memory.pool.compressed_class_space.csv"],
            ["neo4j.vm.memory.pool.g1_eden_space.csv",0,"-mb","vm.memory.pool.g1_eden_space.csv"],
            ["neo4j.vm.memory.pool.g1_old_gen.csv",0,"-mb","vm.memory.pool.g1_old_gen.csv"],
            ["neo4j.vm.memory.pool.g1_survivor_space.csv",0,"-mb","vm.memory.pool.g1_survivor_space.csv"],
            ["neo4j.vm.memory.pool.metaspace.csv",0,"-mb","vm.memory.pool.metaspace.csv"]
        ]
    else:
        print ("Exiting:   Incorrect Metric Type: " + metric_category)
        exit(5)

    filenames_keep=[]
    filenames_delete=[]
    i=0
    for file in filenames:
       metrics_file = globals.metrics_directory + "/" + file[0]
       if globals.debug:
           print ("metric_fie--> " + metrics_file)
       if not os.path.isfile(metrics_file):
            filenames_delete.append(file)
            print ("Missing Metric File" + metrics_file)
       else:
            filenames_keep.append(file)

       i=i+1

    if globals.debug:
        print (filenames_keep)

    if len(filenames_keep) == 0:
        print (" ")
        print ("No Matching metric file names found.   Please ensure the correct database name is being referenced here--> " + globals.database)
        print (" ")
        exit(1)

    return filenames_keep

def merge_rotated_files(metrics_category):

    if debug:
         print ("  ")
         print ("merged_rotated_files......START")
    filenames = get_filenames(metrics_category)

    for file in filenames:

       cmd = 'cd '  + globals.metrics_directory + ';ls -r ' + file[0] + '*  | xargs cat > ' + file[0] + '.merged_rotated_files' + ' 2> /dev/null'
       os.system(cmd)

       #if debug:
           #print(cmd)

       #if  metrics_category == 'transaction':
           #cmd = 'cd '  + globals.metrics_directory + '; cp ' + file[0] + '.merged_rotated_files '  + file[3]
           #os.system(cmd)

def run2(metric_category):
    #globals.initialize()
    if metric_category == 'operation':
        filenames = [
            ["neo4j.db.operation.count.create.csv", 0, "","db.operation.count.create.csv"],
            ["neo4j.db.operation.count.drop.csv", 0, "","db.operation.count.drop.csv"],
            ["neo4j.db.operation.count.failed.csv", 0, "","db.operation.count.failed.csv",],
            ["neo4j.db.operation.count.recovered.csv", 0, "","db.operation.count.recovered.csv"],
            ["neo4j.db.operation.count.start.csv", 0, "","db.operation.count.start.csv"],
            ["neo4j.db.operation.count.stop.csv", 0, "","db.operation.count.stop.csv"]
        ]
    elif metric_category == 'server':
        filenames = [
            ["neo4j.server.threads.jetty.all.csv", 0, ""],
            ["neo4j.server.threads.jetty.idle.csv", 0, ""]
        ]
    elif metric_category == 'query':
        filenames = [
            ["neo4j.long_running_queries.csv", 0, ""]
        ]
    elif metric_category == 'log_rotation':
        filenames = [
            ["neo4j." + globals.database + ".log.rotation_events.csv", 0, "", "neo4j.log_rotation.events.csv"]
            #["neo4j." + globals.database + ".log.rotation.total_time.csv", 2, "", "neo4j.log.rotation.total_time.csv"]
    ]
    elif metric_category == 'causal_clustering':
        filenames = [
            ["neo4j.causal_clustering.catchup.tx_pull_requests_received.csv",1,""],
            ["neo4j.causal_clustering.core.append_index.csv",1,""],
            ["neo4j.causal_clustering.core.commit_index.csv",1,""],
            #["neo4j.causal_clustering.core.dropped_messages.csv",1,""],     # TODO: configurable
            ["neo4j.causal_clustering.core.in_flight_cache.element_count.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.hits.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.max_bytes.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.max_elements.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.misses.csv",1,""],
            ["neo4j.causal_clustering.core.in_flight_cache.total_bytes.csv",1,""],
            ["neo4j.causal_clustering.core.is_leader.csv",0,""],    # either 0 or 1
            ["neo4j.causal_clustering.core.leader_not_found.csv",1,""],
            ["neo4j.causal_clustering.core.message_processing_delay.csv",0,""],                     # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.append_entries_request.csv",0,""], # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.append_entries_response.csv",0,""],# calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.csv",0,""],                     # CuC or CuT calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.election_timeout.csv",0,""],
            ["neo4j.causal_clustering.core.message_processing_timer.heartbeat.csv",0,""],           # CuC or CuT calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.heartbeat_response.csv",0,""],  # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.heartbeat_timeout.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.log_compaction_info.csv",0,""], # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.new_batch_request.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.new_entry_request.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.pre_vote_request.csv",0,""],    # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.pre_vote_response.csv",0,""],   # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.prune_request.csv",0,""],       # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.vote_request.csv",0,""],        # calls/second,milliseconds
            ["neo4j.causal_clustering.core.message_processing_timer.vote_response.csv",0,""],       # calls/second,milliseconds
            #["neo4j.causal_clustering.core.queue_sizes.csv",0,""],          #TODO: configurable
            ["neo4j.causal_clustering.core.replication_attempt.csv",1,""],
            ["neo4j.causal_clustering.core.replication_fail.csv",1,""],
            ["neo4j.causal_clustering.core.replication_new.csv",1,""],
            ["neo4j.causal_clustering.core.replication_success.csv",1,""],
            ["neo4j.causal_clustering.core.term.csv",1,""],
            ["neo4j.causal_clustering.core.tx_retries.csv",0,""]
        ]
    elif metric_category == 'network':
        filenames = [
            ["neo4j.network.master_network_store_writes.csv", 0, ""],
            ["neo4j.network.master_network_tx_writes.csv", 0, ""],
            ["neo4j.network.slave_network_tx_writes.csv", 0, ""]
        ]

    elif metric_category == 'store':
        filenames = [
            ["neo4j." + globals.database + ".store.size.database.csv", 0, "", "neo4j.store.size.database.csv", "store.size.database.csv"],
            ["neo4j." + globals.database + ".store.size.total.csv", 0, "", "neo4j.store.size.total.csv","store.size.total.csv"]
        ]

    elif metric_category == 'object':
        filenames = [
            ["neo4j." + globals.database + ".ids_in_use.node.csv", 1, "-ps", "neo4j.ids_in_use.node.csv"],
            ["neo4j." + globals.database + ".ids_in_use.property.csv", 1, "-ps", "neo4j.ids_in_use.property.csv"],
            ["neo4j." + globals.database + ".ids_in_use.relationship.csv", 1, "-ps", "neo4j.ids_in_use.relationship.csv"],
            ["neo4j." + globals.database + ".ids_in_use.relationship_type.csv", 1, "-ps", "neo4j.ids_in_use.relationship_type.csv"]
        ]

    elif metric_category == 'transaction':
        filenames = [
            ["neo4j." + globals.database + ".transaction.peak_concurrent.csv", 0, "", "neo4j.transaction.peak_concurrent.csv"],
            ["neo4j." + globals.database + ".transaction.started.csv", 1, "-ps", "neo4j.transaction.started.csv"],
            ["neo4j." + globals.database + ".transaction.active.csv", 0, "-ps", "neo4j.transaction.active.csv"],
            ["neo4j." + globals.database + ".transaction.active_read.csv", 0, "-ps", "neo4j.transaction.active_read.csv"],
            ["neo4j." + globals.database + ".transaction.active_write.csv", 0, "-ps", "neo4j.transaction.active_write.csv"],
            ["neo4j." + globals.database + ".transaction.committed.csv", 1, "-ps", "neo4j.transaction.committed.csv"],
            ["neo4j." + globals.database + ".transaction.committed_read.csv", 1, "-ps", "neo4j.transaction.committed_read.csv"],
            ["neo4j." + globals.database + ".transaction.committed_write.csv", 1, "-ps", "neo4j.transaction.committed_write.csv"],
            ["neo4j." + globals.database + ".transaction.rollbacks.csv", 1, "-ps", "neo4j.transaction.rollbacks.csv"],
            ["neo4j." + globals.database + ".transaction.rollbacks_read.csv", 1, "-ps", "neo4j.transaction.rollbacks_read.csv"],
            ["neo4j." + globals.database + ".transaction.rollbacks_write.csv", 1, "-ps", "neo4j.transaction.rollbacks_write.csv"],
            ["neo4j." + globals.database + ".transaction.terminated.csv", 1, "-ps", "neo4j.transaction.terminated.csv"],
            ["neo4j." + globals.database + ".transaction.terminated_read.csv", 1, "-ps", "neo4j.transaction.terminated_read.csv"],
            ["neo4j." + globals.database + ".transaction.terminated_write.csv", 1, "-ps", "neo4j.transaction.terminated_write.csv"]
       ]

    elif metric_category == 'bolt':
        filenames = [
            ["neo4j.bolt.accumulated_processing_time.csv", 2, "","bolt.accumulated_processing_time.csv"],
            ["neo4j.bolt.accumulated_queue_time.csv", 2, "","bolt.accumulated_queue_time.csv"],
            ["neo4j.bolt.messages_done.csv", 1, "-ps","bolt.messages_done.csv"],
            ["neo4j.bolt.messages_received.csv", 1, "-ps","bolt.messages_received.csv"],
            ["neo4j.bolt.messages_failed.csv",1, "-ps","bolt.messages_failed.csv"],
            ["neo4j.bolt.messages_started.csv", 1, "-ps","bolt.messages_started.csv"],
            ["neo4j.bolt.connections_closed.csv", 1, "-ps","bolt.connections_closed.csv"],
            ["neo4j.bolt.connections_opened.csv", 1, "-ps","bolt.connections_opened.csv"],
            ["neo4j.bolt.connections_running.csv", 0, "-ps","bolt.connections_running.csv"],
            ["neo4j.bolt.connections_idle.csv", 0, "-ps","bolt.connections_idle.csv"],
            ["neo4j.bolt.sessions_started.csv", 1, "-ps","bolt.sessions_started.csv"]
        ]
    elif metric_category == 'bolt2':
        filenames = [
            ["neo4j.bolt.accumulated_queue_time.csv", 2, ""],
            ["neo4j.bolt.messages_done.csv", 1, "-ps"]
        ]
    elif metric_category == 'cypher':
        filenames = [
            ["neo4j." + globals.database + ".cypher.replan_events.csv", 1, "-ps", "neo4j.cypher.replan_events.csv"],
            ["neo4j." + globals.database + ".cypher.replan_wait_time.csv", 2, "", "neo4j.cypher.replan_wait_time.csv"]
        ]

    elif metric_category == 'page_cache':
        filenames = [
            ["neo4j.page_cache.hit_ratio.csv", 0, ""],
            ["neo4j.page_cache.page_faults.csv", 1, "-ps"],
            ["neo4j.page_cache.hits.csv", 1, "-ps"],
            ["neo4j.page_cache.flushes.csv", 1, "-ps"],
            ["neo4j.page_cache.eviction_exceptions.csv", 1, "-ps"],
            ["neo4j.page_cache.evictions.csv", 1, "-ps"],
            ["neo4j.page_cache.pins.csv", 1, "-ps"],
            ["neo4j.page_cache.unpins.csv", 1, "-ps"]
        ]
    elif metric_category == 'check_point':
        filenames = [
            # collected at checkpoint times only and thus far less frequently collected than other datapointsk
            ["neo4j." + globals.database + ".check_point.events.csv", 0, "", "neo4j.check_point.events.csv"],
            ["neo4j." + globals.database + ".check_point.duration.csv", 3, "", "neo4j.check_point.check_point_duration.csv"],
            ["neo4j." + globals.database + ".check_point.total_time.csv", 2, "", "neo4j.check_point.total_time.csv"]
        ]


    elif metric_category == 'jvm_thread':
        filenames = [
            ["neo4j.vm.thread.total.csv", 0, "", "vm.thread.count.csv","vm.thread.count"],
            ["neo4j.vm.thread.count.csv", 0, "", "vm.thread.total.csv","vm.thread.total"]
        ]
    elif metric_category == 'jvm_gc2':
        filenames = [
            #["vm.gc.time.g1_young_generation.csv", 2, ""],
            #["vm.gc.time.g1_old_generation.csv", 2, ""]
       ]
    elif metric_category == 'jvm_gc':
        filenames = [
            ["neo4j.vm.gc.count.g1_old_generation.csv", 0, "", "vm.gc.count.g1_old_generation.csv"],
            ["neo4j.vm.gc.count.g1_young_generation.csv", 1, "-ps","vm.gc.count.g1_young_generation.csv"],
            ["neo4j.vm.gc.time.g1_old_generation.csv", 2, "" , "vm.gc.time.g1_old_generation.csv"],
            ["neo4j.vm.gc.time.g1_young_generation.csv",2,"","vm.gc.time.g1_young_generation.csv"]
        ]
    elif metric_category == 'jvm_memory':
        filenames = [
            #neo4j.vm.file.descriptors.count.csv
            #neo4j.vm.file.descriptors.maximum.csv
            #neo4j.vm.heap.committed.csv
            #neo4j.vm.heap.max.csv
            #neo4j.vm.heap.used.csv
            #neo4j.vm.memory.pool.codeheap_'non-nmethods'.csv
            #neo4j.vm.memory.pool.codeheap_'non-profiled_nmethods'.csv
            #neo4j.vm.memory.pool.codeheap_'profiled_nmethods'.csv
            #neo4j.vm.pause_time.csv
            #["vm.memory.pool.code_cache.csv", 0, "-mb"],
            ["neo4j.vm.memory.buffer.direct.capacity.csv", 0, "-mb","vm.memory.buffer.direct.capacity.csv"],
            ["neo4j.vm.memory.buffer.direct.count.csv", 0, "", "vm.memory.buffer.direct.count.csv"],
            ["neo4j.vm.memory.buffer.direct.used.csv", 0,"-mb","vm.memory.buffer.direct.used.csv"],
            ["neo4j.vm.memory.buffer.mapped.capacity.csv", 0,"-mb","vm.memory.buffer.mapped.capacity.csv" ],
            ["neo4j.vm.memory.buffer.mapped.count.csv", 0,"","vm.memory.buffer.mapped.count.csv"],
            ["neo4j.vm.memory.buffer.mapped.used.csv", 0,"-mb","vm.memory.buffer.mapped.used.csv"],
            ["neo4j.vm.memory.pool.compressed_class_space.csv",0,"-mb","vm.memory.pool.compressed_class_space.csv"],
            ["neo4j.vm.memory.pool.g1_eden_space.csv",0,"-mb","vm.memory.pool.g1_eden_space.csv"],
            ["neo4j.vm.memory.pool.g1_old_gen.csv",0,"-mb","vm.memory.pool.g1_old_gen.csv"],
            ["neo4j.vm.memory.pool.g1_survivor_space.csv",0,"-mb","vm.memory.pool.g1_survivor_space.csv"],
            ["neo4j.vm.memory.pool.metaspace.csv",0,"-mb","vm.memory.pool.metaspace.csv"]
        ]
    else:
        print ("Exiting:   Incorrect Metric Type: " + metric_category)
        exit(5)

    filenames_keep=[]
    filenames_delete=[]
    i=0
    for file in filenames:
       metrics_file = globals.metrics_directory + "/" + file[0]
       if debug:
           print (metrics_file)
       if not os.path.isfile(metrics_file):
            filenames_delete.append(file)
            print ("Missing Metric File" + metrics_file)
       else:
            filenames_keep.append(file)

       i=i+1

    if globals.debug:
        print (filenames_keep)

    return filenames_keep
