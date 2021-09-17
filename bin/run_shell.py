from bin import globals
import subprocess
import sys

def run(shell_in,section_title,report_error):
    file_tmp="/tmp/file.out"
    #print(shell_in)
    shell=shell_in + " > " + file_tmp
    process = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output , error  = process.communicate()
    exit_code = process.returncode

    print ("###################################################################")
    print ("")
    print (section_title)
    print ("")

    if exit_code == 0:
        file = open(file_tmp, 'r')
        print (file.read() )
        file.close()
    else:
        if report_error == 1:
            if '60000' not in shell_in:
                print("ERROR: " + shell_in)
                print(error)
                #raise Exception(shell, output)
                #exit(0)

    print ("")
    #print ("###################################################################")
    #sys.stdout.flush()
