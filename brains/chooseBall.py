import math
import brains.singleton as singleton
from model.ball import Ball
from brains import waypoint


def getChosenBall():
    return singleton.Singleton.chosenBall


def getWaypoints():
    way_points = []
    if singleton.Singleton.chosenBall is not None:
        way_points = waypoint.waypoints(singleton.Singleton.chosenBall)
        return way_points
    else:
        return None

def setChosenBall(ball):
    singleton.Singleton.chosenBall = ball


def findBestBall(balls):
    robot = singleton.Singleton.robot
    track = singleton.Singleton.track

    minDist = 0
    dist = 0
    maxNumberOfTries = 5
    numberOfBallsLeft = len(singleton.Singleton.balls)
    danger = track.pixelConversion * 5
    cornerSafePointX = track.pixelConversion * 3
    cornerSafePointY = track.pixelConversion * 12
    sideSafePoint = track.pixelConversion * 7
    tempBall = Ball

    cirX = None
    cirY = None


    print("Choose ball")
    # return ball
    if numberOfBallsLeft == 0:
        return None
    # elif numberOfTries >= maxNumberOfTries:
    #     numberOfTries = 0
    #     tempBall = balls[0]
    #     # setChosenBall(balls[0])
    #     return tempBall
    else:
        for ball in balls:
            dist = math.sqrt(pow(robot.centrumX - ball.x, 2) + pow(robot.centrumY - ball.y, 2))

            if minDist == 0:
                minDist = dist
                # print("MinDist: " + str(minDist/track.pixelConversion))
                cirX = ball.x
                cirY = ball.y
                tempBall.x = ball.x
                tempBall.y = ball.y

            elif dist < minDist:
                minDist = dist
                cirX = ball.x
                cirY = ball.y

                tempBall.x = ball.x
                tempBall.y = ball.y

                # tempBall.x = cirX
                # tempBall.y = cirY

            #     print("circ: " + str(cirX) + ", " + str(cirY))
            # print("minDist: " + str(minDist), "Dist: " + str(dist))


        return tempBall
