from model import ball
import cv2
import numpy as np


def getBalls(img):
    tempBall = []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=500, param2=26, minRadius=1, maxRadius=20)
    # print(circles)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        tempBall = []
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            # cv2.circle(img, center, 1, (0, 100, 100), 5)
            # # circle outline
            # radius = i[2]
            # cv2.circle(img, center, radius, (255, 0, 255), 3)
            singleBall = ball.Ball(i[0], i[1], i[2])
            print(str("Balls: " + str(singleBall.x)))

            tempBall.append(singleBall)
            print(str("balls: " + str(tempBall[0].x)))

    return tempBall