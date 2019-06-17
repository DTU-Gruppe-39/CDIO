import numpy as np
import cv2
import copy

from brains.detectTrack import getTrack
from brains.detectBalls import getBalls
from brains.detectRobotBox import getRobot
from brains.detectObstacle import getObstacle
from brains.angle import getPointFromTwoLines
import brains.singleton as singleton

from model import ball
from model import track
from model import obstacle
from view import visionOutputView


while True:
    # obstacle = obstacle.Obstacle

    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('/Users/thomasmattsson/Google Drev/DTU/DTU - Studiegruppe/4. Semester/CDIO Lego/Test_Images/VideoOfRobot_2.mov')
    # cap = cv2.VideoCapture('/home/soren/Downloads/VideoOfRobot_2.mov')

    cap.set(cv2.CAP_PROP_FPS, 30)
    # while True:
    ret, img = cap.read()
    singleton.Singleton.img = copy.deepcopy(img)

    singleton.Singleton.balls = getBalls(copy.deepcopy(img))
    singleton.Singleton.robot = getRobot(copy.deepcopy(img))
    singleton.Singleton.track = getTrack(copy.deepcopy(img))
    singleton.Singleton.obstacle = getObstacle(copy.deepcopy(img))

    robot = singleton.Singleton.robot
    track = singleton.Singleton.track
    obstacle = singleton.Singleton.obstacle

    # point = getPointFromTwoLines([robot.centrumX, robot.centrumY], [robot.blSquareX, robot.blSquareY],
    #                      [track.topLeftCorner.x, track.topLeftCorner.y], [track.topRightCorner.x, track.topRightCorner.y])

    point = getPointFromTwoLines((robot.centrumX, robot.centrumY),
                                 (obstacle.x, obstacle.y),
                                 (track.topLeftCorner.x, track.topLeftCorner.y),
                                 (track.bottomRightCorner.x, track.bottomRightCorner.y))

    print("Intersection: " + str(point.x) + ", " + str(point.y))

    print("visionController: PixelConversion is " + str(singleton.Singleton.track.pixelConversion))

    getObstacle(copy.deepcopy(img))

    # robot = getRobot(img)

    print("visionController: BottomRightCoord is " + str(singleton.Singleton.track.bottomRightCorner.x) + " " + str(singleton.Singleton.track.bottomRightCorner.y))




    # cv2.imshow("images", np.hstack([img]))

    # visionOutputView.showImage(img, singleton.Singleton.track, singleton.Singleton.balls, singleton.Singleton.robot)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()