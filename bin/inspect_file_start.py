from bin import globals
from bin import get_filenames
import datetime
import os

#
# Different metric files can have different start/end times.  This module will align their start/end times
#
def run(metrics_category):
    filenames = get_filenames.run(metrics_category)

    final_endtime=1735689600
    final_starttime=0

    for file in filenames:
        metrics_file = globals.metrics_directory + "/" + file[0] + '.merged_rotated_files'
        f = open(metrics_file, "r")
        lines = f.readlines()
        f.close()

        max_timestamp=0
        min_timestamp=1735689600 # (1/1/2025)

        for line in lines:
            #if ("t," not in line) or ("c" not in line):
            if ("t," not in line):
                cur_timestamp=int(line.split(',')[0])
                if cur_timestamp < min_timestamp:
                    min_timestamp=cur_timestamp
                if cur_timestamp > max_timestamp:
                    max_timestamp=cur_timestamp
                #break

        if max_timestamp < final_endtime:
            final_endtime = max_timestamp
        if min_timestamp > final_starttime:
            final_starttime = min_timestamp

        final_starttime_tz= datetime.datetime.fromtimestamp(final_starttime)
        final_endtime_tz= datetime.datetime.fromtimestamp(final_endtime)

        #print(">>>>>>>>>>>: " + str(final_starttime_tz)  + "    " + str(final_endtime_tz)  + "  " + metrics_file )
        #if (final_starttime >= final_endtime):
               #print("---> detected endtime < starttime: ")

    #print("final_starttime: "  + str(final_starttime)  + "final_endtime: "  + str(final_endtime) )
    #print(" ")

    for file in filenames:
        metrics_file = globals.metrics_directory + "/" + file[0] + '.merged_rotated_files'
        f = open(metrics_file, "r")
        lines = f.readlines()
        f.close()

        metrics_file = globals.metrics_directory + "/" + file[0] + ".final"
        f = open(metrics_file, "w")
        f.write("t,value\n")
        i = 0
        for line in lines:
                i += 1
                if "t," not in line:
                     cur_timestamp=int(line.split(',')[0])
                     #print(line)
                     #print(str(cur_timestamp))
                     #print(str(final_starttime))
                     #print(str(final_endtime))
                     #print(' ')
                     #if (cur_timestamp > final_endtime) or (cur_timestamp < final_starttime):
                if ( final_starttime  < cur_timestamp < final_endtime):
                     f.write(line)
                     #print("--> " + line)
                #if (i == 4):
                     #exit()
        f.close()

        cmd = 'cd ' + globals.metrics_directory + ';rm '  + file[0] + '.merged_rotated_files  2> /dev/null'
        os.system(cmd)


