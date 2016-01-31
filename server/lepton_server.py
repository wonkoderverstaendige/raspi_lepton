#!/usr/bin/env python

import sys
import time
#from pylepton import Lepton
import zmq

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:{}".format(port))

n = 0
while True:
    socket.send("Server message {}".format(n))
    n += 1

