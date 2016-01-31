#!/usr/bin/env python

import sys
import time
import zmq

from common.Frame import Frame

class LeptonClient(object):
    def __init__(self, *args, **kwargs):
        self.context = zmq.Context()
        self.socket  = self.context.socket(zmq.SUB)
        self.connect(*args, **kwargs)

    def connect(self, host="localhost", port=5556):
        self.socket.connect("tcp://{}:{}".format(host, port))
        self.socket.setsockopt(zmq.SUBSCRIBE, "")

    def recv(self):
        if not self.socket.closed:
            return Frame.from_json(self.socket.recv())
