import cv2
import numpy as np
import math

#cap = cv2.imread('(3).jpg')
#cap = cv2.VideoCapture('/home/soren/Downloads/VideoOfRobot_2.mov')

class angle:
    clockWise = True

def getAngle(cenBox, blPoint, cenBall):
    ang = math.degrees(math.atan2(cenBall[1] - blPoint[1], cenBall[0] - blPoint[0]) - math.atan2(cenBox[1] - blPoint[1], cenBox[0] - blPoint[0]))
    rotation = (blPoint[0] - cenBox[0]) * (cenBall[1] - cenBox[1]) - (blPoint[1] - cenBox[1]) * (cenBall[0] - cenBox[0])
    if ang < 0 and rotation > 0:
        ang = ang + 180
        clockwise = True
    if ang > 180:
        ang = ang - 180
        clockwise = True
    if rotation < 0:
            ang = 180 - ang
            clockwise = False
            if ang > 180:
                ang = ang - 360
                clockwise = False
    return ang, clockwise
