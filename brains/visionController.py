import numpy as np
import cv2

import brains.corners.getTrack
from model import ball
from model import track
from model import obstacle
from view import visionOutputView

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 24)


def captureVideo():
    # Capture frame-by-frame
    ret, frame = cap.read()

    return frame


class VisionController:
    track = track.Track
    obstacle = obstacle.Obstacle
    balls = [ball.Ball]
    robot = None

    while True:
        img = captureVideo()

        visionOutputView.showImage(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # balls = getBalls(img)

        track = brains.corners.getTrack(img)

        print(str("Test: " + track.bottomRightCorner))

        # obstacle = getObstacle(img)

        # robot = getRobot(img)




cap.release()
cv2.destroyAllWindows()






