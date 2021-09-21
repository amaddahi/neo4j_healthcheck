

import warnings
from bin import globals
from bin import print_dataframe
from bin import plot_metric
from bin import run_shell
import time, os, fnmatch
import pandas as pd
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


def run():


    warnings.simplefilter(action='ignore', category=FutureWarning)

    globals.working_directory = os.getcwd()
    globals.metrics_directory = globals.admin_report_directory + "/metrics"
    globals.logs_directory = globals.admin_report_directory + "/logs"
    globals.conf_directory = globals.admin_report_directory


    globals.pp = PdfPages('allcharts.pdf')
    plt.savefig(globals.pp, format='pdf')
    plt.title("MY TITLE")

    if not os.path.isdir(globals.results_directory):
        os.makedirs(globals.results_directory)

    if not os.path.isdir('/proc/1/cgroup'):
        docker=True

    if os.path.isdir('logs'):
        if fnmatch.filter(os.listdir('logs'), 'debug.log'):
              logs_directory = os.path.join(globals.working_directory, 'logs')
        else:
              print("")
              print ("Exiting:  Can not find any debug.log files in the logs directory in this folder")
              print("")
              exit(1)

        if os.path.isdir('conf'):
            if fnmatch.filter(os.listdir('conf'), 'neo4j.conf'):
                conf_directory = os.path.join(globals.working_directory, 'conf')
            else:
                print("")
                print ("Exiting:  Can not find any neo4j.conf files in the conf directory in this folder")
                print("")
                exit(1)

def admin_report_check():

    warnings.simplefilter(action='ignore', category=FutureWarning)

    #if globals.logs_directory is not None:
        #run_shell.run("grep 'Operating System' " + globals.logs_directory + "/debug.log | head -1","Host Operating System + Number of cpu cores",1)

    #check_size()

    globals.long_running_query_file = globals.results_directory + "/long_running_queries.log"
    globals.long_running_query_sorted_file = globals.results_directory + "/long_running_queries_sorted.log"

    if globals.logs_directory is not None:
        os.system("cd " + globals.logs_directory + ";" + "ls -1v  " + globals.logs_directory  + "/query.log* | xargs cat > " +  globals.long_running_query_file )
        os.system("grep INFO  " + globals.long_running_query_file + " | sort -k4nr,4  | cut -c1-280  > " + globals.long_running_query_sorted_file)
        os.system("head -1000 " + globals.long_running_query_sorted_file + " | grep INFO | cut -c1-16 > /tmp/q1")
        os.system("head -1000 " + globals.long_running_query_sorted_file + " | grep INFO | cut -c36-40 > /tmp/q2")
        os.system("echo 't,duration'  > /tmp/qqq ")
        os.system("paste -d ',' /tmp/q1 /tmp/q2  >> /tmp/qqq")

        #run_shell.run("head -10 " + globals.long_running_query_sorted_file , "Top 10 Slowest Queries",1)

        #run_shell.run(" grep -i 'Detected VM stop-the-world pause' " +
              #globals.logs_directory + "/debug.log | sort -k10 -r | head -10 ","Neo4j Top 10 Longest GC pauses(3.4+)",1)

        #run_shell.run(" grep -n -i blocked " + globals.logs_directory +
              #"/debug.log | sort -r -n -k 11 | head -10","Neo4j Top 10 Longest GC pauses (< 3.4) ",1)

        #run_shell.run("grep -v '^#\' " + globals.conf_directory + "/neo4j.conf | sed -e  '/^$/d' | sort ","Non-default Neo4j.conf settings",1)

    #get_config_recommendation()
    get_and_print_debug_errors()
    print_top_long_running_queries()
    plot_long_running_queries("LongRunningQueries")
    print_dataframe.run2(0,"\n")
    print_dataframe.run2(0,"###################################################################")
    return

def plot_long_running_queries(metric_category):

    warnings.simplefilter(action='ignore', category=FutureWarning)

    #filenames = get_filenames.run(metric_category)

    #
    # Read the merged file with epoch timestamp into a dataframe
    #
    df = pd.read_csv("/tmp/qqq")

    #if globals.debug:
        #df.to_csv(metric_category + "_0.csv")

    #
    # drop any rows with null values - indicating mismatched enddates
    #
    #df = df.dropna()

    plot_metric.run2(df,"query")
    os.system("rm /tmp/q1; rm /tmp/q2 ")
    return df


def get_and_print_debug_errors():

        warnings.simplefilter(action='ignore', category=FutureWarning)

        error_keep_list=["Deprecated index providers","Caused by","o.n.c.c.c.RaftMachine", "o.n.c.c.c.s.RaftState","o.n.c.c.c.s.RaftLogShipper","o.n.c.c.c.m.RaftMembershipChanger","o.n.c.c.c.m.RaftMembershipManager","o.n.c.m.RaftOutbound","o.n.k.i.c.MonitorGc","o.n.c.d.HazelcastCoreTopologyService","o.n.c.c.c.m.MembershipWaiterLifecycle","o.n.k.AvailabilityGuard","o.n.i.p.PageCache","o.n.c.i.ClusterBinder","o.n.k.i.DatabaseHealth","o.n.c.c.s.s.CoreStateDownloader","o.n.c.c.IdentityModule","GetOperation","ERROR","WARN","o.n.k.i.f.GraphDatabaseFacadeFactory"]


        print_dataframe.run2(0,"###################################################################")
        print_dataframe.run2(0, " ")
        print_dataframe.run2(0,"Interesting Messages in Debug.log")
        print_dataframe.run2(0, "\n")
        print_dataframe.run2(0, "\n")

        debug_file = globals.logs_directory + "/debug.log"
        f = open(debug_file, "r")
        lines = f.readlines()
        f.close()

        debug_filtered_file = globals.logs_directory + "/filtered_debug.log"
        f = open(debug_filtered_file, "w")

        for line in lines:
            for error in error_keep_list:
                if (error in line) and ('Failed to load') not in line:
                     f.write(line)
        f.close()

        f = open(debug_filtered_file, "r")
        lines = f.readlines()
        f.close()

        line_count=len(lines)
        i=0
        for line in lines:
              i=i+1
              if i >= (line_count - 100 ):
                   #print(line , end = '')
                   print_dataframe.run2(0, "----> "+ line )

        print_dataframe.run2(0, "\n")
        print_dataframe.run2(0, "\n")


def print_top_long_running_queries():

        warnings.simplefilter(action='ignore', category=FutureWarning)

        print_dataframe.run2(0,"###################################################################")
        print_dataframe.run2(0, " ")
        print_dataframe.run2(0,"Top 10 Slowest Queries")
        print_dataframe.run2(0, " \n ")
        print_dataframe.run2(0, " \n ")
        
        f = open(globals.long_running_query_sorted_file, "r")
        lines = f.readlines()
        f.close()

        #line_count=len(lines)
        i=0
        for line in lines:
              i=i+1
              if i <= 10:
                 #print(line , end = '')
                 print_dataframe.run2(0, "----> "+ line )
        print_dataframe.run2(0, " \n ")
