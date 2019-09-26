# -*- coding: utf-8 -*-
# Simple perforce api demo

import os
import traceback

from contextlib import contextmanager
from P4 import P4, P4Exception
from pprint import pprint

P4USER = os.environ['P4USER']
P4PASSWD = os.environ['P4PASSWD']
P4CLIENT = os.environ['P4CLIENT']
P4PORT = os.environ['P4PORT']

class P4Manager():
    def __init__(self, port, user, password, client):
        self.port = port
        self.user = user
        self.passord = password
        self.client = client
        self.p4 = P4(port=port, user=user, password=password, client=client)
        self.p4.connect()

    def __enter__(self):
        return self.p4

    def __exit__(self, type, value, trace):
        if type is not None:
            print(f'Exception: {value}')
        self.p4.disconnect()
        print('Connection disconnected!')
        return True

def main():
    with P4Manager(P4PORT, P4USER, P4PASSWD, P4CLIENT) as p4:
        # Make a valid call
        info = p4.run("info")
        pprint(info)
        # Let's create an exception
        p4.port = '2000'

if __name__ == '__main__':
    main()
