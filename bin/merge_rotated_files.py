
from bin import globals
import os
from bin import get_filenames

def run(metrics_category,filenames):

    if globals.debug:
         print ("  ")
         print ("Inside Merged_rotated_files >>> Concatenating multiple rotated historical files (i.e metrics.csv & metrics.csv.1, etc) by appending them into a single file called metrics.csv.rotated")
         print ("  ")

    #filenames = get_filenames.run(metrics_category)

    for file in filenames:

       cmd = 'cd '  + globals.metrics_directory + ';ls -r ' + file[0] + '*  | xargs cat > ' + file[0] + '.merged_rotated_files' + ' 2> /dev/null'
       os.system(cmd)

