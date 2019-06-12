import cv2
import numpy as np
import math

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FPS, 80)
cap = cv2.imread('(3).jpg')
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


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    if ang < 0:
        ang = ang + 180
    if a[0] < b[0] and a[1] > c[1] or a[1] < c[1] and a[0] > b[0]:
            ang = 180 - ang

    return ang


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

            cv2.putText(gray, "c1", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c2", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c3", (x3, y3), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c4", (x4, y4), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c5", (x5, y5), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c6", (x6, y6), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c7", (x7, y7), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c8", (x8, y8), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
            cv2.putText(gray, "c9", (x9, y9), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)


angle1 = getAngle(c1, c2, c3)
angle2 = getAngle(c2, c3, c4)
angle3 = getAngle(c3, c4, c5)
angle4 = getAngle(c4, c5, c6)
angle5 = getAngle(c5, c6, c7)
angle6 = getAngle(c6, c7, c8)
angle7 = getAngle(c7, c8, c9)

cv2.putText(gray, "c2: {} deg".format(angle1), (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c3: {} deg".format(angle2), (20, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c4: {} deg".format(angle3), (20, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c5: {} deg".format(angle4), (20, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c6: {} deg".format(angle5), (20, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c7: {} deg".format(angle6), (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)
cv2.putText(gray, "c8: {} deg".format(angle7), (20, 320), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 1)

# Display the resulting frame

cv2.imshow('frame', gray)
cv2.waitKey(0)
# cap.release()
cv2.destroyAllWindows()