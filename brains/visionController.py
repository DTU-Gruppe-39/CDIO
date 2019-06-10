import numpy as np
import cv2

from brains.detectTrack import getTrack
from model import ball
from model import Track
from model import obstacle
from view import visionOutputView

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 30)


def captureVideo():
    # Capture frame-by-frame
    ret, frame = cap.read()

    return frame


class VisionController:
    track = Track.Track
    obstacle = obstacle.Obstacle
    balls = [ball.Ball]
    robot = None

    while True:
        img = captureVideo()



        # balls = getBalls(img)

        track = getTrack(img)

        # test print
        print("BottomRight: " + str(track.bottomRightCorner.x) + " " + str(track.bottomRightCorner.y))
        print("BottomLeft: " + str(track.bottomLeftCorner.x) + " " + str(track.bottomLeftCorner.y))
        print("TopRight: " + str(track.topRightCorner.x) + " " + str(track.topRightCorner.y))
        print("TopLeft: " + str(track.topLeftCorner.x) + " " + str(track.topLeftCorner.y))

        print("Lille mål x: " + str(track.smallGoal.x))
        print("Lille mål y: " + str(track.smallGoal.y))

        print("Stort mål x: " + str(track.bigGoal.x))
        print("Stort mål y: " + str(track.bigGoal.y))


        # obstacle = getObstacle(img)

        # robot = getRobot(img)

        cv2.imshow("images", np.hstack([img]))

        # visionOutputView.showImage(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()






