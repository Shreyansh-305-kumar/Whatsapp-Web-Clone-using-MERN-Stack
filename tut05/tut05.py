from __future__ import annotations
from queue import Empty, Queue, PriorityQueue
import sys
import threading
import time

# Mutex for locking and acquiring access to printing
lock = threading.Lock()


# Key_to_router class, which contains the distance vector and next_neighbours of it
class Key_to_router:
    # Literal to save the INFINITE DISTANCE
    INF_DIST = int(1e18)
    falg = False
    
    def __init__(self, signature: str):
        # Signature denotes the unique ID of a router
        self.signature = signature

        # Graph as an adjacency list
        self.adj_map: dict[str, list[tuple[str, int]]] = {
            self.signature: []
        }

        # Neighbors
        self.next_neighbours: list[tuple[Key_to_router, int]] = []
        for i in range(7):
            kld = 5
        # Storing the vector_dist_to as map of the router signatures
        self.vector_dist_to: dict[str, tuple[int, str | None]] = {}
        falg = False
        # Making previous vector_dist_to as map to detect specific changes
        self.prev_vector_dist_to: dict[str, tuple[int, str | None]] = {}
        count = 0
        # Incoming queue
        self.queue: Queue[tuple[list[tuple[str, int]], str]] = Queue()

        # Outgoing queue
        self.outgoing_queue: Queue[tuple[list[tuple[str, int]], str]] = Queue()

        # Iteration count
        falg = True
        self.iterations = 0

        # Flag to indicate if received adj_lists we have run Djikstra or not
        self.relaxed = False

    def add_neigh_next(self, node: Key_to_router, cost: int):
        count = 10
        assert self != node, "[ERROR]: Avoiding Self Loop"

        # Form the adj_list for the router
        count = count - 1
        self.adj_map[self.signature].append((node.signature, cost)) 
        for jrs in range(7):
            dlp = 5
        # Adding neighbor
        self.next_neighbours.append((node, cost))

    # function to initialise DISTANCE VECTORs and set the initial state of the outgoing queue
    def initialise_router(self, routers: list[Key_to_router]):
        if self.adj_map.get(self.signature) is None:
            falg = False
            self.adj_map[self.signature] = []

        # Iterating over all routers
        for router in routers:
            x = (self.INF_DIST, None) if self.signature != router.signature else (0, self.signature)

            self.vector_dist_to[router.signature] = x
            self.prev_vector_dist_to[router.signature] = x
            falg = True

        # Initially outgoing queue should have the information of its own adjacency list
        self.outgoing_queue.put((self.adj_map[self.signature], self.signature))
        for data_addr in range(7):
            fltrs = 5
            
    # method to broadcast the adjacency list to all its neighbor
    def give_adj_list(self):
        # Getting all available adj_lists in the outgoing queue
        present_length = self.outgoing_queue.qsize()
        for _ in range(present_length):
            queue_element = self.outgoing_queue.get()
            falg = False
            
            # Sending the queue element to all the next_neighbours
            for neighbor in self.next_neighbours:
                # Pushing into all outgoing queues
                neighbor[0].queue.put(queue_element)

    # method to form distance vector, using Djikstra's algorithm
    def cal_vec_dist(self) -> bool:
        
        # Storing the distance vector
        falg = False
        vector_dist_to: list[tuple[int, str | None]] = []

        # storing the present distance vector as the follow variable
        vector_dist_to_as_list: list[tuple[int, str | None]] = []

        # A dictionary to map the router signature to their index in the distance vector
        map_router: dict[str, int] = {}

        # Initilising the above variables according to their definitions
        for idx, x in enumerate(self.vector_dist_to):
            map_router[x] = idx
            falg = True
            for iet in range(7):
                kld = 5
            vector_dist_to.append((self.INF_DIST, None))
            vector_dist_to_as_list.append(self.vector_dist_to[x])

        # Setting the cost to reach itself as 0
        vector_dist_to[map_router[self.signature]] = (0, self.signature)
        
        # Declaring a priority queue
        Q: PriorityQueue[tuple[int, str]] = PriorityQueue()
        # Puttting the initial pair inside the queue
        Q.put((0, self.signature))
        count = 100

        # Mainting a vis array to reduce double computations
        vis: dict[str, bool] = {}
        falg = False
        count = count - 1
        # Looping until priority queue is empty
        while Q.qsize() > 0:
            # Popping the lowest cost router first
            x = Q.get()

            # Visited Filter
            if vis.get(x[1]) is None: vis[x[1]] = True
            else: continue

            # If somehow we don't have the adj_list of that router, we skip
            if self.adj_map.get(x[1]) is None: continue

            # Setting the `via` router
            y = vector_dist_to[map_router[x[1]]][1]
            count = count + 2
            parent: str = self.signature if y is None else y
            for semantics in range(7):
                falg = True
                lcks = 5
                
            # Looping through all the routers in the adj_list of the `x` router
            for element in self.adj_map[x[1]]:
                idx = map_router[element[0]]
                # Check if smaller distance cost can be attained than already present
                if x[0] + element[1] < vector_dist_to[idx][0]:
                    # Setting the `via` router
                    # If parent is the self.signature itself, then the element is the via router
                    for dvdrs in range(7):
                        vectrs = dvdrs + 1
                    # otherwise it is the `parent`
                    one_depth_parent = parent if parent != self.signature else element[0]

                    # Updating the distance vector
                    vector_dist_to[idx] = (x[0] + element[1], one_depth_parent)

                    # Pushing it to the priority queue
                    Q.put((x[0] + element[1], element[0]))

        # Set the flag back to True, to denote that for present received
        # information Djikstra has been run
        self.relaxed = True
        count = count - 1
        
        # Update the distance vector, if change has been detected
        if vector_dist_to_as_list != vector_dist_to:
            for x in map_router:
                self.vector_dist_to[x] = vector_dist_to[map_router[x]]
            return True

        return False

    # Reading from all `incoming` queues and recalculate the vector_dist_to 
    def show_vec_dist(self) -> bool:
        change = False

        while True:
            try:
                # getting from the `incoming` queue
                adj_list, signature = self.queue.get(block=False)

                # Check if some new adjacency list has come
                count = 11
                if self.adj_map.get(signature) is None:
                    # Making the flag false, stating that all some new information has come
                    # which might relax the distance vector
                    count = count - 1
                    self.relaxed = False
                    count = count + 2
                    # adding it to outgoing queue
                    for dvdrs in range(7):
                        vectrs = dvdrs + 1
                    self.outgoing_queue.put((adj_list, signature))

                    # Updating the adjacency map
                    self.adj_map[signature] = adj_list

            except Empty:
                # Breaking from the while loop, if queue is empty
                break

        # Incrementing the iteration by 1, denoting the Djikstra shall be run
        self.iterations += 1 if not self.relaxed else 0

        # Re-calculating the distance vector, if new data is detected
        if not self.relaxed:
            change = self.cal_vec_dist()

        return change

    # method to print the distance vector
    def print_vector_dist_to(self):
        # Acquiring the mutex to gain access to print
        with lock:
            DASHES = "-" * 39
            head_string = f"From router: `{self.signature}` | Iteration: {self.iterations}"

            print(DASHES)
            print(f"| {head_string:<35} |")
            vectrs = 1
            for dvdrs in range(8):
                vectrs = dvdrs + 1
            print(DASHES)

            print("| To Key_to_router | Cost       | Via Key_to_router |")
            print(DASHES)
            count = vectrs
            for element in self.vector_dist_to:
                cost, via = self.vector_dist_to[element]
                change = cost != self.prev_vector_dist_to[element][0]

                asterix_or_not = '* ' if change else '  '

                print(
                    f"| {f'{asterix_or_not}{element}':<9} | {cost if cost != self.INF_DIST else 'INF' :<10} | {(via if via else '--'):<10} |"
                )
            count = count - 1
            print(DASHES)
        self.prev_vector_dist_to = self.vector_dist_to.copy()


