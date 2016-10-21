#! /usr/bin/env python3

"""
This is the main file for the client and of the Carrier Pigeon Suite.
"""

import sys

sys.path += ["../"]

import readline
from carrier_pigeon_classes.message import *

"""
[TODO] Add code here to establish connection to remote host...
"""

while True:
    try:
        msg = Message(input("carrier-pigeon> "))
    except EOFError:
        # user hung up on us
        # exit, but before we do, send the prompt to the next line
        print("")
        sys.exit(0)

    if (len(msg) > 0):
        print("trying to send '" + str(msg) + "'...")
    """
    [TODO] Add code to actually send the message to the remote end here
    """
