#!/usr/bin/env python

import sys
import time
import zmq
import numpy as np
try:
    import progressbar
except ImportError:
    progressbar = None

try:
    import pylepton 
except ImportError:
    print "Couldn't import pylepton, using Dummy data!"
    Lepton = None

# importing packages in parent folders is voodoo
from common.Frame import Frame

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:{}".format(port))

widgets = ['Got ', progressbar.Counter(), ' frames (', progressbar.Timer(), ')']
pbar = progressbar.ProgressBar(widgets=widgets, maxval=progressbar.UnknownLength).start()

if pylepton is not None:
    with pylepton.Lepton("/dev/spidev0.1") as lepton:
        n = 0
        while True:
	    arr, idx = lepton.capture()
	    frame = Frame(idx, arr) 
	    #frame = Frame(-1, np.random.random_integers(4095, size=(60.,80.)))
	    socket.send(frame.encode())
            pbar.update(n)
            n += 1
