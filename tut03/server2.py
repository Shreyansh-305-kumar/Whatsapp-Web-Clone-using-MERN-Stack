# import required libraries
import socket as sk
import errno
import sys
from _thread import *
import threading

# Define a class that extends the threading.Thread class to handle client connections
class conn_thread(threading.Thread):
    
    # Constructor that sets the client's address, port number and connection object
    def __init__(self, address, port_conn, conn): 
        threading.Thread.__init__(self) 
        self.address = address 
        self.port_conn = port_conn 
        self.conn = conn
        print("connection from:", str(address), "port:", str(port_conn)) 
        
    # The run() method is called when a new thread is started
    def run(self): 
        # Continuously listen for data from the client
        while True:
            # Receive data from the client and decode it
            data = self.conn.recv(1024).decode()
            # If the data is empty, break the loop
            if not data:
                break
            
            # Print the received data
            print("received over the connection:", str(data))
            
            # Initialize message variable
            msg = "try again"
            
            try:
                # Try to evaluate the received data as a Python expression
                msg = eval(str(data))
            except SyntaxError as err:
                # If the expression has a syntax error, send an error message
                msg="Invalid syntax"
            except NameError as err:
                # If the expression contains an undefined variable, send an error message
                msg="Please write an expression"

            # Send the message back to the client
            self.conn.send(str(msg).encode())
        

# Get the host IP address and port number from the command-line arguments
host_ip =  sys.argv[1]
port = sys.argv[2]
port = int (port)

try: 
    # Create a new socket object
    server2_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    print("Socket created")
except sk.error as err:
    # If socket creation fails, print an error message and exit
    print("Socket creation failed with error: ", str(err))
    sys.exit()

# Check if the specified port number is available
destination = (host_ip, port)
result = server2_socket.connect_ex(destination)
if result == 0:
    print("Port is not available")
    print("Restart...........")
    exit()
else:
    print("Port is available")

try:
    # Bind the socket to the host IP address and port number
    server2_socket.bind((host_ip, port))
    print("Socket started with ip:", str(host_ip), "port:", str(port))
    print("Server started....Give keyboard interrupt to stop :)")
    print("-------------------------------------")
except sk.error as err:
    # If socket binding fails, print an error message and exit
    if err.errno == errno.EADDRINUSE:
        print("Port already in use")
        sys.exit()
    else:
        print("Socket binding failed with error: ", str(err))
        sys.exit()
        
# Create an empty list to hold thread objects
threads = []

while True:
    # Listen for incoming client connections
    server2_socket.listen(5)
    # Accept a new client connection
    (conn, (address, port_conn)) = server2_socket.accept()
    print("Connected client :", address)
    # Send a flag to the client indicating that the connection has been established
    flag = "1"
    conn.send(flag.encode())
    
    print("connection from:", str(address), "port:", str(port_conn)) 
    
    # Create a new thread to handle the client connection
    # start_new_thread(thread_conn, (conn, ))
    newthread = conn_thread(address, port_conn, conn) 
    newthread.start() 
    threads.append(newthread)