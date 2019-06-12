import cv2
import numpy as np
import math

#cap = cv2.imread('(3).jpg')
#cap = cv2.VideoCapture('/home/soren/Downloads/VideoOfRobot_2.mov')


def getAngle(cenBox, blPoint, cenBall):
    ang = math.degrees(math.atan2(cenBall[1] - blPoint[1], cenBall[0] - blPoint[0]) - math.atan2(cenBox[1] - blPoint[1], cenBox[0] - blPoint[0]))
    if ang < 0:
        ang = ang + 180
        clockwise = True
    if cenBox[0] < blPoint[0] and cenBox[1] > cenBall[1] or cenBox[1] < cenBall[1] and cenBox[0] > blPoint[0]:
            ang = 180 - ang
            clockwise = False
    return ang, clockwise
