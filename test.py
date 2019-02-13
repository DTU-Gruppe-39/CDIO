#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
# from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds

# TODO: Add code here
leds = Leds()
leds.set_color('LEFT', 'AMBER')

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
ultra = UltrasonicSensor()
ultra.mode = 'US-DIST-CM'

while (ultra.value()/10) > 10:
    tank_drive.on(50,50)

tank_drive.off()