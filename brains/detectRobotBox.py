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

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


    boundaries = [
        ([100, 150, 20], [140, 255, 255])
    ]
    boundaries1 = [
        ([60, 0, 100], [255, 75, 255])
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
        # the mask

        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(mask, 1, 2, cv2.THRESH_BINARY)[1]

    for (lower, upper) in boundaries1:
        # create NumPy arrays from the boundaries
        lower1 = np.array(lower, dtype="uint8")
        upper1 = np.array(upper, dtype="uint8")

        mask1 = cv2.inRange(img, lower1, upper1)
        output += cv2.bitwise_and(img, img, mask=mask1)


        gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        minDist = 0
        x = 0
        y = 0
        cirX = 0
        cirY = 0
        tempRobot = robot.Robot

        # Bounding box of robot
        x, y, w, h = cv2.boundingRect(mask)
        #cv2.rectangle(img, (x - 40, y - 35), (x + w + 35, y + h + 35), (255, 0, 0), 1)

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
        for c in cont:
            # compute the center of the contour
            M = cv2.moments(c)

            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                # set values as what you need in the situation
                cX, cY = 0, 0
            #
            # # draw the contour and center of the shape on the image

          #  cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
         #   cv2.circle(img, (cX, cY), 1, (0, 255, 255), 2)
            tempRobot.blSquareX = cont[0][0][0][0]
            tempRobot.blSquareY = cont[0][0][0][1]

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

        # Smallest distance from robot to ball
        # dist = math.sqrt(pow(i[0] - x, 2) + pow(i[1] - y, 2))
        #
        # # print(minDist)
        # if (minDist == 0):
        #     minDist = dist
        # elif (dist < minDist):
        #     minDist = 0
        #     minDist = dist
        #     cirX = i[0]
        #     cirY = i[1]
        #     #print(minDist)
        #
        #     cv2.line(img, (cx, cy), (cirX, cirY), (0, 0, 255), 1)

        cv2.imshow("mask", mask)
   # print("\n")
    return tempRobot









