#!/usr/bin/env python

import sys
import time
import zmq
import numpy as np

try:
    from pylepton import Lepton
except ImportError:
    print "Couldn't import pylepton, using Dummy data!"
    Lepton = None

# importing packages in parent folders is voodoo
from common.Frame import Frame

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:{}".format(port))

n = 0
while True:
    frame = Frame(n, np.random.random_integers(255, size=(60.,80.)))
    socket.send(frame.encode())
    time.sleep(0.1)
    n += 1

