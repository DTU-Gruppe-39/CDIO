import time

import math
import numpy as np
import imutils
import cv2
from imutils import contours

def nothing(x): # for trackbar
    pass


#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture("/home/soren/Downloads/RobotWithMarkings.mov")
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
        ([180, 0, 0], [255, 190, 50])
        # ([0, 150, 0], [150, 255, 150]) #Bander red
        # ([86, 0, 0], [255, 0, 0])
    ]
    boundaries1 = [
        ([70, 0, 100], [255, 20, 255])
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


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(mask, 1, 2, cv2.THRESH_BINARY)[1]

    for (lower, upper) in boundaries1:
        # create NumPy arrays from the boundaries
        lower1 = np.array(lower, dtype="uint8")
        upper1 = np.array(upper, dtype="uint8")

        mask1 = cv2.inRange(frame, lower1, upper1)
        output += cv2.bitwise_and(frame, frame, mask=mask1)


        gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
   #     thresh1 = cv2.threshold(mask1, 0, 0, cv2.THRESH_BINARY)[1]

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



                # Robot box rotation
                contours, _ = cv2.findContours(mask1, 1, 1)
                max_area = 0
                best_cnt = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > max_area:
                        max_area = area
                        best_cnt = cnt

                rect = cv2.minAreaRect(best_cnt)
                cv2.circle(frame, (x + 10, y + 10), 5, (255, 255, 255), 1)
                cv2.putText(frame, "Robo bot", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                #print(rect)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
               # print(rect)

                #box[0][0] -= 50
                #box[0][1] += 50
                #box[1][0] -= 50
                #box[1][1] -= 50
                #box[2][0] += 50
                #box[2][1] -= 50
                #box[3][0] += 50
                #box[3][1] += 50

              #  print(box)
                cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)


                dist = math.sqrt(pow(i[0] - x, 2) + pow(i[1] - y, 2))

               # print(minDist)
                if (minDist == 0):
                    minDist = dist
                elif (dist < minDist):
                    minDist = dist
                    cirX = i[0]
                    cirY = i[1]
                   # print(minDist)
                   # print((i[0], i[1]))

                  #  cv2.line(frame, (x, y), (i[0], i[1]), (0, 0, 255), 1)
        #print((cirx,ciry, x,y))
                    cv2.line(frame, (x, y), (cirX, cirY), (0, 0, 255), 1)

        print("\n")
    # show the images
    cv2.imshow("images", np.hstack([rect1, output]))

    # Display the resulting frame
    #cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()









