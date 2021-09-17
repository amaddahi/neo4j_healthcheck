from bin import globals

def db(cypher,section_title):
       global host_ip
       cypher_shell=bin_directory + "/cypher-shell"
       cmd = " echo ' " + cypher + " ' | " + cypher_shell + " --encryption=false " + \
            " -u " + db_user + " -p " + db_pwd + " --format verbose -a " + host_ip + ":" + str(bolt_port) + " | egrep -v 'row available|rows available' "
            #" -u " + db_user + " -p " + db_pwd + " --format verbose -a " + host_ip + ":" + str(bolt_port) + " | egrep -v 'row available|rows available' "
       #print(cmd)
       run_shell(cmd,section_title,1)
