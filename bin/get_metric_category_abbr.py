from bin import globals

def run(file_type):

    if globals.debug:
        print(" ")
        print(">>>>> Inside get_metric_category_abbr module - filetype: " + file_type)
        print("-----------------------------------------------")

    if file_type == "transaction":
        metric_category_abbr = "tx."
        db_category_abbr = "neo4j."
    elif file_type == "store":
        metric_category_abbr = "store."
        db_category_abbr = "neo4j."
    elif file_type == "operation":
        metric_category_abbr = "operation"
        db_category_abbr = "neo4j."  
    elif file_type == "page_cache":
        metric_category_abbr = "pgc."
        db_category_abbr = "neo4j."
    elif file_type == "bolt":
        metric_category_abbr = "blt."
        db_category_abbr = "neo4j."
    elif file_type == "causal_clustering":
        metric_category_abbr = "cc."
        db_category_abbr = "neo4j."
    elif file_type == "cypher":
        metric_category_abbr = "cyp."
        db_category_abbr = "neo4j."
    elif file_type == "check_point":
        metric_category_abbr = "ckp."
        db_category_abbr = "neo4j."
    elif file_type == "object":
        metric_category_abbr = "ids."
        db_category_abbr = "neo4j."
    elif file_type == "network":
        metric_category_abbr = "net."
        db_category_abbr = "neo4j."
    elif file_type == "server":
        metric_category_abbr = "srv."
        db_category_abbr = "neo4j."
    elif file_type == "log_rotation":
        metric_category_abbr = "log."
        db_category_abbr = "neo4j."
    elif file_type == "log":
        metric_category_abbr = "log."
        db_category_abbr = "neo4j."
    elif file_type == "jvm_gc":
        metric_category_abbr = "gc."
        db_category_abbr = "neo4j.vm."
    elif file_type == "jvm_memory":
        metric_category_abbr = "mem."
        db_category_abbr = "vm."
    elif file_type == "jvm_thread":
        metric_category_abbr = "thr."
        db_category_abbr = "vm."
    elif file_type == "count":
        metric_category_abbr = "neo4j."
        db_category_abbr = "count."
    else:
        print (" ")
        print ("Existing...get_metric_category_abbr.py... :" + file_type )
        print (" ")
        exit

    return metric_category_abbr, db_category_abbr

