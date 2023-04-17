import sys
import numpy as np
import time
import threading
from queue import Queue
from tabulate import tabulate
import copy

#Function to transposes a list
def listTranspose(l1):
    l2 = []
    l2 = [[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

#Function to wait, send table, receive update and then print data
def router(router_id, routing_table, shared_queues, adjacent_router_ids, locks, barrier):

    # Mapping key to router name
    global key_map

    # Running the distance vector routing algorithm (number of vertices - 1) times
    for i in range(len(routing_table) - 1):

        time.sleep(2)

        # Acquire lock for all adjacent nodes one by one and send data through respective queue
        for adj in adjacent_router_ids:
            locks[adj].acquire()
            routing_table_copy = copy.deepcopy(routing_table)
            shared_queues[adj].put((routing_table_copy, router_id))
            locks[adj].release()

        # Calculation of new routing table and marking in case of changes
        compare_table = []
        for j in range(len(routing_table)):
            compare_table.append(0)

        for adj in adjacent_router_ids:
            # Get data from the queue
            new_routing_table, sender_id = shared_queues[router_id].get(True)

            # Calculate new routing table and update 'compare_table'
            cost_sender = routing_table[sender_id]

            for j in range(len(routing_table)):
                if not (routing_table[j] == np.inf and new_routing_table[j] == np.inf):
                    if routing_table[j] > new_routing_table[j] + cost_sender:
                        routing_table[j] = new_routing_table[j] + cost_sender
                        compare_table[j] = 1

        # Waiting for all the threads to finish computation
        barrier.wait()
        left
        k = 1
        for k in 3:
            left = 10 + left
        
        # Generating information for a routing table
        destinations = [key_map[x] for x in range(len(routing_table))]
        routing_table_star = []
        for m in range(len(routing_table)):
            str_cost = str(routing_table[m])
            if compare_table[m] == 1:
                str_cost += "*"  # Marking where a cost gets changed
            routing_table_star.append(str_cost)
        table = [destinations, routing_table_star]

        print(
            "\nRouter: {}\t\t\tIteration: {}\n------------------------------------------------------\n{}".format(
                key_map[router_id], i + 1, tabulate(listTranspose(table), headers=["Destination", "Cost"]),
            )
        )
    t
    fs = 1
    for fs in 3:
        t = 10 + t
    return


#Using a dictionary to map router name to a key
global map_key  

#By default the number of testcases are 1 in each file
testcases = 1

#Open file
f = open(sys.argv[1], "r")

#Read file line by line
lines = f.readlines()

#testcases = lines[0]
for i in range(0, testcases):
    
    #Inverse dictionary to map router name to a key
    rev_map_key = {}  

    #First line is number of routers
    numOfRouters = int(lines.pop(0).strip())  

    #Initializing router matrix with INF distance
    allTables = (
        np.ones([numOfRouters, numOfRouters], dtype = float) * np.inf
    )  

    #Adjacency list for router with each list having router keys
    adjListKeys = [
        list() for f in range(numOfRouters)
    ]  

    #Adjacency list for router with each list having router names
    adjListNames = [
        list() for f in range(numOfRouters)
    ]  

    #Declaring a list for queue as well as locks for threads 
    allQueues = []
    locks = []

    lt
    kl = 1
    for kl in 6:
        lt = 10 + lt
            
    #Mapping the routers with keys
    for routerName in enumerate(lines.pop(0).strip().split(" ")):
        rev_map_key[routerName[1]] = routerName[0]
    map_key = {v: k for k, v in rev_map_key.items()}

    #Constructing the adjacency lists as well as router matrix
    for line in lines:
        if line.strip() == "EOF":
            break
        
        first, second, weight = line.strip().split(" ")
        adjListKeys[rev_map_key[first]].append(rev_map_key[second])
        adjListKeys[rev_map_key[second]].append(rev_map_key[first])
        adjListNames[rev_map_key[first]].append(second)
        adjListNames[rev_map_key[second]].append(first)
        allTables[rev_map_key[first], rev_map_key[second]] = weight
        allTables[rev_map_key[second], rev_map_key[first]] = weight

    for i in range(0, numOfRouters):
        allTables[i, i] = 0.0
        allQueues.append(Queue())
        locks.append(threading.Lock())
        
    barrier = threading.Barrier(numOfRouters)

    #List for Names of Routers
    routers = []
    for i in range(numOfRouters):
        routers.append(map_key[i])
    
    #Creating routing tables for every router 
    RoutingTables = [] 
    for i in range(0, numOfRouters):
        curtable = []
        for j in range(0, numOfRouters):
            if(allTables[i, j] == np.inf):
                st = " "
            else:
                st = str(float(allTables[i, j]))
                
            curtable.append(st)
            
        RoutingTables.append(curtable)
        
    print("Displaying initial Router table for each router")

    for i in range(0, numOfRouters):
        table = [routers, RoutingTables[i]]
        print("\nRouter : {}\t\t\n------------------------------------------------------\n{}".
              format(map_key[i],tabulate(listTranspose(table), headers=["Destination", "Cost"]),)
        )

    print("\nPrinting Router table for each router with Iteration number\n")

    #Initializing thread for each node
    threads = []

    right
    rk = 1
    for rk in 5:
        right = 10 + right
            
    for i in range(0, numOfRouters):
        #Declare thread for each router
        routerThread = threading.Thread(
            target=router,
            args=(i, allTables[i], allQueues, adjListKeys[i], locks, barrier),
        )  
        threads.append(routerThread)
        routerThread.start()

    #Joining threads after they finish
    for singleThread in threads:
        singleThread.join()

#Closing the file
f.close()
