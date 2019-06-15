import cv2
import numpy as np
import math

#cap = cv2.imread('(3).jpg')
#cap = cv2.VideoCapture('/home/soren/Downloads/VideoOfRobot_2.mov')


clockWise = True


def getAngle(cenBox, blPoint, cenBall):
    global clockwise
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
    return ang


def vector(vector):
    return vector / np.linalg.norm(vector)


def vectorAngle(v1, v2):
    v1_u = vector(v1)
    v2_u = vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def realVectorAngle(p1, p2, p3):
    v0 = np.array(p1) - np.array(p2)
    v1 = np.array(p3) - np.array(p2)
    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
    return np.degrees(angle)


def calculateAngle(pointCord, robot):
    print("Calculate angle")
    ang = getAngle((robot.centrumX, robot.centrumY), (robot.blSquareX, robot.blSquareY),
                   (pointCord[0], pointCord[1]))
    print("routeCon: angle is " + str(ang))
    return ang
