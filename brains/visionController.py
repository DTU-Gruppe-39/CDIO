import cv2
import copy

from vision.detectTrack import getTrack
from vision.detectBalls import getBalls
from vision.detectRobotBox import getRobot
from vision.detectObstacle import getObstacle
import brains.singleton as singleton
from view import visionOutputView


cap = None


def captureFrame():
    global cap
    # obstacle = obstacle.Obstacle
    robot = None

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
    
    print("visionController: PixelConversion is " + str(singleton.Singleton.track.pixelConversion))
    print("visionController: BottomRightCoord is " + str(singleton.Singleton.track.bottomRightCorner.x) + " " + str(singleton.Singleton.track.bottomRightCorner.y))

    visionOutputView.showImage()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


def releaseImage():
    global cap
    cap.release()
    cv2.destroyAllWindows()
