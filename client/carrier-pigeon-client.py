#! /usr/bin/env python3

"""
This is the main file for the client and of the Carrier Pigeon Suite.
"""

import sys

sys.path += ["../"]

import readline
from socket import *
from carrier_pigeon_classes.message import *

def fatal(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

connect_host = "foothillstemclubs.org"
connect_port = 4545

sock = socket()
try:
    # set network timeout to something sane
    sock.settimeout(5)
    sock.connect((connect_host, connect_port))
    fsock = sock.makefile(mode="w", encoding="utf-8", buffering=4096)
except Exception as e:
    fatal("Error connecting to " + connect_host + ":" + str(connect_port) + ": " + str(e))

while True:
    try:
        msg = Message(input("carrier-pigeon> "))
    except EOFError:
        # user hung up on us
        # exit, but before we do, send the prompt to the next line
        print("")
        sys.exit(0)

    if (len(msg) > 0):
        try:
            print(msg, file=fsock)
            fsock.flush()
        except Exception as e:
            fatal("Error sending message to remote host: " + str(e))
