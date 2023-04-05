# server side

# Import socket module
import socket
import sys
from random import randint

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server address and port number from command line arguments
LOCALHOST = sys.argv[1]
PORT = sys.argv[2]
PORT = int(PORT)

# Check if the specified port is available or not
destination = (LOCALHOST, PORT)
result = server.connect_ex(destination)
if result == 0:
    print("Port is not available")
    print("Restart...........")
    exit()
else:
    print("Port is available")

# Bind the socket to the specified address and port number
print("Server address", LOCALHOST)
print("PORT number", PORT)
server.bind((LOCALHOST, PORT))

# Start the server and wait for incoming connections
print("Server started....Give keyboard interrupt to stop :)")
print("-------------------------------------")

while True:
    # Wait for incoming connections
    server.listen(1)
    
    # Accept the connection and get client address and connection object
    clientConnection, clientAddress = server.accept()
    print("Connected client :", clientAddress)
    
    # Send initial flag to client indicating successful connection
    flag = "1"
    clientConnection.send(flag.encode())
    
    # Running infinite loop to receive and process client requests
    while True:
        # Receive client request
        msg = ''
        data = clientConnection.recv(1024)
        msg = data.decode()
        
        # Display received request from client
        print("Received Request ", clientAddress[1] ,"is : " , msg)
        
        # If client sends 'n' or 'N', close the connection with client
        if msg == "n" or msg == "N":
            print("Closing client : ",clientAddress)
            break
        
        # Evaluate client request and send the result back to client
        output = ''
        try:
            res = eval(msg)
            print("Send the result to client : ", clientAddress[1])
            output = str(res)
        except(NameError, SyntaxError):
            print("Wrong expression given to server.....")
            output = str("wrong expression.... resend your query")
            
        clientConnection.send(output.encode())

# Close the connection with client and stop the server
print("Connection closed")
print("-------------------------------------")
clientConnection.close()
