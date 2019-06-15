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


def main():
    front.on_for_degrees(20, 180)
    if front.is_stalled():
        front.stop()
        time.sleep(1)






if __name__ == "__main__":
    main()