import cv2
import numpy as np
from model import track
from model import ball
from model import robot


def showImage(img, track, balls, robot):


    #--Draw border-lines--#
    # Convert corners tuples:
    bottomLineA = (track.bottomLeftCorner.x, track.bottomLeftCorner.y)
    bottomLineB = (track.bottomRightCorner.x, track.bottomRightCorner.y)
    leftLineA = (track.bottomLeftCorner.x, track.bottomLeftCorner.y)
    leftLineB = (track.topLeftCorner.x, track.topLeftCorner.y)
    rightLineA = (track.bottomRightCorner.x, track.bottomRightCorner.y)
    rightLineB = (track.topRightCorner.x, track.topRightCorner.y)
    topLineA = (track.topRightCorner.x, track.topRightCorner.y)
    topLineB = (track.topLeftCorner.x, track.topLeftCorner.y)

    if track.bottomLeftCorner.x is not None:
        # Draw bottom line, 180 cm
        cv2.line(img, bottomLineA, bottomLineB, (0, 255, 0), thickness=3, lineType=8)
        # # Draw left line, 120 cm
        cv2.line(img, leftLineA, leftLineB, (0, 255, 0), thickness=3, lineType=8)
        # # Draw right line, 120 cm
        cv2.line(img, rightLineA, rightLineB, (0, 255, 0), thickness=3, lineType=8)
        # # Draw top line, 180 cm
        cv2.line(img, topLineA, topLineB, (0, 255, 0), thickness=3, lineType=8)

    #--Draw goals--#
    # Convert to tuple
    bigGoal = (track.bigGoal.x, track.bigGoal.y)
    smallGoal = (track.smallGoal.x, track.smallGoal.y)

    if track.bottomLeftCorner.x is not None:
        cv2.circle(img, bigGoal, 7, (255, 255, 255), -1)
        cv2.circle(img, smallGoal, 7, (255, 255, 255), -1)

    #--Draw balls--#

    for ball in balls:
        print("lol: " + str(ball.x))
        center = (ball.x, ball.y)
        cv2.circle(img, center, 1, (0, 100, 100), 5)
        # circle outline
        cv2.circle(img, center, ball.radius, (255, 0, 255), 3)

    if robot.blSquareX is not None:
        # contour point
        cv2.circle(img, (robot.blSquareX, robot.blSquareY), 3, 255, -1)

        # center of robot
        cv2.circle(img, (robot.centrumX, robot.centrumY), 4, 255, -1)
        cv2.putText(img, "Robo bot", (robot.centrumX, robot.centrumY), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        # drawing robot outline
        cv2.drawContours(img, [robot.box], 0, (0, 255, 0), 2)

        # danger zone
        cv2.line(img,(bottomLineA[0] + 40, bottomLineA[1] - 40), (bottomLineB[0] - 40 ,bottomLineB[1] - 40), (0,0,255), 2)
        cv2.line(img, (topLineA[0] - 40, topLineA[1] + 40), (topLineB[0] + 40, topLineB[1] + 40),(0, 0, 255), 2)
        cv2.line(img, (rightLineA[0] - 40, rightLineA[1] - 40), (rightLineB[0] - 40, rightLineB[1] + 40),(0, 0, 255), 2)
        cv2.line(img, (leftLineA[0] + 40, leftLineA[1] - 40), (leftLineB[0] + 40, leftLineB[1] + 40),(0, 0, 255), 2)

        # robot to ball line
        # cv2.line(img, (robot.x, robot.y), (ball.x, ball.y), (0, 0, 255), 1)

    # cv2.imshow('frame', img)
    cv2.imshow("images", np.hstack([img]))
