#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_D, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
# from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds

# TODO: Add code here
leds = Leds()
leds.set_color('LEFT', 'AMBER')

arm = MediumMotor(OUTPUT_D)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
ultra = UltrasonicSensor()
ultra.mode = 'US-DIST-CM'

arm.on(50)
while (True) :
    while (ultra.value()/10) > 30:
        tank_drive.on(50,50)

    tank_drive.off()
    tank_drive.on_for_rotations(0, 20, 1)

