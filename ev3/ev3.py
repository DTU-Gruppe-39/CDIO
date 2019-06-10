#!/usr/bin/env python3
#Kode der skal køre på ev3
#Fungere som en server hvor "brains" kan forbinde til
#Klienten "brains" sender kommandoer til serveren(ev3) og
#de bliver tilføjet en liste.
#Det er et dictionary der indeholder felterne:
#cmdid - et unikt id for hver ny kommando
#cmdtype - get/set/custom - skal en sensor aflæses eller en motor startes.
#cmdname - en bestemt motor, sensor eller lignende
#cmdstate - init, running, done - hvilken state kommandoen er i - er motor f.eks. i gang at køre
#
#TODO:
#cmdHandler skal bindes til ev3dev's objekter

import sys
import json
import socket
import time
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank, MediumMotor, OUTPUT_A, OUTPUT_D

#Sætter default mode til noev3
#Andre modes: 
#noev3debug - uden ev3 men med debugging
#ev3 - når ev3.py kører på ev3
#ev3debug - når koden kører på ev3 og vi vil have output til debugging
#          
MODE = "noev3"

HOST = None
PORT = 6000

actionslist = []

tank_drive = MoveTank(OUTPUT_C, OUTPUT_B)
left = LargeMotor(OUTPUT_C)
right = LargeMotor(OUTPUT_B)
front = MediumMotor(OUTPUT_A)
back = MediumMotor(OUTPUT_D)


# def cmdHandler(cmd):
#     """Handling af actions. Sensorer der skal aflæses eller motorer der skal tændes"""

#     #hvis det er en sensorvalue der skal læses
#     if cmd["cmdtype"] == "sensor":
#         #her skal være kode til handle
#         pass

#     #hvis det er en motor der skal sættes i gang
#     elif cmd['cmdtype'] == "motor":
#         print(cmd)
#         if cmd['cmdname'] == "right":
#             tank_drive.on_for_rotations(50, 0, cmd['cmddistance'])
#             tank_drive.off()
#             cmd['cmdstate'] = "done"
#         if cmd['cmdname'] == "left":
#             tank_drive.on_for_rotations(0, 50, cmd['cmddistance'])
#             tank_drive.off()
#             cmd['cmdstate'] = "done"
#         if cmd['cmdname'] == "front":
#             tank_drive.on_for_rotations(0, 50, cmd['cmddistance'])
#             tank_drive.off()
#             cmd['cmdstate'] = "done"
#         if cmd['cmdname'] == "back":
#             tank_drive.on_for_rotations(0, 50, cmd['cmddistance'])
#             tank_drive.off()
#             cmd['cmdstate'] = "done"

#     #custom commands - hvis vi har en bestemt
#     #handling der bare skal hardcodes.
#     elif cmd['cmdtype'] == "custom":
#         pass


def cmdHandler2(cmd):
    #hvis det er en motor der skal sættes i gang
        if cmd['type'] == "tank_drive":
            tank_drive.on_for_rotations(cmd['left'], cmd['right'], cmd['degrees'])
            tank_drive.off()
        if cmd['type'] == "front":
            front.on_for_degrees(cmd['speed'], cmd['degrees'])
        if cmd['type'] == "back":
            back.on_for_degrees(cmd['speed'], cmd['degrees'])
        if cmd['type'] == "attack":
            tank_drive.on_for_rotations(cmd['left'], cmd['right'], cmd['tank_degrees'])
            front.on(cmd['front_degrees'])
            tank_drive.off()
        if cmd['type'] == "deliver":
            front.on(-20)
            back.on_for_degrees(10, 90)
            time.sleep(4)
            back.on_for_degrees(-10, 90)
            time.sleep(1)
            front.off()



def tcpServer(PORT, s):

    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            print(msg)
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except OSError as msg:
            print(msg)
            s.close()
            continue
        break
    return(s)

def queueAction(msg):
    """Tilføjer action send fra 'brains'"""
    actionslist.append(msg)

def checkMode(arg):
    if arg == "noev3":
        globals.MODE = "noev3"
    elif arg == "noev3debug":
        globals.MODE = "noev3debug"
    elif arg == "ev3":
        globals.MODE = "ev3"
    elif arg == "ev3debug":
        globals.MODE = "ev3debug"
    elif arg == "help":
        print(sys.argv[0], "instructions here")




def main():

    if len(sys.argv) == 2:
        checkMode(sys.argv[1])

    #lokal ip   
    #localip = socket.gethostbyname(socket.getfqdn())

    print("Starting", sys.argv[0])
    print("Using mode:", MODE)
    #print("Connect to", localip, "on port", PORT)


    s = None

    sockettcp = tcpServer(PORT, s)
    if sockettcp == None:
        print("Could not open socket on port:", PORT)
        sys.exit(1)
    else:
       pass #print(sockettcp)

    while True:
    #    laver socket der er klar til at modtage forbindelse
        print("Waiting for client")
        conn, addr = sockettcp.accept()
        #with conn:
        print(addr, "connected")
        testing = False
        while True:
            try:
                data = conn.recv(1024)
                msg = json.loads(data.decode('utf-8'))
                if testing == False:
                    cmdHandler2(msg)
                    testing = True
                        #Husk fjern udført kommand fra listen
                if not data: break
            except Exception as e:
                print(e)
                print("Client disconnected")
                break




if __name__ == "__main__":
    main()