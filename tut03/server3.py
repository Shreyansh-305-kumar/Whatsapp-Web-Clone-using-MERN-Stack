import sys
import socket
import selectors
import types
from operator import pow, truediv, mul, add, sub 

# Create a selector object for monitoring I/O events
sel = selectors.DefaultSelector()

# Function to handle accepting new connections
def accept_wrapper(sock):
    # Accept the connection and get client address
    conn, addr = sock.accept()  
    print("Connected client :", addr[1])
    
    # Send a flag to the client indicating successful connection
    flag = "1"
    conn.send(flag.encode())
    
    # Set the connection to non-blocking and create a data object to store connection info
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb="", outb="")
    
    # Register the connection with the selector object
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    
# Function to handle serving existing connections
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    
    # If the socket is ready to read, receive data from the client
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        print("Received data from client socket",data.addr[1])
        
        # If data was received, process the client request
        if recv_data:
            msg = str(recv_data.decode())
            output = ""
            
            # Try to evaluate the client request
            try:
                res = eval(msg)
                print("Sending reply : ", res )
                output = str(res)
                
            # If the client request is invalid, send an error message
            except(NameError, SyntaxError):
                print("Wrong expression given to server.....")
                output = str("wrong expression.... resend your query")
            
            # Send the response back to the client
            sock.sendall(str(output).encode())
        
        # If no data was received, the connection was closed by the client
        else:
            print("Connection closed from client", data.addr[1])
            sel.unregister(sock)
            sock.close()

# Get server host and port from command line arguments
host = sys.argv[1]
port = sys.argv[2]
port = int(port)
    
# Attempt to bind to the given address and port
try:
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host, port))
    lsock.listen()
    print("server address",host)
    print("PORT number",port)
    
    # Set the server socket to non-blocking and register with the selector object
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)
    print("Server started....Give keyboard interupt to stop :)")
    print("-------------------------------------")
    
# If the address is already in use, print an error message and exit
except:
    print("Address already in use......RESTART")
    exit()

# Wait for connections and process requests until interrupted by keyboard
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    # If keyboard interrupt is detected, close the server
        print("Caught Keyboard Interrput. Server Closed.")
finally:
        sel.close()
