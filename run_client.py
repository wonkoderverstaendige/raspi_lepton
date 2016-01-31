#!/usr/bin/env python
from client.client import LeptonClient

client = LeptonClient(host="localhost", port=5556)
frame = client.recv()
from scipy.misc import imsave
imsave("frame.png", frame.arr)
print "Client Done"

