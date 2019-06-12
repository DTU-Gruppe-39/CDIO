import time

import math
import numpy as np
import imutils
import cv2
from imutils import contours

def nothing(x): # for trackbar
    pass

def calculateAngle(px1, py1, px2, py2, px3, py3):

    numerator = py2 * (px1 - px3) + py1 * (px3 - px2) + py3 * (px2 - px1)
    denominator = (px2 - px1) * (px1 - px3) + (py2 - py1) * (py1 - py3)
    ratio = numerator / denominator

    angleRad = math.atan(ratio)
    angleDeg = (angleRad * 180) / math.pi

    if angleDeg < 0:
        angleDeg = 180 + angleDeg

    return int(angleDeg)

cap = cv2.VideoCapture('/home/soren/Downloads/VideoOfRobot_2_Trim.mov')
#cap = cv2.VideoCapture("VideoOfRobot_2_Trim.mp4")
cap.set(cv2.CAP_PROP_FPS, 24)
cv2.namedWindow("test")
minDist = 0


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
#    frame = cv2.imread("../Test_images/ImageOfRobot8.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=550, param2=17, minRadius=5, maxRadius=8)


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]



    boundaries = [
        # ([119, 182, 143], [136, 199, 169]),
        #([0, 230, 230], [130, 255, 255])  # Robot yellow
        ([170, 0, 0], [255, 190, 50])
        # ([0, 150, 0], [150, 255, 150]) #Bander red
        # ([86, 0, 0], [255, 0, 0])
    ]
    boundaries1 = [
        #([100, 90, 120], [205, 107, 255])
        ([105, 5, 100], [210, 90, 255])
       # ([30, 0, 100], [55, 50, 200])
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
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(mask, 1, 2, cv2.THRESH_BINARY)[1]

    for (lower, upper) in boundaries1:
        # create NumPy arrays from the boundaries
        lower1 = np.array(lower, dtype="uint8")
        upper1 = np.array(upper, dtype="uint8")

        mask1 = cv2.inRange(frame, lower1, upper1)
        output += cv2.bitwise_and(frame, frame, mask=mask1)


        gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # thresh1 = cv2.threshold(mask1, 0, 0, cv2.THRESH_BINARY)[1]

        minDist = 0
        x = 0
        y = 0
        cirX = 0
        cirY = 0

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(output, center, 1, (0, 100, 100), 5)

                # circle outline
                radius = i[2]
                cv2.circle(output, center, radius, (255, 0, 255), 2)

                # Bounding box of robot
                x, y, w, h = cv2.boundingRect(mask)
                rect1 = cv2.rectangle(frame.copy(), (x - 40, y - 35), (x + w + 35, y + h + 35), (255, 0, 0), 1)

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
                    x1 = circles[0][0][0]
                    y1 = circles[0][0][1]
                    c1 = (x1, y1)

                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        center = (cX, cY)
                    else:
                        # set values as what you need in the situation
                        cX, cY = 0, 0
                    #
                    # # draw the contour and center of the shape on the image

                    cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                    cv2.circle(frame, (cX, cY), 1, (0, 255, 255), 2)
                    #print(cont[1][0][0][0])
                    #cv2.line(frame, (cont[0][0][0][0], cont[0][0][0][1]), (cont[1][0][0][0], cont[1][0][0][1]), (0, 0, 255), 1)
                    cv2.line(frame, c1, (cont[0][0][0][0], cont[0][0][0][1]), (0, 0, 255), 1)
                    #cv2.line(frame, c1, (cont[0][0][0][1], cont[0][0][0][0]), (0, 255, 255), 1)
                    #angle = calculateAngle(x1, y1, cX, cY, cont[0][0][0][0], cont[0][0][0][1])
                    a = np.array([[cX, cY]])
                    b = np.array([x1, y1])
                    c = np.array([cont[0][0][0][0], cont[0][0][0][1]])

                    ba = a - b
                    bc = c - b

                    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                    angle = np.arccos(cosine_angle)

                    print(np.degrees(angle))

                # Center of robot
                M = cv2.moments(best_cnt)
                cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
                cv2.circle(frame, (cx, cy), 4, 255, -1)
                rect = cv2.minAreaRect(best_cnt)
                cv2.putText(frame, "Robo bot", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
                #cv2.line(frame, c1, (cx, cy), (0, 0, 255), 1)

                print(angle)
                # Rotating box
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
                #print(rect)
                #box[0][0] -= 50
                #box[0][1] += 50
                #box[1][0] -= 50
                #box[1][1] -= 50
                #box[2][0] += 50
                #box[2][1] -= 50
                #box[3][0] += 50
                #box[3][1] += 50

                cv2.circle(frame, (box[1][0], box[1][1]), 4, 255, -1)

                # Smallest distance from robot to ball
                dist = math.sqrt(pow(i[0] - x, 2) + pow(i[1] - y, 2))

               # print(minDist)
                if (minDist == 0):
                    minDist = dist
                elif (dist < minDist):
                    minDist = dist
                    cirX = i[0]
                    cirY = i[1]
                    #print(minDist)
                    cv2.line(frame, (cx, cy), (cirX, cirY), (0, 0, 255), 1)

        print("\n")
    # show the images
    cv2.imshow("images", np.hstack([frame, output]))

    # Display the resulting frame
    #cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()