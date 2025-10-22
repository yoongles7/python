# TCP Server Side

import socket

# Create a server side socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# See how to get IP address dynamically
print(socket.gethostname()) # hostname
print(socket.gethostbyname(socket.gethostname())) #ip of the given hostname