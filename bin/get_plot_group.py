from bin import globals

def run(metric_category):
    if metric_category == 'transaction':
        plot_group = [
            ["peak_concurrent"],
            ["active", "started"],
            ["committed", "rollbacks"],
            ["terminated"]
        ]
    elif metric_category == 'query':
        plot_group = [
            ["query"]
        ]
    elif metric_category == 'store':
        plot_group = [
            ["store"]
        ]
    elif metric_category == 'count':
        plot_group = [
            ["count"]
        ]
    elif metric_category == 'log_rotation':
        plot_group = [
            ["rotation"]
        ]
    elif metric_category == 'server':
        plot_group = [
            ["jetty"]
        ]
    elif metric_category == 'object':
        plot_group = [
            ["Max"]
        ]
    elif metric_category == 'operation':
        plot_group = [
            ["operation"]
        ]
    elif metric_category == 'network':
        plot_group = [
            ["network"]
        ]
    elif metric_category == 'cypher':
        plot_group = [
            ["replan"]
        ]
    elif metric_category == 'bolt':
        plot_group = [
            ["accumulated"],
            ["messages", "sessions"],
            ["connection"]
        ]
    elif metric_category == 'page_cache':
        plot_group = [
            ["hit_ratio"],
            ["hits", "flushes"],
            ["eviction"],
            ["pin"]
        ]
    elif metric_category == 'check_point':
        plot_group = [
            ["duration","ckp.total_time_Sum"],
            ["total_time"],
            ["events"]
        ]
    elif metric_category == 'jvm_thread':
        plot_group = [
            ["thread"]
        ]
    elif metric_category == 'jvm_gc':
        plot_group = [
            ["count"],
            ["time"]
        ]
    elif metric_category == 'jvm_thread':
        plot_group = [
            ["direct"]
        ]
    elif metric_category == 'jvm_memory':
        plot_group = [
            ["direct"],
            ["mapped"],
            ["code-cache"],
            ["compressed_class_space"],
            ["g1"],
            ["metaspace"]

        ]
    elif metric_category == 'causal_clustering':
        plot_group = [
            ["election_timeout"],
            ["pre_vote"],
            [".vote_request",".vote_response"],
            ["heartbeat"],
            ["catchup"],
            ["prune_request"],
            ["tx_retries"],
            ["message_processing_delay"],
            ["append_entries_request","append_entries_response"],
            ["log_compaction_info"],
            ["new_batch_request","new_entry_request"],
            ["term"],
            ["is_leader"],
            ["leader_not_found"],
            ["element_count"],
            ["hits","misses"],
            ["max_bytes"],
            ["max_elements"],
            ["total_bytes"],
            ["replication_success","replication_fail"],
            ["replication_new","replication_attempt"],
            ["index"]
        ]

    return plot_group
