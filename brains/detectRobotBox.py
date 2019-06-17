import time

from brains.detectBalls import getBalls
import math
import numpy as np
import imutils
import cv2
from model import robot
from model import point
from brains.correction import point_correction
from imutils import contours


def getRobot(img):
    # Capture frame-by-frame
    tempRobot = robot.Robot


    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    boundaries = [
        ([27, 54, 20], [32, 255, 255])
    ]
    boundaries1 = [
        # Dag kørsel:
        ([120, 100, 20], [170, 255, 255])

        #Nat kørsel:
        # ([140, 40, 10], [190, 255, 255])
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
            cX = round(B["m10"] / B["m00"])
            cY = round(B["m01"] / B["m00"])
        else:
                # set values as what you need in the situation
            cX, cY = 0, 0
            #
            # # draw the contour and center of the shape on the image
        x_val = np.amax(img, axis=0)
        y_val = np.amax(img, axis=1)
        x_val = round(len(x_val)/2)
        y_val = round(len(y_val)/2)
        camera_center = point.Point(x_val, y_val)
        bl = point.Point(cX, cY)
        blSquare_corrected = point_correction(camera_center, bl)
        # tempRobot.blSquareX = cX
        # tempRobot.blSquareY = cY

        tempRobot.blSquareX = blSquare_corrected.x
        tempRobot.blSquareY = blSquare_corrected.y

        # Center of robot
        M = cv2.moments(best_cnt)
      cx, cy = round(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        rect = cv2.minAreaRect(best_cnt)

        # Rotating box
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        robot_center = point.Point(cx, cy)
        center_corrected = point_correction(camera_center, robot_center)

        # tempRobot.centrumX = cx
        # tempRobot.centrumY = cy
        tempRobot.centrumX = center_corrected.x
        tempRobot.centrumY = center_corrected.y
        tempRobot.box = box

        scale_percent = 30  # percent of original size
        width = int(mask1.shape[1] * scale_percent / 100)
        height = int(mask1.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(mask1, dim, interpolation=cv2.INTER_AREA)

        scale_percent = 30  # percent of original size
        width = int(mask.shape[1] * scale_percent / 100)
        height = int(mask.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized1 = cv2.resize(mask, dim, interpolation=cv2.INTER_AREA)


        cv2.imshow("maskPurple", resized)
        cv2.imshow("maskYellow", resized1)

   # print("\n")
    return tempRobot
