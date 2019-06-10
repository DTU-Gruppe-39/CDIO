import numpy as np
import cv2

from brains.detectTrack import getTrack
from model import ball
from model import track
from model import obstacle
from view import visionOutputView

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 30)


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



        # balls = getBalls(img)

        track = getTrack(img)

        print("Test: " + str(track.bottomRightCorner.x))
        print("Test: " + str(track.bottomRightCorner.y))

        # obstacle = getObstacle(img)

        # robot = getRobot(img)

        cv2.imshow("images", np.hstack([img]))

        # visionOutputView.showImage(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()






