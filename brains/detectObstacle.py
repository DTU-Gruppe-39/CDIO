import cv2
import math
import imutils
import numpy as np
from model import track
import brains.singleton as singleton
from model import obstacle


def getObstacle(img):

    tempObstacle = obstacle.Obstacle

    tempTrack = singleton.Singleton.track

    if tempTrack.bottomRightCorner is not None:
        pixelConversion = tempTrack.pixelConversion
        scale = int(pixelConversion*5)

        low_x_roi = tempTrack.topLeftCorner.x + scale + round(scale/2)
        up_x_roi = tempTrack.bottomRightCorner.x - scale - round(scale/2)
        low_y_roi = tempTrack.topLeftCorner.y + round(1.5 * scale)
        up_y_roi = tempTrack.bottomRightCorner.y - round(1.5 * scale)

        roi = img[low_y_roi:up_y_roi, low_x_roi:up_x_roi]

        blurred_frame = cv2.GaussianBlur(roi, (5, 5), 0)

        img_hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

        # lower mask (0-10)
        lower_red = np.array([0, 150, 20])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([175, 150, 20])
        upper_red = np.array([180, 255, 255])
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

        # join my masks
        mask = mask0 + mask1

        areaArray = []
        count = 1

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, offset=(low_x_roi, low_y_roi))
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            areaArray.append(area)

        # first sort the array by area
        sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)

        # find the nth largest contour [n-1][1], in this case 2
        largestContour = sorteddata[0][1]


        # compute the center of the contour
        if largestContour is not None:
            M = cv2.moments(largestContour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            tempObstacle.x = cX
            tempObstacle.y = cY

            # draw the contour and center of the shape on the image
            cv2.drawContours(img, [largestContour], -1, (0, 255, 0), 2)
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(img, "center", (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow("image", img)
        cv2.imshow("mask", mask)

    return tempObstacle
