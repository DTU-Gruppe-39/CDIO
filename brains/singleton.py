from model import ball
from model import boundary
from model import corner
from model import obstacle
from model import point
from model import track


class Singleton:

    balls = [ball.Ball]
    track = track.Track
    obstacle = obstacle.Obstacle


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






