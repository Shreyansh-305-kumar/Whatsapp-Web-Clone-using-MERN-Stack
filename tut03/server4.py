import sys
import socket
import selectors
import types

# Create a selector object
sel = selectors.DefaultSelector()

# Define a function to handle new client connections
def accept_wrapper(sock):
    # Accept a new client connection
    conn, addr = sock.accept()  
    print("Connected client :", addr[1])
    
    # Send a flag to the client indicating that the connection was successful
    flag = "1"
    conn.send(flag.encode())
    
    # Set the connection to non-blocking mode
    conn.setblocking(False)
    
    # Create a namespace object to store data related to this connection
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    
    # Register the connection with the selector object
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

# Define a function to handle client connections
def service_connection(key, mask):
    # Get the socket object from the key
    sock = key.fileobj
    
    # Get the data object associated with this connection
    data = key.data
    
    # Handle read events
    if mask & selectors.EVENT_READ:
        # Receive data from the client
        recv_data = sock.recv(1024)
        
        # If data was received, append it to the output buffer for this connection
        if recv_data:
            data.outb += recv_data
            print("Received: ",recv_data," from client socket",data.addr[1])
        else:
            # If no data was received, the connection has been closed
            print("Connection closed from client", data.addr[1])
            sel.unregister(sock)
            sock.close()
    
    # Handle write events
    if mask & selectors.EVENT_WRITE:
        # If there is data in the output buffer for this connection, send it back to the client
        if data.outb:
            print("Sending reply: ",data.addr[1]) #Echoing data back to client
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

# Get the server address and port from the command line arguments
host = sys.argv[1]
port = sys.argv[2]
port = int(port)

# Set up the server socket
try:
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host, port))
    lsock.listen()
    print("server address",host)
    print("PORT number",port)
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)
    print("Server started....Give keyboard interupt to stop :)")
    print("-------------------------------------")
except:
    print("Address already in use......RESTART")
    exit()

# Main loop to handle incoming connections
try:
    while True:
        # Wait for events to occur
        events = sel.select(timeout=None)
        
        # Handle each event that occurred
        for key, mask in events:
            if key.data is None:
                # If there is no data associated with the key, a new client connection is being made
                accept_wrapper(key.fileobj)
            else:
                # If there is data associated with the key, a client connection is being serviced
                service_connection(key, mask)

# Handle a keyboard interrupt to shut down the server
except KeyboardInterrupt:
    print("Caught Keyboard Interrput. Server Closed.")

# Close the selector object
finally:
    sel.close()
