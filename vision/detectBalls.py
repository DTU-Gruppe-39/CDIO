from model import ball
import cv2
import numpy as np
from brains import correction
from model import point

tempBall = []
def getBalls(img):
    global tempBall
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=500, param2=16, minRadius=1, maxRadius=20)
    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=550, param2=17, minRadius=5, maxRadius=8)
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
            x_val = np.amax(img, axis=0)
            y_val = np.amax(img, axis=1)
            x_val = round(len(x_val) / 2)
            y_val = round(len(y_val) / 2)
            camera_center = point.Point(x_val, y_val)
            corrected_ball_center = correction.ball_cen_correction(camera_center, singleBall)
            singleBall.x = int(corrected_ball_center.x)
            singleBall.y = int(corrected_ball_center.y)
            # print("correctedball_X: " + str(corrected_ball_center.x))
            # print("correctedball_Y: " + str(corrected_ball_center.y))
            tempBall.append(singleBall)
    else:
        tempBall.clear()
        return tempBall

    return tempBall