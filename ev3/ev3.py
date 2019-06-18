#!/usr/bin/env python3
#Kode der skal køre på ev3

import sys
import json
import socket
import time
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank, MediumMotor, OUTPUT_A, OUTPUT_D
from ev3dev2.sound import Sound
       
HOST = None
PORT = 6000

tank_drive = MoveTank(OUTPUT_C, OUTPUT_B)
left = LargeMotor(OUTPUT_C)
right = LargeMotor(OUTPUT_B)
front = MediumMotor(OUTPUT_A)
back = MediumMotor(OUTPUT_D)

sound = Sound()

def cmdHandler(cmd):
        if cmd['type'] == "tank_drive":
            tank_drive.on_for_degrees(cmd['left'], cmd['right'], cmd['degrees'])
            tank_drive.off()
        if cmd['type'] == "front":
            front.on_for_degrees(cmd['speed'], cmd['degrees'])
        if cmd['type'] == "back":
            back.on_for_degrees(cmd['speed'], cmd['degrees'])
        if cmd['type'] == "attack":
            tank_drive.on_for_degrees(cmd['left'], cmd['right'], cmd['tank_degrees'])
            front.on_for_degrees(20, cmd['front_degrees'])
            sound.play_file('/home/robot/CDIO/sounds/DJ_Khaled_Another_One_Sound_Effect_HD-E71Dlf4ccXQ.wav',  play_type=1)
        if cmd['type'] == "deliver":
            front.on_for_degrees(-20, 180)
            back.on_for_degrees(10, 90)
            time.sleep(4)
            back.on_for_degrees(-10, 90)
            time.sleep(1)
            back.on_for_degrees(10, 90)
            time.sleep(1)
            back.on_for_degrees(-10, 90)
            back.on_for_degrees(10, 90)
            # back.on_for_degrees(-10, 90)
            # back.on_for_degrees(10, 90)
            back.on_for_degrees(-10, 90)
            back.on_for_degrees(10, 90)
            time.sleep(2)
            back.on_for_degrees(-10, 90)
            time.sleep(1)
            front.on_for_degrees(20, 180)
        if cmd['type'] == "wall":
            front.on_for_degrees(10, 45)
            front.on_for_degrees(-10, 45)
            front.on_for_degrees(-cmd['speed'], cmd['arm_degrees'])
            tank_drive.on_for_degrees(cmd['speed'], cmd['speed'], cmd['tank_degrees'])
            front.on_for_degrees(cmd['speed'], cmd['arm_degrees'])
            tank_drive.on_for_degrees(-cmd['speed']*3, -cmd['speed']*3, cmd['tank_degrees'])
            sound.play_file('/home/robot/CDIO/sounds/DJ_Khaled_Another_One_Sound_Effect_HD-E71Dlf4ccXQ.wav',  play_type=1)
        if cmd['type'] == "cross":
            front.on_for_degrees(10, 45)
            front.on_for_degrees(-10, 45)
            front.on_for_degrees(-cmd['speed'], cmd['arm_degrees'])
            tank_drive.on_for_degrees(cmd['speed'], cmd['speed'], cmd['tank_degrees'])
            front.on_for_degrees(cmd['speed'], cmd['cross_arm_degrees']) #close a little
            front.on_for_degrees(cmd['speed'], cmd['arm_degrees'] - cmd['cross_arm_degrees'])
            tank_drive.on_for_degrees(-cmd['speed']*3, -cmd['speed']*3, cmd['tank_degrees'])
            sound.play_file('/home/robot/CDIO/sounds/DJ_Khaled_Another_One_Sound_Effect_HD-E71Dlf4ccXQ.wav',  play_type=1)
        if cmd['type'] == "w":
            tank_drive.on(30, 30)
        if cmd['type'] == "a":
            tank_drive.on(-20, 20)
        if cmd['type'] == "s":
            tank_drive.on(-15, -15)
        if cmd['type'] == "d":
            tank_drive.on(20, -20)
        if cmd['type'] == "stop":
            tank_drive.off()
        if cmd['type'] == "sound":
            # sound.speak(text)
            sound.play_file('/home/robot/CDIO/sounds/we-are-the-champions-copia.wav')
            #sound.beep().wait()
            # sound.tone([(500, 1000, 400)] * 3)



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

def main():

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
        while True:
            try:
                # print("Before recv..")
                data = conn.recv(1024)
                # print("Before load..")
                # print("Data: " + str(data))
                msg = json.loads(data.decode())
                    # print("Before handler..")
                cmdHandler(msg)
                try:
                    command = {
                        "type": "sucess"
                    }
                    dataToSend = json.JSONEncoder().encode(command)
                    conn.sendall(dataToSend.encode())
                except Exception as e:
                    print("Respond failed e:" + e)
                        #Husk fjern udført kommand fra listen
                # if not data: break
            except Exception as e:
                print(e)
                print("Client disconnected")
                break


if __name__ == "__main__":
    main()