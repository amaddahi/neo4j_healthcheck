
import os

def run(cleanup_filename):
       if os.path.exists(cleanup_filename):
            os.system("rm " + cleanup_filename)
