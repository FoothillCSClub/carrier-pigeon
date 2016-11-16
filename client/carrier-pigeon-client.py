#! /usr/bin/env python3

"""
This is the main file for the client and of the Carrier Pigeon Suite.
"""

import sys

sys.path += ["../"]

import readline
from socket import *
from selectors import *
from carrier_pigeon_classes.message import *

def fatal(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def print_prompt():
    print("carrier-pigeon> ", end='', file=sys.stdout)
    sys.stdout.flush()

connect_host = "foothillstemclubs.org"
connect_port = 4545

sock = socket()
try:
    # set network timeout to something sane
    sock.settimeout(5)
    sock.connect((connect_host, connect_port))
    network_send = sock.makefile(mode="w", encoding="utf-8", buffering=4096)
    network_recv = sock.makefile(mode="r", encoding="utf-8", buffering=4096)
except BaseException as e:
    fatal("Error connecting to " + connect_host + ":" + str(connect_port) + ": " + str(e))

io_selector = DefaultSelector()
io_selector.register(sys.stdin, EVENT_READ)
io_selector.register(network_recv, EVENT_READ)

while True:
    print_prompt()

    input_ready = io_selector.select()

    for key, events in input_ready:
        if key.fileobj is sys.stdin:
            input_line = sys.stdin.readline()
            if input_line == '':
                # user hung up on us
                # exit, but before we do, send the prompt to the next line
                print("")
                sys.exit(0)

            # chomp trailing newline
            msg = Message(input_line[:-1])

            if (len(msg) > 0):
                try:
                    print(msg.serialize(), file=network_send)
                    network_send.flush()
                except BaseException as e:
                    fatal("Error sending message to remote host: " + str(e))
        elif key.fileobj is network_recv:
            # XXX: crude hack; what if the network is only ready to give us part of the message?
            network_input = network_recv.readline()
            if network_input == "":
                exit("remote end hung up")
            try:
                msg = Message.deserialize(network_input)
                print("")
                print(msg)
            except BaseException as e:
                print("Error parsing message from network: " + str(e))
