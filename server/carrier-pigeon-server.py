#! /usr/bin/env python3

import sys
from socket import *

def fatal(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

server_port = 4545
listener_queuedepth = 20
network_family = AF_INET

listen_socket = socket(AF_INET, SOCK_STREAM)
try:
    listen_socket.bind(("", server_port))
    listen_socket.listen(listener_queuedepth)
except Exception as e:
    fatal("Error listening to port " + str(server_port) + ": " + str(e))

print("Ready to rumble on port " + str(server_port))

while True:
    connection_socket, client_address = listen_socket.accept()
    print("Client connected from " + client_address[0] + ":" + str(client_address[1]))
    socket_file = connection_socket.makefile(mode="w", encoding="utf-8", buffering=4096)

    print("Hello, %s" % client_address[0], file=socket_file)
    socket_file.flush()

    socket_file.close()
    connection_socket.close()
