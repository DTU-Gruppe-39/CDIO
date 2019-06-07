#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Kode der skal køre på maskine med webcam forbundet
#TODO:
#OpenCV kode
#MEGET

import sys
import time
import json
import os
import threading
import vision
import networking
import re
import globals


#Hvis server og klient skal køre på samme maskine
HOST = "127.0.0.1"
PORT = 6000
MODE = "gfx"
ballarray = []

def instructions():
    print("\nUsage:")
    print("python3 brains.py [mode] [ev3 ip]\n")
    print("Possible modes:")
    print("nogfx - no opencv frame")
    print("gfx - opencv frame shows imagecapture")
    print("nogfxdebug  - NOT YET")
    print("gfxdebug - NOT YET")
    print("\nExample:\n")
    print("Testscenario running ev3.py and brains.py on same machine:")
    print("python3 brains.py nogfx 127.0.0.1")


def checkMode(arg1, arg2):
    """Tjekker mode og argumenter. """
    global HOST
    global MODE
    #mode der kun viser tekst og ikke opencv capt
    if arg1 == "nogfx":
        globals.MODE = "nogfx"
    elif arg1 == "nogfxdebug":
        globals.MODE = "nogfxdebug"
    elif arg1 == "gfx":
        globals.MODE = "gfx"
    elif arg1 == "gfxdebug":
        globals.MODE = "gfxdebug"
    

    #tjek for valid ip
    ipregex = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",arg2)

    if ipregex:
        HOST = arg2
    else:
        print("Invalid ip")
        instructions()
        sys.exit(1)

def main():
    if len(sys.argv) >= 2:
        checkMode(sys.argv[1], sys.argv[2])
    else:
        instructions()
        sys.exit(1)

    try:
        tcpclient = networking.tcpClient(HOST, PORT)
        if tcpclient == None:
            print("Could not connect")
            sys.exit(1)
        else:
            tcpthread = networking.networkThread(1, "tcp socket", tcpclient)
            tcpthread.start()
            vision.imageCaptureBalls(ballarray)

            while True:
                vision.imageCaptureBalls(ballarray)
                #get key
    except KeyboardInterrupt:
        print("Exiting..")
        tcpclient.close()
        time.sleep(1)
        sys.exit(0)




if __name__ == "__main__":

    main()
