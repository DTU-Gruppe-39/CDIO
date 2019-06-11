# -*- coding: utf-8 -*-

import sys
import time
import json
import os
import networking
import re
import globals
import socket


HOST = "172.20.10.5"
PORT = 6000
INIT = True
tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# def checkMode(arg1, arg2):
#     global HOST

#     #tjek for valid ip
#     ipregex = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",arg2)

#     if ipregex:
#         HOST = arg2
#     else:
#         print("Invalid ip")
#         sys.exit(1)


def sendCommand(command):
    global INIT
    global tcpclient
    # if len(sys.argv) >= 2:
    #     checkMode(sys.argv[1], sys.argv[2])
    # else:
    #     sys.exit(1)

    try:
        if INIT:
            # tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpclient.connect((HOST,PORT))
            INIT = False

        # tcpclient.
        print(json.JSONEncoder().encode(command))
        dataToSend = json.JSONEncoder().encode(command)
        tcpclient.sendall(dataToSend.encode())
        print("Data sent")
    except KeyboardInterrupt:
        print("Exiting..")
        tcpclient.close()
        time.sleep(1)
        sys.exit(0)
