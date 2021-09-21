from bin import globals
from bin import get_filenames
import time


def run():
    #filenames = get_filenames("server")
    # it appears as of 4.2.x, server files are missing, so we will use 1st bolt csv file for this purpose
    filenames = get_filenames.run("object")
    for file in filenames:
        metrics_file = globals.metrics_directory + "/" + file[0]

    #print (file)
    #print (metrics_file)
    #print (globals.metrics_directory)
    #print (file[0])

    f = open(metrics_file, "r")
    lines = f.readlines()
    f.close()

    print ("###################################################################")
    print (" ")
    print ("Database Restarts: ")
    print (" ")

    timestamp_cur=0
    timestamp_prev=0
    flag_start=False
    i = 1
    for line in lines:
        timestamp_prev=timestamp_cur
        if "t," not in line:
            timestamp_cur=int(line.split(',')[0])

        if flag_start is True:
            restart_timestamp=int(line.split(',')[0])
            converted_restart_timestamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(restart_timestamp))
            print(converted_restart_timestamp)
            flag_start=False
        if "t," in line:
            flag_start=True
        i += 1
        #print(str(timestamp_prev) + "  " + str(timestamp_cur) + "  " + str(timestamp_cur - timestamp_prev))
    metrics_csv_interval=timestamp_cur-timestamp_prev
    return metrics_csv_interval
