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
#import vision
import networking
import re
import globals
import socket


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

def createCommandTank (left, right, degrees):
    message = {
        "type": "tank_drive",
        "left": left,
        "right": right,
        "degrees": degrees
    }
    return message

def createCommandFront (speed, degrees):
    message = {
        "type": "front",
        "speed": speed,
        "degrees": degrees
    }
    return message

def createCommandBack (speed, degrees):
    message = {
        "type": "back",
        "speed": speed,
        "degrees": degrees
    }
    return message


def createCommandAttack (left, right, tank_degrees, front_degrees):
    message = {
        "type": "attack",
        "left": left,
        "right": right,
        "tank_degrees": tank_degrees,
        "front_degrees": front_degrees
    }
    return message

def createCommandDeliver ():
    message = {
        "type": "deliver"
    }
    return message


def main():
    if len(sys.argv) >= 2:
        checkMode(sys.argv[1], sys.argv[2])
    else:
        instructions()
        sys.exit(1)

    try:
        tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpclient.connect((HOST,PORT))
        testing = False
        while True:
            #Run vision
            if testing == False:
                testMs1 = createCommandTank(50, 50, 360*4)
                #testMs1 = createCommandDeliver()
                print(json.JSONEncoder().encode(testMs1))
                dataToSend = json.JSONEncoder().encode(testMs1)
                tcpclient.sendall(dataToSend.encode())
                print("Data sended")
                print(testMs1)
                testing = True

        # tcpclient = networking.tcpClient(HOST, PORT)
        # if tcpclient == None:
        #     print("Could not connect")
        #     sys.exit(1)
        # else:
        #     tcpthread = networking.networkThread(1, "tcp socket", tcpclient)
        #     tcpthread.start()
        #     #vision.imageCaptureBalls(ballarray)
        #
        #     #while True:
        #         #vision.imageCaptureBalls(ballarray)
        #         #get key
        print("disconnected")
    except KeyboardInterrupt:
        print("Exiting..")
        tcpclient.close()
        time.sleep(1)
        sys.exit(0)

if __name__ == "__main__":
    main()

