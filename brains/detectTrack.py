import cv2
import imutils
import numpy as np
from model import Track
from model import corner
from model import Point


def sort(points):

    # Sorted array:
    # [Top left, Bottom left, Top right, Bottom right]

    arr = points

    arr.sort()

    if arr[0][1] > arr[1][1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp

    if arr[2][1] > arr[3][1]:
        temp = arr[2]
        arr[2] = arr[3]
        arr[3] = temp

    return arr


def calculateGoals(corner1, corner2):

    goalMidpoint = Point.Point(int((corner1.x + corner2.x)/2), int((corner1.y + corner2.y)/2))

    # goalMidpoint.x = (corner1.x + corner2.x)/2
    # goalMidpoint.y = (corner1.y + corner2.y)/2

    return goalMidpoint


def getTrack(frame):

    tempTrack = Track.Track

    corner_boundaries = [
        ([43, 40, 40], [97, 255, 255])
        # ([86, 0, 0], [255, 0, 0])
    ]

    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    points = []

    # loop over the boundaries
    for (lower, upper) in corner_boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(hsv, lower, upper)
        # coutput = cv2.bitwise_and(hsv, hsv, mask=mask)

    # find contours in the thresholded image
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    count = 0

    # loop over the contours
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        count = count + 1
        # print(str(count))
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # print("count: " + str(count) + " cX: " + str(cX) + " cY: " + str(cY))

            # draw the contour and center of the shape on the image
            # cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            # cv2.circle(frame, (cX, cY), 3, (255, 255, 255), -1)
            # cv2.putText(frame, "center", (cX - 20, cY - 20),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # print("X: " + str(cX))
            # print("Y: " + str(cY))

            # Add points to array of points
            points.append([cX, cY])

    if len(points) == 4:

        # Set corners on track object
        sortedPoints = sort(points)

        tempTrack.topLeftCorner = corner.Corner(sortedPoints[0][0], sortedPoints[0][1])
        tempTrack.bottomLeftCorner = corner.Corner(sortedPoints[1][0], sortedPoints[1][1])

        tempTrack.topRightCorner = corner.Corner(sortedPoints[2][0], sortedPoints[2][1])
        tempTrack.bottomRightCorner = corner.Corner(sortedPoints[3][0], sortedPoints[3][1])

        # Calculate goals
        tempTrack.smallGoal = calculateGoals(tempTrack.topLeftCorner, tempTrack.bottomLeftCorner)

        tempTrack.bigGoal = calculateGoals(tempTrack.topRightCorner, tempTrack.bottomRightCorner)

    return tempTrack

















    # if len(points) == 4:
    #     # Draw bottom line, 180 cm
    #     cv2.line(frame, tuple(sortedPoints[1]), tuple(sortedPoints[3]), (0, 255, 0), thickness=3, lineType=8)
    #     # # Draw left line, 120 cm
    #     cv2.line(frame, tuple(sortedPoints[0]), tuple(sortedPoints[1]), (0, 255, 0), thickness=3, lineType=8)
    #     # # Draw right line, 120 cm
    #     cv2.line(frame, tuple(sortedPoints[2]), tuple(sortedPoints[3]), (0, 255, 0), thickness=3, lineType=8)
    #     # # Draw top line, 180 cm
    #     cv2.line(frame, tuple(sortedPoints[0]), tuple(sortedPoints[2]), (0, 255, 0), thickness=3, lineType=8)
    #
    #     ####Draw on output image
    #     # Draw bottom line, 180 cm
    #     cv2.line(output, tuple(sortedPoints[1]), tuple(sortedPoints[3]), (0, 255, 0), thickness=3, lineType=8)
    #     # # Draw left line, 120 cm
    #     cv2.line(output, tuple(sortedPoints[0]), tuple(sortedPoints[1]), (0, 255, 0), thickness=3, lineType=8)
    #     # # Draw right line, 120 cm
    #     cv2.line(output, tuple(sortedPoints[2]), tuple(sortedPoints[3]), (0, 255, 0), thickness=3, lineType=8)
    #     # # Draw top line, 180 cm
    #     cv2.line(output, tuple(sortedPoints[0]), tuple(sortedPoints[2]), (0, 255, 0), thickness=3, lineType=8)


