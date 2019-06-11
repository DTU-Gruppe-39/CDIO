import numpy as np
import cv2

from brains.detectTrack import getTrack
from brains.detectBalls import getBalls
from model import ball
from model import track
from model import obstacle
from view import visionOutputView


class VisionController:
    track = track.Track
    obstacle = obstacle.Obstacle
    ball = ball.Ball
    balls = []
    robot = None

    cap = cv2.VideoCapture(1)
    # cap = cv2.VideoCapture('/Users/thomasmattsson/Documents/GitHub/CDIO/Test_images/MovieWithMovingRobotAndBalls.mov')

    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
        ret, img = cap.read()

        balls = getBalls(img)

        track = getTrack(img)

        # if len(balls) is not 0:
        #     print(str(balls[0].x))
        # test print
        # print("BottomRight: " + str(track.bottomRightCorner.x) + " " + str(track.bottomRightCorner.y))
        # print("BottomLeft: " + str(track.bottomLeftCorner.x) + " " + str(track.bottomLeftCorner.y))
        # print("TopRight: " + str(track.topRightCorner.x) + " " + str(track.topRightCorner.y))
        # print("TopLeft: " + str(track.topLeftCorner.x) + " " + str(track.topLeftCorner.y))
        #
        # print("Lille mål x: " + str(track.smallGoal.x))
        # print("Lille mål y: " + str(track.smallGoal.y))
        #
        # print("Stort mål x: " + str(track.bigGoal.x))
        # print("Stort mål y: " + str(track.bigGoal.y))


        # obstacle = getObstacle(img)

        # robot = getRobot(img)

        # cv2.imshow("images", np.hstack([img]))

        visionOutputView.showImage(img, track, balls)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()






