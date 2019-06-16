import model
from model import ball
# import model.ball as ball
from model import boundary
from model import corner
from model import obstacle
from model import point
from model import track
from model import robot
from model import ball

class Singleton:

    balls = [ball.Ball]
    track = track.Track
    obstacle = obstacle.Obstacle
    robot = robot.Robot
    way_points = []
    is_dangerous = False
    clockWise = False
    img = None

    chosenBall = None


    __instance = None
    @staticmethod

    def getInstance():
       """ Static access method. """
       if Singleton.__instance == None:
          Singleton()
       return Singleton.__instance

    def __init__(self):
       """ Virtually private constructor. """
       if Singleton.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          Singleton.__instance = self


    # Getters and setters

    # def getBalls(self):
    #     return self.balls
    #
    # def setBalls(self, balls):
    #     self.balls = balls
    #
    # def getTrack(self):
    #     return self.track
    #
    # def setTrack(self, track):
    #     self.track = track
    #
    # def getObstacle(self):
    #     return self.obstacle
    #
    # def setObstacle(self, obstacle):
    #     self.obstacle = obstacle

    # def getRobot(self):
    #    return self.robot

    # def setRobot(self, robot):
    #    self.robot = robot





