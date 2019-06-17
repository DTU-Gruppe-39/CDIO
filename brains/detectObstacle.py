import cv2
import math
import imutils
import numpy as np
from model import track
from model import point
from shapely.geometry import LineString
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

            # Set the centerpoint of the obstacle
            tempObstacle.center_x = cX
            tempObstacle.center_y = cY

            # variables for 20 and 25 in pixels
            cm15_in_pix = round(15 * tempTrack.pixelConversion)
            cm20_in_pix = round(20 * tempTrack.pixelConversion)
            cm25_in_pix = round(25 * tempTrack.pixelConversion)

            # makes the top_left corner of the bounding square
            top_left_y = cY - cm20_in_pix
            top_left_x = cX - cm20_in_pix

            # makes the top_right corner of the bounding square
            top_right_y = cY - cm20_in_pix
            top_right_x = cX + cm20_in_pix

            # makes the bottom_left corner of the bounding square
            bottom_left_y = cY + cm20_in_pix
            bottom_left_x = cX - cm20_in_pix

            # makes the bottom_right corner of the bounding square
            bottom_right_y = cY + cm20_in_pix
            bottom_right_x = cX + cm20_in_pix

            # makes the lines of the bounding square
            tempObstacle.right_line = LineString([(bottom_right_x, bottom_right_y), (top_right_x, top_right_y)])
            tempObstacle.top_line = LineString([(top_left_x, top_left_y), (top_right_x, top_right_y)])
            tempObstacle.left_line = LineString([(bottom_left_x, bottom_left_y), (top_left_x, top_left_y)])
            tempObstacle.bottom_line = LineString([(bottom_left_x, bottom_left_y), (bottom_right_x, bottom_right_y)])

            # Make midpoints for the dangerzone lines around the obstacle
            rightMidPt = tempObstacle.right_line.interpolate(0.5, normalized=True)
            topMidPt = tempObstacle.top_line.interpolate(0.5, normalized=True)
            bottomtMidPt = tempObstacle.bottom_line.interpolate(0.5, normalized=True)
            leftMidPt = tempObstacle.left_line.interpolate(0.5, normalized=True)

            # Calculate points on border that are projected 90 degrees from midpoints - 20 cm
            a = (int(tempTrack.topRightCorner.x - cm15_in_pix ), int(rightMidPt.y))
            b = (int(topMidPt.x), int(tempTrack.topRightCorner.y + cm15_in_pix ))
            c = (int(bottomtMidPt.x), int(tempTrack.bottomRightCorner.y - cm15_in_pix ))
            d = (int(tempTrack.topLeftCorner.x + cm15_in_pix ), int(leftMidPt.y))

            # Find the safepoints that are halfway between the midpoints and the 90 degree points - 20 cm
            safePoint1 = LineString([rightMidPt, a]).interpolate(0.5, normalized=True)
            safePoint2 = LineString([topMidPt, b]).interpolate(0.5, normalized=True)
            safePoint3 = LineString([bottomtMidPt, c]).interpolate(0.5, normalized=True)
            safePoint4 = LineString([leftMidPt, d]).interpolate(0.5, normalized=True)

            # Clear old safepoints
            singleton.Singleton.safe_points.clear()

            # Add to singleton
            singleton.Singleton.safe_points.append(point.Point(safePoint1.x, safePoint1.y))
            singleton.Singleton.safe_points.append(point.Point(safePoint2.x, safePoint2.y))
            singleton.Singleton.safe_points.append(point.Point(safePoint3.x, safePoint3.y))
            singleton.Singleton.safe_points.append(point.Point(safePoint4.x, safePoint4.y))


            # # defines the midpoints of the bounding square
            # obstacle_danger_left_x = tempObstacle.center_x - cm20_in_pix
            # obstacle_danger_top_y = tempObstacle.center_y - cm20_in_pix
            # obstacle_danger_right_x = tempObstacle.center_x + cm20_in_pix
            # obstacle_danger_bottom_y = tempObstacle.center_y + cm20_in_pix
            # # defines half the distance between the danger zone of the track and the obstacle for the left side
            # left_safe_point_danger = (obstacle_danger_left_x - (tempTrack.topLeftCorner.x + cm25_in_pix))/2
            # # defines the left_safe_point and puts it in the singleton
            # singleton.Singleton.safe_points.append(point.Point(obstacle_danger_left_x - left_safe_point_danger, tempObstacle.center_y))
            # # defines half the distance between the danger zone of the track and the obstacle for the top side
            # top_safe_point_danger = (obstacle_danger_top_y - (tempTrack.topLeftCorner.y + cm25_in_pix))/2
            # # defines the top safe point and puts it in the singleton
            # singleton.Singleton.safe_points.append(point.Point(tempObstacle.center_x, obstacle_danger_top_y - top_safe_point_danger))
            # # defines half the distance between the danger zone of the track and the obstacle for the right side
            # right_safe_point_danger = ((tempTrack.topRightCorner.x - cm25_in_pix) - obstacle_danger_right_x) / 2
            # # defines the right safe point and puts it in the singleton
            # singleton.Singleton.safe_points.append(point.Point(obstacle_danger_right_x + right_safe_point_danger, tempObstacle.center_y))
            # # defines half the distance between the danger zone of the track and the obstacle for the bottom side
            # bottom_safe_point_danger = ((tempTrack.bottomLeftCorner.y - cm25_in_pix) - obstacle_danger_bottom_y) / 2
            # # defines the bottom safe point and puts it in the singleton
            # singleton.Singleton.safe_points.append(point.Point(tempObstacle.center_x, obstacle_danger_bottom_y + bottom_safe_point_danger))

            # draw the contour and center of the shape on the image
            cv2.drawContours(img, [largestContour], -1, (0, 255, 0), 2)
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(img, "center", (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # cv2.imshow("image", img)
        # cv2.imshow("mask", mask)

    return tempObstacle
