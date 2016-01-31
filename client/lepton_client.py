#!/usr/bin/env python

import sys
import time
import zmq

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:{}".format(port))
socket.setsockopt(zmq.SUBSCRIBE, "")

while True:
    print socket.recv()
