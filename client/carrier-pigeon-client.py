#! /usr/bin/env python3

"""
This is the main file for the client and of the Carrier Pigeon Suite.
"""

import sys
import readline

"""
[TODO] Add code here to establish connection to remote host...
"""

while True:
    try:
        line = input("carrier-pigeon> ")
    except EOFError:
        # user hung up on us
        # exit, but before we do, send the prompt to the next line
        print("")
        sys.exit(0)

    """
    [TODO] Add code to actually send the message to the remote end here
    """

    print("trying to send '" + line + "'...")
