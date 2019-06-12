import cv2
import numpy as np
import math

#cap = cv2.imread('(3).jpg')
#cap = cv2.VideoCapture('/home/soren/Downloads/VideoOfRobot_2.mov')

class angle:
    clockWise = True

    def getAngle(cenBox, blPoint, cenBall):
        ang = math.degrees(math.atan2(cenBall[1] - blPoint[1], cenBall[0] - blPoint[0]) - math.atan2(cenBox[1] - blPoint[1], cenBox[0] - blPoint[0]))
        clockWise = True
        if ang < 0:
            ang = ang + 180
        if cenBox[0] < blPoint[0] and cenBox[1] > cenBall[1] or cenBox[1] < cenBall[1] and cenBox[0] > blPoint[0]:
                ang = 180 - ang
                clockWise = False
        return ang