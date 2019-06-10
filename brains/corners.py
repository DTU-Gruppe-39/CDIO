import cv2
import imutils
import numpy as np
from model import track


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


def calculateGoals(track):
    print("not implemented")


def getTrack(frame):

    tempTrack = track.Track

    corner_boundaries = [
        ([60, 40, 40], [86, 255, 255]),
        # ([86, 0, 0], [255, 0, 0])
    ]

    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    points = []

    # loop over the boundaries
    for (clower, cupper) in corner_boundaries:
        # create NumPy arrays from the boundaries
        clower = np.array(clower, dtype="uint8")
        cupper = np.array(cupper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        cmask = cv2.inRange(hsv, clower, cupper)
        # coutput = cv2.bitwise_and(hsv, hsv, mask=cmask)

    # find contours in the thresholded image
    cnts = cv2.findContours(cmask.copy(), cv2.RETR_EXTERNAL,
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
        sortedPoints= sort(points)

        tempTrack.topLeftCorner = sortedPoints[0]
        tempTrack.bottomLeftCorner = sortedPoints[1]
        tempTrack.topRightCorner = sortedPoints[2]
        tempTrack.bottomRightCorner = sortedPoints[3]


        print(sortedPoints)

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


