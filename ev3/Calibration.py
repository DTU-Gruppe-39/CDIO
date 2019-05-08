#!/usr/bin/env python3
# from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, MoveTank, MediumMotor, OUTPUT_A, OUTPUT_D 
import math
import time

# Button.waitForAnyPress()
tank_drive = MoveTank(OUTPUT_C, OUTPUT_B)
left = LargeMotor(OUTPUT_C)
right = LargeMotor(OUTPUT_B)
arm = MediumMotor(OUTPUT_A)
lift = MediumMotor(OUTPUT_D)

squareSize = 100
wheelCircunference = 3 * math.pi
wheelBase = 12.5
speed = 25


for j in range(5):
    arm.on(20)
    for i in range(4): 
        # Move straight the squareSize centimetres
        degrees = math.floor((squareSize / wheelCircunference) * 360.0)
        print("Degrees" + str(degrees))
        # left.on_for_degrees(speed, degrees)
        # right.on_for_degrees(speed, degrees)
        tank_drive.on_for_degrees(speed*2, speed*2, degrees)
        tank_drive.wait_until_not_moving()
        time.sleep(1)
        
        # Rotate on the spot 
        degrees = math.floor((((wheelBase * math.pi) / 4.0) / wheelCircunference) * 360.0)
        print("Degrees" + str(degrees))
        # left.on_for_degrees(speed, -degrees)
        # right.on_for_degrees(speed, degrees)
        # left.wait_until_not_moving()
        tank_drive.on_for_degrees(-speed, speed, degrees)
        tank_drive.wait_until_not_moving()
        time.sleep(1)
    
    arm.on(-20)
    lift.on_for_degrees(10, 90)
    time.sleep(4)
    lift.on_for_degrees(-10, 90)
    time.sleep(1)
  
    # System.out.println("CW: "+(j+1)+"/5")
    # brick.getAudio().systemSound(0)
    # Button.waitForAnyPress()
