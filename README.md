# Remote Command Execution using Python Sockets

This project demonstrates a simple client-server model where the server sends commands to the client, which executes them on its machine and returns the output back to the server. This can be used for remote command execution, where the server remotely controls the client machine.

## Features
- **Remote Command Execution**: The server sends shell commands to the client, which are executed on the client machine. The output is then sent back to the server.
- **Directory Navigation**: The client can change directories on its system using the `cd` command sent by the server.
- **Real-time Interaction**: The server continuously interacts with the client, executing commands until the server sends a `quit` command.

## Prerequisites
- Python 3.x installed on both the client and server machines.
- Both machines must be on the same network, or the server's IP should be accessible by the client.

## Setup

### Server Setup

1. **Create a Python environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install required modules** (if not already installed):
   ```bash
   pip install socket
   ```

3. **Run the server**:
   ```bash
   python server.py
   ```

   The server will start listening on the specified port (default: `7777`) for incoming client connections.

### Client Setup

1. **Create a Python environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install required modules** (if not already installed):
   ```bash
   pip install socket
   ```

3. **Run the client**:
   ```bash
   python client.py
   ```

   The client will attempt to connect to the server's IP address on the specified port.

## Usage

1. **Start the server** by running `server.py` on the server machine.
2. **Start the client** by running `client.py` on the client machine. The client will connect to the server and wait for commands.
3. On the server, type shell commands to be executed on the client machine. The output of the commands will be displayed on the server.
4. To stop the interaction, type `quit` in the server's command input. This will close the connection.

## Example Commands
- `ls` (Linux/Mac) or `dir` (Windows): List the contents of the current directory on the client machine.
- `cd <directory>`: Change the current directory on the client machine.
- `quit`: Close the connection between the server and client.

## Limitations

- **No Interactive Commands**: The program does not support interactive commands like `vim`, `nano`, or `top`. These commands require a terminal interface for interaction, which this program does not provide. If you try to run such commands, the client will hang, waiting for input that cannot be provided through this setup.
  
- **Command Output Size**: The program can handle only a limited amount of command output at once (up to 1024 bytes). Commands that produce output larger than this will be truncated, and not all output will be returned to the server.

- **Security**: This implementation does not include any encryption or authentication mechanisms. Any data sent between the client and server is transmitted in plain text, which makes it vulnerable to interception. This program should not be used in an unsecured or untrusted network environment.

- **Network Dependency**: The client and server must be able to communicate over the network. If there are issues such as firewall blocks or network restrictions, the connection may fail.

## Notes
- This example assumes both the server and client are on the same network or have a direct connection. If they are on different networks, port forwarding may be required.
- Ensure that the server IP address in `client.py` is set correctly to the server's actual IP address.

## Disclaimer
This script is for educational purposes only. Misuse of this script could lead to unauthorized access to a computer system. The author is not responsible for any misuse.
