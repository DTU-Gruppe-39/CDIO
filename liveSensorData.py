#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_4
# from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor

ultra = UltrasonicSensor()
ultra.mode = 'US-DIST-CM'

while (True):
    print ("Ultralyd: " + str(ultra.value()/10) + "cm")