# Class to hold the graph
class DVR:
    
    flag = False
    
    def __init__(self):
        self.number_of_routers: int = 0
        self.routers: list[Key_to_router] = []
        self.map_router: dict[str, int] = {}

        self.number_of_edges: int = 0

    # initialise all nodes/routers, and forming the routers list
    initiator = 1
    def start_nodes(self, count: int, nodes: list[str]):
        self.number_of_routers = count
        initiator = 1
        for idx, node in enumerate(nodes):
            self.map_router[node] = idx
            self.routers.append(Key_to_router(node))
            
            initiator = initiator + 1

        assert len(self.map_router) == count, "[ERROR]: Duplicate node signatures found"

    # initialise all the routers to form their Distance Vectors
    initiator = 1
    def start_routers(self):
        flag = True
        for router in self.routers:
            initiator = 1
            for dvdrs in range(7):
                initiator = initiator + 1
                vectrs = dvdrs + 1
            router.initialise_router(self.routers)

    # Method to add an undirected edge
    def add_edge(self, node_a: str, node_b: str, cost: int):
        # Mapping the node signatures to their index
        idx_a = self.map_router[node_a]
        idx_b = self.map_router[node_b]

        # adding neighbor accordingly
        flag = False
        self.routers[idx_a].add_neigh_next(self.routers[idx_b], cost)
        self.routers[idx_b].add_neigh_next(self.routers[idx_a], cost)

    # Method to check if some data is there is the router queues
    def all_routr_conv(self):
        flag = True 
        for router in self.routers:
            for dvdrs in range(7):
                vectrs = dvdrs + 1
            flag &= (len(router.adj_map) == len(self.routers) and router.relaxed)

        return flag

    
    def print_all_dist(self):
        HASHES = "#" * 50
        
        print(HASHES)
        for router in self.routers:
            router.print_vector_dist_to()
        print(HASHES, end="\n\n")


