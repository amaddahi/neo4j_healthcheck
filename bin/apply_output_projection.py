from bin import globals

def run(df,metric_category):

        column_names = list(df)
        if globals.debug:
             print (">>>> Inside apply_output_projections--> ", column_names )
             print ("-----------------------------------------")

        if metric_category == 'check_point':
            #output_keep_list = ['ckp.events_Count', 'ckp.total_time_Sum', 'ckp.check_point_duration_Count', 'ckp.check_point_duration_Avg', 'ckp.check_point_duration_Max']
            output_keep_list = ['ckp.total_time_Sum', 'ckp.check_point_duration_Avg', 'ckp.check_point_duration_Max']
            #output_keep_list = ['ckp.events_Count', 'ckp.total_time_Sum', 'ckp.check_point_duration_Sum', 'ckp.check_point_duration_Count', 'ckp.check_point_duration_Avg', 'ckp.check_point_duration_Max']
        elif metric_category == 'causal_clustering':
            output_keep_list = ['cc.catchup.tx_pull_requests_received_Sum', 'cc.catchup.tx_pull_requests_received_Avg', 'cc.catchup.tx_pull_requests_received_Max' , 'cc.core.append_index_Sum', 'cc.core.append_index_Avg', 'cc.core.append_index_Max', 'cc.core.commit_index_Sum', 'cc.core.commit_index_Avg', 'cc.core.commit_index_Max', 'cc.core.in_flight_cache.element_count_Sum', 'cc.core.in_flight_cache.element_count_Avg', 'cc.core.in_flight_cache.element_count_Max', 'cc.core.in_flight_cache.hits_Sum', 'cc.core.in_flight_cache.hits_Avg', 'cc.core.in_flight_cache.hits_Max', 'cc.core.in_flight_cache.max_bytes_Sum', 'cc.core.in_flight_cache.max_bytes_Avg', 'cc.core.in_flight_cache.max_bytes_Max', 'cc.core.in_flight_cache.max_elements_Sum', 'cc.core.in_flight_cache.max_elements_Avg', 'cc.core.in_flight_cache.max_elements_Max' , 'cc.core.in_flight_cache.misses_Sum', 'cc.core.in_flight_cache.misses_Avg', 'cc.core.in_flight_cache.misses_Max', 'cc.core.in_flight_cache.total_bytes_Sum', 'cc.core.in_flight_cache.total_bytes_Avg', 'cc.core.in_flight_cache.total_bytes_Max', 'cc.core.is_leader_Sum', 'cc.core.is_leader_Avg', 'cc.core.is_leader_Max', 'cc.core.leader_not_found_Sum', 'cc.core.leader_not_found_Avg', 'cc.core.leader_not_found_Max', 'cc.core.message_processing_delay_Sum', 'cc.core.message_processing_delay_Avg', 'cc.core.message_processing_delay_Max', 'cc.core.message_processing_timer.append_entries_request_Sum', 'cc.core.message_processing_timer.append_entries_request_Avg', 'cc.core.message_processing_timer.append_entries_request_Max', 'cc.core.message_processing_timer.append_entries_response_Sum' , 'cc.core.message_processing_timer.append_entries_response_Avg', 'cc.core.message_processing_timer.append_entries_response_Max', 'cc.core.message_processing_timer_Sum'  , 'cc.core.message_processing_timer_Avg', 'cc.core.message_processing_timer_Max', 'cc.core.message_processing_timer.election_timeout_Sum', 'cc.core.message_processing_timer.election_timeout_Avg', 'cc.core.message_processing_timer.election_timeout_Max', 'cc.core.message_processing_timer.heartbeat_Sum', 'cc.core.message_processing_timer.heartbeat_Avg', 'cc.core.message_processing_timer.heartbeat_Max', 'cc.core.message_processing_timer.heartbeat_response_Sum', 'cc.core.message_processing_timer.heartbeat_response_Avg', 'cc.core.message_processing_timer.heartbeat_response_Max', 'cc.core.message_processing_timer.heartbeat_timeout_Sum', 'cc.core.message_processing_timer.heartbeat_timeout_Avg', 'cc.core.message_processing_timer.heartbeat_timeout_Max', 'cc.core.message_processing_timer.log_compaction_info_Sum', 'cc.core.message_processing_timer.log_compaction_info_Avg', 'cc.core.message_processing_timer.log_compaction_info_Max', 'cc.core.message_processing_timer.new_batch_request_Sum', 'cc.core.message_processing_timer.new_batch_request_Avg', 'cc.core.message_processing_timer.new_batch_request_Max', 'cc.core.message_processing_timer.new_entry_request_Sum', 'cc.core.message_processing_timer.new_entry_request_Avg', 'cc.core.message_processing_timer.new_entry_request_Max', 'cc.core.message_processing_timer.pre_vote_request_Sum', 'cc.core.message_processing_timer.pre_vote_response_Sum', 'cc.core.message_processing_timer.prune_request_Sum', 'cc.core.message_processing_timer.prune_request_Avg', 'cc.core.message_processing_timer.prune_request_Max', 'cc.core.message_processing_timer.vote_request_Sum', 'cc.core.message_processing_timer.vote_response_Sum', 'cc.core.replication_attempt_Sum', 'cc.core.replication_attempt_Avg', 'cc.core.replication_attempt_Max', 'cc.core.replication_fail_Sum', 'cc.core.replication_fail_Avg', 'cc.core.replication_fail_Max', 'cc.core.replication_new_Sum', 'cc.core.replication_new_Avg', 'cc.core.replication_new_Max', 'cc.core.replication_success_Sum', 'cc.core.replication_success_Avg', 'cc.core.replication_success_Max', 'cc.core.term_Sum', 'cc.core.term_Avg', 'cc.core.term_Max', 'cc.core.tx_retries_Sum', 'cc.core.tx_retries_Avg', 'cc.core.tx_retries_Max']
        elif metric_category == 'cypher':
            #output_keep_list = ['cyp.replan_events-ps_Sum', 'cyp.replan_events-ps_Avg', 'cyp.replan_events-ps_Max', 'cyp.replan_wait_time_Sum', 'cyp.replan_wait_time_Avg', 'cyp.replan_wait_time_Max']
            output_keep_list = ['cyp.replan_wait_time_Sum', 'cyp.replan_wait_time_Count','cyp.replan_wait_time_Avg', 'cyp.replan_wait_time_Max']
        elif metric_category == 'server':
            output_keep_list = ['srv.threads.jetty.all_Avg', 'srv.threads.jetty.all_Max', 'srv.threads.jetty.idle_Avg', 'srv.threads.jetty.idle_Max']
        elif metric_category == 'log_rotation':
            #output_keep_list = ['log.events_Sum', 'log.events_Avg', 'log.events_Max', 'log.total_time_Sum', 'log.total_time_Avg', 'log.total_time_Max']
            output_keep_list = ['log_rotation.events_Sum', 'log_rotation.events_Avg', 'log_rotation.events_Max', 'log_rotation.total_time_Sum', 'log_rotation.total_time_Avg', 'log_rotation.total_time_Max']
        elif metric_category == 'page_cache':
            output_keep_list = ['pgc.hit_ratio_Avg', 'pgc.hit_ratio_Max', 'pgc.page_faults-ps_Sum', 'pgc.page_faults-ps_Avg', 'pgc.page_faults-ps_Max', 'pgc.hits-ps_Sum', 'pgc.hits-ps_Avg', 'pgc.hits-ps_Max', 'pgc.flushes-ps_Sum', 'pgc.flushes-ps_Avg', 'pgc.flushes-ps_Max', 'pgc.eviction_exceptions-ps_Sum', 'pgc.eviction_exceptions-ps_Avg', 'pgc.eviction_exceptions-ps_Max', 'pgc.evictions-ps_Sum', 'pgc.evictions-ps_Avg', 'pgc.evictions-ps_Max', 'pgc.pins-ps_Sum', 'pgc.pins-ps_Avg', 'pgc.pins-ps_Max', 'pgc.unpins-ps_Sum', 'pgc.unpins-ps_Avg', 'pgc.unpins-ps_Max']
        elif metric_category == 'jvm_gc':
            output_keep_list = ['vm.gc.count.g1_old_generation_Sum',  'vm.gc.count.g1_old_generation_Avg', 'vm.gc.count.g1_old_generation_Max', 'vm.gc.count.g1_young_generation-ps_Sum', 'vm.gc.count.g1_young_generation-ps_Avg', 'vm.gc.count.g1_young_generation-ps_Max', 'vm.gc.time.g1_old_generation_Sum', 'vm.gc.time.g1_old_generation_Avg', 'vm.gc.time.g1_old_generation_Max', 'vm.gc.time.g1_young_generation_Sum', 'vm.gc.time.g1_young_generation_Avg', 'vm.gc.time.g1_young_generation_Max', 'Total_GC_pause_time-ms_Sum', 'Total_GC_pause_time-ms_Avg', 'Total_GC_pause_time-ms_Max']
        elif metric_category == 'jvm_thread':
            output_keep_list = ['vm.thread.count_Sum', 'vm.thread.count_Avg', 'vm.thread.count_Max', 'vm.thread.total_Sum', 'vm.thread.total_Avg', 'vm.thread.total_Max']
        elif metric_category == 'jvm_memory':
            output_keep_list = ['vm.memory.buffer.direct.capacity-mb_Sum', 'vm.memory.buffer.direct.capacity-mb_Avg', 'vm.memory.buffer.direct.capacity-mb_Max', 'vm.memory.buffer.direct.count_Sum', 'vm.memory.buffer.direct.count_Avg', 'vm.memory.buffer.direct.count_Max', 'vm.memory.buffer.direct.used-mb_Sum', 'vm.memory.buffer.direct.used-mb_Avg', 'vm.memory.buffer.direct.used-mb_Max', 'vm.memory.buffer.mapped.capacity-mb_Sum', 'vm.memory.buffer.mapped.capacity-mb_Avg', 'vm.memory.buffer.mapped.capacity-mb_Max', 'vm.memory.buffer.mapped.count_Sum', 'vm.memory.buffer.mapped.count_Avg', 'vm.memory.buffer.mapped.count_Max', 'vm.memory.buffer.mapped.used-mb_Sum', 'vm.memory.buffer.mapped.used-mb_Avg', 'vm.memory.buffer.mapped.used-mb_Max', 'vm.memory.pool.code_cache-mb_Sum', 'vm.memory.pool.code_cache-mb_Avg', 'vm.memory.pool.code_cache-mb_Max', 'vm.memory.pool.compressed_class_space-mb_Sum', 'vm.memory.pool.compressed_class_space-mb_Avg', 'vm.memory.pool.compressed_class_space-mb_Max', 'vm.memory.pool.g1_eden_space-mb_Sum', 'vm.memory.pool.g1_eden_space-mb_Avg', 'vm.memory.pool.g1_eden_space-mb_Max', 'vm.memory.pool.g1_old_gen-mb_Sum', 'vm.memory.pool.g1_old_gen-mb_Avg', 'vm.memory.pool.g1_old_gen-mb_Max', 'vm.memory.pool.g1_survivor_space-mb_Sum', 'vm.memory.pool.g1_survivor_space-mb_Avg', 'vm.memory.pool.g1_survivor_space-mb_Max', 'vm.memory.pool.metaspace-mb_Sum', 'vm.memory.pool.metaspace-mb_Avg', 'vm.memory.pool.metaspace-mb_Max', 'heap_size-mb_Sum', 'heap_size-mb_Avg', 'heap_size-mb_Max']
        elif metric_category == 'transaction':
            output_keep_list = ['tx.peak_concurrent_Avg', 'tx.peak_concurrent_Max',
                                 'tx.started-ps_Sum', 'tx.started-ps_Avg', 'tx.started-ps_Max',
                                 'tx.active_Sum', 'tx.active_Avg', 'tx.active_Max', 'tx.active_read_Sum', 'tx.active_read_Avg', 'tx.active_read_Max', 'tx.active_write_Sum', 'tx.active_write_Avg', 'tx.active_write_Max', 'tx.committed-ps_Sum', 'tx.committed-ps_Avg', 'tx.committed-ps_Max', 'tx.committed_read-ps_Sum', 'tx.committed_read-ps_Avg', 'tx.committed_read-ps_Max', 'tx.committed_write-ps_Sum', 'tx.committed_write-ps_Avg', 'tx.committed_write-ps_Max', 'tx.rollbacks-ps_Sum', 'tx.rollbacks-pshgCount', 'tx.rollbacks-ps_Avg', 'tx.rollbacks-ps_Max', 'tx.rollbacks_read-ps_Sum', 'tx.rollbacks_read-ps_Avg', 'tx.rollbacks_read-ps_Max', 'tx.rollbacks_write-ps_Sum', 'tx.rollbacks_write-ps_Avg', 'tx.rollbacks_write-ps_Max', 'tx.terminated-ps_Sum', 'tx.terminated-ps_Avg', 'tx.terminated-ps_Max', 'tx.terminated_read-ps_Sum', 'tx.terminated_read-ps_Avg', 'tx.terminated_read-ps_Max', 'tx.terminated_write-ps_Sum', 'tx.terminated_write-ps_Avg', 'tx.terminated_write-ps_Max']

        elif metric_category == 'bolt':
            output_keep_list = ['blt.accumulated_processing_time_Sum', 'blt.accumulated_processing_time_Avg', 'blt.accumulated_processing_time_Max', 'blt.accumulated_queue_time_Sum',  'blt.accumulated_queue_time_Avg', 'blt.accumulated_queue_time_Max', 'blt.messages_done-ps_Sum', 'blt.messages_done-ps_Avg', 'blt.messages_done-ps_Max', 'blt.messages_received-ps_Sum', 'blt.messages_received-ps_Avg', 'blt.messages_received-ps_Max', 'blt.messages_failed-ps_Sum', 'blt.messages_failed-ps_Avg', 'blt.messages_failed-ps_Max', 'blt.messages_started-ps_Sum', 'blt.messages_started-ps_Avg', 'blt.messages_started-ps_Max', 'blt.connections_closed-ps_Sum', 'blt.connections_closed-ps_Avg', 'blt.connections_closed-ps_Max', 'blt.connections_opened-ps_Sum', 'blt.connections_opened-ps_Avg', 'blt.connections_opened-ps_Max', 'blt.connections_running-ps_Avg', 'blt.connections_running-ps_Max', 'blt.connections_idle-ps_Avg', 'blt.connections_idle-ps_Max', 'blt.sessions_started-ps_Sum', 'blt.sessions_started-ps_Avg', 'blt.sessions_started-ps_Max']

        elif metric_category == 'object':
            #output_keep_list = ['neo4j.ids_in_use.node_Max', 'neo4j.ids_in_use.property_Max', 'neo4j.ids_in_use.relationship_Max', 'neo4j.ids_in_use.relationship_type_Max']
                    output_keep_list = ['neo4j.ids_in_use.node-ps_Sum', 'neo4j.ids_in_use.node-ps_Avg', 'neo4j.ids_in_use.node-ps_Max',
                            'neo4j.ids_in_use.property-ps_Sum', 'neo4j.ids_in_use.property-ps_Avg', 'neo4j.ids_in_use.property-ps_Max',
                            'neo4j.ids_in_use.relationship-ps_Sum', 'neo4j.ids_in_use.relationship-ps_Avg', 'neo4j.ids_in_use.relationship-ps_Max',
                            'neo4j.ids_in_use.relationship_type-ps_Sum', 'neo4j.ids_in_use.relationship_type-ps_Avg', 'neo4j.ids_in_use.relationship_type-ps_Max']

        elif metric_category == 'store':
                    output_keep_list = [
                            'neo4j.' + globals.database + '.store.size.database_Max',
                            'neo4j.' + globals.database + '.store.size.total_Max']

        elif metric_category == 'count':
                    output_keep_list = [
                            'neo4j.' + globals.database + '.neo4j.count.node_Max',
                            'neo4j.' + globals.database + '.neo4j.count.relationship_Max']

        elif metric_category == 'operation':
                    output_keep_list = [
                    "neo4j.db.operation.count.create_Max",
                    "neo4j.db.operation.count.drop_Max",
                    "neo4j.db.operation.count.failed_Max",
                    "neo4j.db.operation.count.recovered_Max",
                    "neo4j.db.operation.count.start_Max",
                    "neo4j.db.operation.count.stop_Max"
                    ]

        output_delete_list = list(set(column_names) - set(output_keep_list))


        df_output = df.drop(output_delete_list, 1, errors='ignore')

        if globals.debug:
              print ("DF before apply projection")
              print (df.T)
              print("OUTPUT_KEEP_LIST: ", output_keep_list )
              print("OUTPUT_DELETE_LIST: ", output_delete_list )
              print ("DF AFTER apply projection")
              print (df_output.T)
              df_output.T.to_csv(metric_category + "_12_apply_output_before_processing.csv")

        for label in list(df_output):
            if globals.debug:
                 print ("LABELS---->" + label)
                 print (" ")
            pattern_sum='-ps_Sum'
            pattern_count='-ps_Count'
            pattern_avg='-ps_Avg'
            pattern_max='-ps_Max'
            pattern_cc_message='core.message_processing'
            pattern_cc_core='cc.core'

            #if globals.debug:
                #print(label)

            if ((pattern_sum in label) and (metric_category != 'cypher')):
                #if globals.debug:
                      #print('--------')
                      #print(label)
                      #print(df_output[label])
                      #print(globals.metrics_csv_interval)
                df_output[label] = df_output[label]*globals.metrics_csv_interval
                df_output.rename(columns={label: label.replace(
                     pattern_sum, '_Sum')}, inplace=True)
                #print (label + "   " + label.replace(pattern_sum,'_Sum'))
            elif pattern_count in label:
                df_output.rename(columns={label:label.replace(pattern_count,'_Count')}, inplace=True)
                #print (label + "   " + label.replace(pattern_count,'_Count'))
            elif ((pattern_avg in label) and (metric_category == 'bolt') and (('connections_running' in label) or ('connections_idle' in label))) :
                df_output.rename(columns={label:label.replace(pattern_avg,'_Avg')}, inplace=True)
                #print (label + "   " + label.replace(pattern_avg,'_Avg'))
            elif ((pattern_max in label) and (metric_category == 'bolt') and (('connections_running' in label) or ('connections_idle' in label))) :
                df_output.rename(columns={label:label.replace(pattern_max,'_Max')}, inplace=True)
            elif ((pattern_max in label) and (metric_category == 'cypher') and ('event' in label) ) :
                df_output.rename(columns={label:label.replace(pattern_max,'_Max')}, inplace=True)
            elif ((pattern_avg in label) and (metric_category == 'cypher') and ('event' in label) ) :
                df_output.rename(columns={label:label.replace(pattern_avg,'_Avg')}, inplace=True)
            elif (metric_category == 'causal_clustering')  :
                if (pattern_cc_message in label):
                     df_output.rename(columns={label:label.replace(pattern_cc_message,'msg_proc')}, inplace=True)
                elif (pattern_cc_core in label) :
                     df_output.rename(columns={label:label.replace(pattern_cc_core,'cc')}, inplace=True)

            #print (label + "   " + label.replace(pattern_max,'_Max'))


        for label in list(df_output):
            df_output.rename(columns={label:label.ljust(50," ")}, inplace=True)

        if globals.debug:
              print ("DF after apply projection")
              print (df_output.T)
              df_output.T.to_csv(metric_category + "_13_apply_output_after_processing.csv")
        return df_output
