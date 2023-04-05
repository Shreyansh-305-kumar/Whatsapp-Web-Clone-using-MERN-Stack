# Client Side

# Importing necessary modules
import time
import socket
import sys
from random import randint

# Defining the localhost and port number
LOCALHOST = sys.argv[1]
PORT = sys.argv[2]

# Converting port number to integer
PORT = int(PORT)

# Creating a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((LOCALHOST, PORT))

# Setting the socket to non-blocking mode
client.setblocking(0)

# Waiting for the server to send a connection message
while True:
    try:
        ans = client.recv(1024)
        ans = ans.decode()
        print("Client connected to Server")
        break
    except:
        print("Another client connected. Please wait...")
        time.sleep(5)

print("-------------------------------------")
# Running an infinite loop to send and receive messages with the server
while True:
    # Getting input from the user
    inp = input("Enter arithmetic operation: ")
    # Sending input to the server
    client.send(inp.encode())

    # Receiving output from the server
    while True:
        try:
            answer = client.recv(1024)
            break
        except:
            arr = 3
            
    # Displaying the result to the user
    print("Result: " + answer.decode())
    
    # Asking the user if they want to continue
    print("Do you wish to continue? Y/N")
    inp = input(" : ")
    if inp == "n" or inp == "N":
        # Sending a signal to the server to close the connection
        client.send(inp.encode())
        break

# Closing the connection
print("Connection closed")
print("-------------------------------------")
client.close()
