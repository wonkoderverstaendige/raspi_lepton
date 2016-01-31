#!/usr/bin/env python
import numpy as np
from client.client import LeptonClient
from common.render import print_arr
from scipy.misc import imsave

client = LeptonClient(host="192.168.2.107", port=5556)
while True:
    frame = client.recv()
    #imsave("frame.png", frame.arr)
    print_arr(frame.arr.astype(np.float))

print "Client Done"

