#!/usr/bin/env python3
# from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_D, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.motor import MediumMotor, OUTPUT_D
from ev3dev2.sensor import INPUT_4
# from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
import time

arm = MediumMotor(OUTPUT_D)
ultra = UltrasonicSensor()
ultra.mode = 'US-DIST-CM'

arm.on_for_degrees(10, 90)
time.sleep(1)
arm.on_for_degrees(-10, 90)
while (True):
    print ("Ultralyd: " + str(ultra.value()/10) + "cm")
