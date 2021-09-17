from bin import globals
import os
import time
import fnmatch

def initialize():

    print(' ')
    if globals.checkdb:
        if 'DB_USER' in os.environ:
            globals.user = os.environ.get("DB_USER")
        else:
            print_log('WARNING: cypher-shell username has not been exported.')

        if 'DB_PWD' in os.environ:
            globals.db_pwd = os.environ.get("DB_PWD")
        else:
            print_log('WARNING: cypher-shell pwd has not been exported.')

    globals.working_directory = os.getcwd()
    globals.neo4j_home = os.environ.get('NEO4J_HOME')
    globals.metrics_directory = os.environ.get('METRICS_DIR') #EXPORT METRICS_DIR
    globals.logs_directory = os.environ.get('LOGS_DIR')  # EXPORT LOGS_DIR
    globals.conf_directory = os.environ.get('CONF_DIR')  # EXPORT CONF_DIR

    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H%M', t)

    globals.results_directory=globals.working_directory + "/results/" + globals.customer + "/" + globals.customer + "-healthcheck_results-" + timestamp
    globals.results_file_txt=globals.results_directory + "/" + globals.customer + "_results.txt"
    globals.results_file_pdf=globals.results_directory + "/" + globals.customer + "_results.pdf"
    globals.combined_results_plot_pdf=globals.results_directory + "/" + globals.customer + "_results_w_plots.pdf"


    if not os.path.isdir(globals.results_directory):
        os.makedirs(globals.results_directory)

    if not os.path.isdir('/proc/1/cgroup'):
        docker=True

    #if docker:

    if globals.neo4j_home:
        dbms_metrics_dir = os.path.join(globals.neo4j_home, 'metrics')
        dbms_logs_dir = os.path.join(globals.neo4j_home, 'logs')
        dbms_conf_dir = os.path.join(globals.neo4j_home, 'conf')
        dbms_bin_dir = os.path.join(globals.neo4j_home, 'bin')
        dbms_data_dir = os.path.join(globals.neo4j_home, 'data')

    if os.path.isdir('metrics'):
        if fnmatch.filter(os.listdir('metrics'), '*.csv'):
            globals.metrics_directory = os.path.join(globals.working_directory, 'metrics')
        else:
            print_log("Exiting:  Can not find any CSV metrics files in the metrics directory in this folder")
            exit(1)
    elif globals.neo4j_home:
        if os.path.isdir(dbms_metrics_dir):
                if fnmatch.filter(os.listdir(dbms_metrics_dir), '*.csv'):
                    globals.metrics_directory = dbms_metrics_dir
                else:
                    print_log("Exiting:  Can not find any CSV metrics files in " + globals.metrics_directory )
                    exit(1)
    else:
        if os.getenv("NEO4J_HOME") is None:
              #print_log("NOTE         :  NEO4J_HOME has not been set!   ")
              no_neo4j_home="has not been defined!"
        else:
              no_neo4j_home=""
        print_log("""Exiting      :  Can not find a metrics directory: 

                1) in the current directory 
                2) nor under $NEO4J_HOME (""" + no_neo4j_home + """)
                3) nor any admin reports have been provided 
                """)
        exit(3)


    if globals.checkdb:

        if os.path.isdir('logs'):
            if fnmatch.filter(os.listdir('logs'), 'debug.log'):
                globals.log_directory = os.path.join(globals.g_directory, 'logs')
            else:
                print_log("Exiting:  Can not find any debug.log files in the logs directory in this folder")
                exit(1)
        elif globals.neo4j_home:
            if os.path.isdir(dbms_logs_dir):
                    if fnmatch.filter(os.listdir(dbms_logs_dir), 'debug.log'):
                        globals.log_directory = dbms_logs_dir
                    else:
                        print_log("Exiting:  Can not find any debug.log files in " + globals.log_directory )
                        exit(1)
        else:
            print_log("Exiting      :  Can not find a logs directory in this directory nor under $NEO4J_HOME")
            if os.getenv("NEO4J_HOME") is None:
                  print_log("NOTE         :  NEO4J_HOME has not been set!   ")
            exit(4)

        if os.path.isdir('conf'):
            if fnmatch.filter(os.listdir('conf'), 'neo4j.conf'):
                globals.conf_directory = os.path.join(globals.g_directory, 'conf')
            else:
                print_log("Exiting:  Can not find any neo4j.conf files in the conf directory in this folder")
                exit(1)
        elif globals.neo4j_home:
            if os.path.isdir(dbms_conf_dir):
                    if fnmatch.filter(os.listdir(dbms_conf_dir), 'neo4j.conf'):
                        globals.conf_directory = dbms_conf_dir
                    else:
                        print_log("Exiting:  Can not find any neo4j.conf files in " + globals.conf_directory )
                        exit(1)
        else:
            print_log("Exiting      :  Can not find a conf directory in this directory nor under $NEO4J_HOME")
            if os.getenv("NEO4J_HOME") is None:
                  print_log("NOTE         :  NEO4J_HOME has not been set!   ")
            exit(5)


        if os.path.isdir('bin'):
            if fnmatch.filter(os.listdir('bin'), 'neo4j'):
                globals.bin_directory = os.path.join(globals.g_directory, 'bin')
            else:
                print_log("Exiting:  Can not find any neo4j file in the bin directory in this folder")
                exit(1)
        elif globals.neo4j_home:
            if os.path.isdir(dbms_bin_dir):
                    if fnmatch.filter(os.listdir(dbms_bin_dir), 'neo4j'):
                        globals.bin_directory = dbms_bin_dir
                    else:
                        print_log("Exiting:  Can not find any neo4j files in " + globals.bin_directory )
                        exit(1)
        else:
            print_log("Exiting      :  Can not find a bin directory in this directory nor under $NEO4J_HOME")
            if os.getenv("NEO4J_HOME") is None:
                  print_log("NOTE         :  NEO4J_HOME has not been set!   ")
            exit(6)

        if os.path.isdir('data'):
            if fnmatch.filter(os.listdir('data'), 'databases'):
                globals.data_directory = os.path.join(globals.g_directory, 'data')
            else:
                print_log("Exiting:  Can not find data directory in this folder")
                exit(1)
        elif globals.neo4j_home:
            if os.path.isdir(dbms_data_dir):
                    if fnmatch.filter(os.listdir(dbms_data_dir), 'databases'):
                        globals.data_directory = dbms_data_dir
                    else:
                        print_log("Exiting:  Can not find any databases directory  in " + globals.data_directory )
                        exit(1)
        else:
            print_log("Exiting      :  Can not find a bin directory in this directory nor under $NEO4J_HOME")
            if os.getenv("NEO4J_HOME") is None:
                  print_log("NOTE         :  NEO4J_HOME has not been set!   ")
            exit(7)



def print_log(msg):
            print("")
            print("")
            print(msg) 
            print("")