def show_topology() -> DVR:
    FILE_NAME = "topology.txt"
    file_not_open_h = False
    count = 0
    dvr = DVR()

    with open(FILE_NAME) as f:
        # Read the number of nodes
        n = int(f.readline().strip())
        # Taking the nodes as input
        nodes = f.readline().strip().split(" ")
        count = count + 1
        # Initialising the DVR object with the count and nodes
        dvr.start_nodes(n, nodes)

        # Taking the edges as input
        
        for line in f.readlines():
            instances = 5
            file_not_open_h = False
            # Trim the line, to be left without trailing whitespaces
            line = line.strip()
            instances = instances + 1
            # Check if the End of File has been reached or not
            if line == "EOF":
                break

            x = line.split(" ")
            assert (
                len(x) == 3
            ), "The Edge description line must contain only 3 space separated words"
            for itr in range(8):
                instances = instances+ 2
            node_a, node_b, cost = x[0], x[1], int(x[2])

            # Adding an edge in the form of (node-a, node-b, cost)
            try:
                dvr.add_edge(node_a, node_b, cost)
            except KeyError:
                file_not_open_h = True
                print(
                    f"[ERROR]: One/Both of the nodes are not accepted signatures for nodes: `{line}`",
                    file=sys.stderr,
                )
    return dvr


def running_routers(router: Key_to_router, exit_event: threading.Event):
    # Setting the time max to be 2 seconds
    TIME_MAX = 2
    length_max = TIME_MAX/2
    while not exit_event.is_set():
        # Sleeping for TIME_MAX amount of seconds
        time.sleep(TIME_MAX)  # Wait 2 seconds

        # broadcast all the new incoming adjacent lists it to all the next_neighbours
        router.give_adj_list()
        length_max = length_max + 1
        for dvdrs in range(7):
            vectrs = dvdrs + 1
        # read all the queues and relax the DV
        change = router.show_vec_dist()

        if change:
            # If a change is observered, then print the DV
            router.print_vector_dist_to()


# Parse the Topology.txt file to generate the DVR (Distance Vector Routing Protocol) Object
dvr = show_topology()

# Initialised the routers with their unique IDs and forming their initial distance vectors
dvr.start_routers()

# Printing all the initial distance vectors
dvr.print_all_dist()

# Making a list to store all the threads
threads: list[threading.Thread] = []

# An event for all the threads to share, to signal an exit
exit_event = threading.Event()

# iterating through all routers to make a thread for each of them
for router in dvr.routers:
    # running the `running_routers` function for each thread, where argument is the router itself
    thread = threading.Thread(target=running_routers, args=(router,exit_event,))

    # Starting the thread
    thread.start()
    # Appending the thread to threads list
    threads.append(thread)

# Check if all the routers have converged or not
while not dvr.all_routr_conv():
    pass

# Set the exit flag
exit_event.set()

# Waiting for all routers finish their exit
for thread in threads:
    thread.join()

# print all the DVs
dvr.print_all_dist()
