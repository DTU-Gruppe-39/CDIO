

import cv2

import numpy as np
from scipy.spatial import distance as dist
import math
from imutils import perspective
from imutils import contours
import argparse
import imutils
# define CV_PI 3.1415926535897932384626433832795
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FPS, 80)
cap = cv2.imread('image4.jpg')

# Capture frame-by-frame
# ret, frame = cap.read()

# Our operations on the frame come here
gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
rows = gray.shape[1]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 14, param1=150, param2=14, minRadius=1, maxRadius=20)
ret, thresh = cv2.threshold(gray, 127, 255, 1)
contours, h = cv2.findContours(thresh, 1, 2)

gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def calculateAngle(px1, py1, px2, py2, px3, py3):

    numerator = py2 * (px1 - px3) + py1 * (px3 - px2) + py3 * (px2 - px1)
    denominator = (px2 - px1) * (px1 - px3) + (py2 - py1) * (py1 - py3)
    ratio = numerator / denominator

    angleRad = math.atan(ratio)
    angleDeg = (angleRad * 180) / math.pi

    if angleDeg < 0:
        angleDeg = 180 + angleDeg

    return int(angleDeg)


x1 = circles[0][0][0]
y1 = circles[0][0][1]
x2 = circles[0][1][0]
y2 = circles[0][1][1]
x3 = circles[0][2][0]
y3 = circles[0][2][1]
x4 = circles[0][3][0]
y4 = circles[0][3][1]
x5 = circles[0][4][0]
y5 = circles[0][4][1]
x6 = circles[0][5][0]
y6 = circles[0][5][1]
x7 = circles[0][6][0]
y7 = circles[0][6][1]
x8 = circles[0][7][0]
y8 = circles[0][7][1]
x9 = circles[0][8][0]
y9 = circles[0][8][1]

c1 = (x1, y1)
c2 = (x2, y2)
c3 = (x3, y3)
c4 = (x4, y4)
c5 = (x5, y5)
c6 = (x6, y6)
c7 = (x7, y7)
c8 = (x8, y8)
c9 = (x9, y9)
print('circle 1: ', c1)
print('circle 2: ', c2)
print('circle 3: ', c3)
print('circle 4: ', c4)
print('circle 5: ', c5)
print('circle 6: ', c6)
print('circle 7: ', c7)
print('circle 8: ', c8)
print('circle 9: ', c9)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)

        # a square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        print(shape)
        print(x)
if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:

            center = (i[0], i[1])
            # circle center
            cv2.circle(gray, center, 1, (0, 100, 100), 5)
            # circle outline
            radius = i[2]

            cv2.circle(gray, center, radius, (0, 0, 0), 3)
            line1_2 = cv2.arrowedLine(gray, c1, c2, (255, 0, 0), 2)
            line2_3 = cv2.arrowedLine(gray, c2, c3, (255, 0, 0), 2)
            line3_4 = cv2.arrowedLine(gray, c3, c4, (255, 0, 0), 2)
            line4_5 = cv2.arrowedLine(gray, c4, c5, (255, 0, 0), 2)
            line5_6 = cv2.arrowedLine(gray, c5, c6, (255, 0, 0), 2)
            line6_7 = cv2.arrowedLine(gray, c6, c7, (255, 0, 0), 2)
            line7_8 = cv2.arrowedLine(gray, c7, c8, (255, 0, 0), 2)
            line8_9 = cv2.arrowedLine(gray, c8, c9, (255, 0, 0), 2)

            D1 = dist.euclidean(c1, c2)
            D2 = dist.euclidean(c2, c3)
            D3 = dist.euclidean(c3, c4)
            D4 = dist.euclidean(c4, c5)
            D5 = dist.euclidean(c5, c6)
            D6 = dist.euclidean(c7, c6)
            D7 = dist.euclidean(c8, c7)
            D8 = dist.euclidean(c8, c9)

            # D5 = dist.euclidean((x1, y1), (x2, y2))
            #(mX, mY) = midpoint((x1, y1), (x2, y2))
            cv2.putText(gray, "c1 -> c2 :{:.1f}in".format(D1), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c2 -> c3 :{:.1f}in".format(D2), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c3 -> c4 :{:.1f}in".format(D3), (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c4 -> c5 :{:.1f}in".format(D4), (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c5 -> c6 :{:.1f}in".format(D5), (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c6 -> c7 :{:.1f}in".format(D6), (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c7 -> c8 :{:.1f}in".format(D7), (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            cv2.putText(gray, "c8 -> c9 :{:.1f}in".format(D8), (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)

            cv2.putText(gray, "c1", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c2", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c3", (x3, y3), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c4", (x4, y4), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c5", (x5, y5), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c6", (x6, y6), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c7", (x7, y7), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c8", (x8, y8), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c9", (x9, y9), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)




            # cv2.putText(gray, '%d', angle1, float(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
            # print("x, y :", center)
            # print("radius :", radius)
            # print(len(circles))

angle1 = calculateAngle(x2, y2, x1, y1, x3, y3)
angle2 = calculateAngle(x3, y3, x2, y2, x4, y4)
angle3 = calculateAngle(x4, y4, x3, y3, x5, y5)
angle4 = calculateAngle(x5, y5, x4, y4, x6, y6)
angle5 = calculateAngle(x6, y6, x5, y5, x7, y7)
angle6 = calculateAngle(x7, y7, x6, y6, x8, y8)
angle7 = calculateAngle(x8, y8, x7, y7, x9, y9)

cv2.putText(gray, "c2: {} deg".format(angle1), (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c3: {} deg".format(angle2), (20, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c4: {} deg".format(angle3), (20, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c5: {} deg".format(angle4), (20, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c6: {} deg".format(angle5), (20, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c7: {} deg".format(angle6), (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c8: {} deg".format(angle7), (20, 320), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
print('angle c2:', angle1)
print('angle c3:', angle2)
print('angle c4:', angle3)
print('angle c5:', angle4)
print('angle c6:', angle5)
print('angle c7:', angle6)

# Display the resulting frame
# print("x, y :", center)
cv2.imshow('frame', gray)
# print("radius :", radius)
# print(len(circles))
cv2.waitKey(0)
# When everything done, release the capture
# cap.release()
cv2.destroyAllWindows()









