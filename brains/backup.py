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
        ([27, 40, 20], [32, 255, 255])
    ]
    boundaries1 = [
        ([120, 100, 20], [170, 255, 255])
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
        areaArray = []

        # Finding the biggest contour to find robot
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            areaArray.append(area)

        sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)

        # find the nth largest contour [n-1][1], in this case 2
        largestcontour = sorteddata[0][1]

        M = cv2.moments(largestcontour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            # set values as what you need in the situation
            cX, cY = 0, 0

        tempRobot.blSquareX = cX
        tempRobot.blSquareY = cY

        print("RobotGulX" + str(tempRobot.blSquareX))
        print("RobotGulY" + str(tempRobot.blSquareY))

        areaArray = []

        # Finding the biggest contour to find robot
        contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            areaArray.append(area)

        sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)

        # find the nth largest contour [n-1][1], in this case 2
        largestcontour = sorteddata[0][1]

        M = cv2.moments(largestcontour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            # set values as what you need in the situation
            cX, cY = 0, 0

        tempRobot.centrumX = cX
        tempRobot.centrumY = cY

        print("RobotLillaX" + str(tempRobot.centrumX))
        print("RobotLillaY" + str(tempRobot.centrumY))


        # max_area = 0
        # best_cnt = 0
        # for cnt in contours:
        #     area = cv2.contourArea(cnt)
        #     if area > max_area:
        #         max_area = area
        #         best_cnt = cnt
        #
        # # loop over the contours
        # cont, _ = cv2.findContours(mask, 1, 1)
        # bl_max_area = 0
        # bl_best_cnt = 0
        # for c in cont:
        #     # compute the center of the contour
        #     bl_area = cv2.contourArea(cnt)
        #     if bl_area > bl_max_area:
        #         bl_max_area = bl_area
        #         bl_best_cnt = cnt
        #     M = cv2.moments(bl_best_cnt)
        #
        #     if M["m00"] != 0:
        #         cX = int(M["m10"] / M["m00"])
        #         cY = int(M["m01"] / M["m00"])
        #     else:
        #         # set values as what you need in the situation
        #         cX, cY = 0, 0
        #     #
        #     # # draw the contour and center of the shape on the image
        #
        #   #  cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        #  #   cv2.circle(img, (cX, cY), 1, (0, 255, 255), 2)
        #     tempRobot.blSquareX = cont[0][0][0][0]
        #     tempRobot.blSquareY = cont[0][0][0][1]

        # Center of robot
        # M = cv2.moments(best_cnt)
        # cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        # rect = cv2.minAreaRect(best_cnt)



        # # Rotating box
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        #
        # tempRobot.centrumX = cx
        # tempRobot.centrumY = cy
        # tempRobot.box = box

        # contour point
        cv2.circle(img, (tempRobot.blSquareX, tempRobot.blSquareY), 3, 255, -1)

        # center of robot
        cv2.circle(img, (tempRobot.centrumX, tempRobot.centrumY), 4, 255, -1)

        cv2.imshow("Img", img)
        cv2.imshow("mask1", mask1)
        cv2.imshow("mask", mask)
   # print("\n")
    return tempRobot









