import numpy as np
import cv2
from model import ball
from model import corner
from model import obstacle

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 24)


def captureVideo():
    # Capture frame-by-frame
    ret, frame = cap.read()

    return frame


class VisionController:
    corners = [corner.Corner]
    obstacle = obstacle.Obstacle
    balls = [ball.Ball]

    while True:
        img = captureVideo()

        # balls = getBalls(img):

        # corners = getCorners(img):

        # obstacle = getObstacle(img):

        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()






