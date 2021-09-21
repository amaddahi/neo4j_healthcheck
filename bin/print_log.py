from bin import globals
import sys

def run(level,msg):

    # TODO: Add results_directory to full path
    error_log_file=open(globals.error_log  , 'a') 
    error_log_file.write(msg + "\n")
    error_log_file.close()


    # TODO: Add results_directory to full path
   # with open(results_file_txt, 'w') as fo:
               #fo.write(df.__repr__())

    #print(msg)
    #print('')

