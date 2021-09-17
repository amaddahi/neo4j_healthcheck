from bin import globals

def run_benchmark():
    for i in range(1,20):
        cypher="CREATE (EdH:Person {name:'Joe_" + str(i) + "' , born:1950});"
        #print (cypher)
        db(cypher,"my transaction")
