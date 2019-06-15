import time

from brains.detectBalls import getBalls
import math
import numpy as np
import imutils
import cv2
from model import robot
from imutils import contours


def getRobot(img):
    # Capture frame-by-frame
    tempRobot = robot.Robot


    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    boundaries = [
        ([28, 34, 20], [33, 255, 255])
    ]
    boundaries1 = [
        # Dag kørsel:
        # ([120, 100, 20], [170, 255, 255])

        #Nat kørsel:
        ([140, 40, 10], [190, 255, 255])
        #hsv
        #([105, 5, 100], [210, 90, 255])

    ]

    # roed: ([17, 15, 100], [50, 56, 200])
    # blaa: ([86, 31, 4], [220, 88, 50]),
    # gul: ([25, 146, 190], [62, 174, 250])
    # graa: ([103, 86, 65], [145, 133, 128])

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        mask = cv2.inRange(hsv, lower, upper)


    for (lower, upper) in boundaries1:
        # create NumPy arrays from the boundaries
        lower1 = np.array(lower, dtype="uint8")
        upper1 = np.array(upper, dtype="uint8")

        mask1 = cv2.inRange(hsv, lower1, upper1)

        tempRobot = robot.Robot

        # Finding the biggest contour to find robot
        contours, _ = cv2.findContours(mask1, 1, 1)
        max_area = 0
        best_cnt = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt

        # loop over the contours
        cont, _ = cv2.findContours(mask, 1, 1)
        bl_max_area = 0
        bl_best_cnt = 0
        for c in cont:
            # compute the center of the contour
            bl_area = cv2.contourArea(c)
            if bl_area > bl_max_area:
                bl_max_area = bl_area
                bl_best_cnt = c
        B = cv2.moments(bl_best_cnt)

        if B["m00"] != 0:
            cX = int(B["m10"] / B["m00"])
            cY = int(B["m01"] / B["m00"])
        else:
                # set values as what you need in the situation
            cX, cY = 0, 0
            #
            # # draw the contour and center of the shape on the image

        tempRobot.blSquareX = cX
        tempRobot.blSquareY = cY

        # Center of robot
        M = cv2.moments(best_cnt)
        cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        rect = cv2.minAreaRect(best_cnt)

        # Rotating box
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        tempRobot.centrumX = cx
        tempRobot.centrumY = cy
        tempRobot.box = box

        cv2.imshow("maskPurple", mask1)
        cv2.imshow("maskYellow", mask)

   # print("\n")
    return tempRobot
