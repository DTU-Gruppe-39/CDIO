import math
import brains.singleton as singleton
from model.ball import Ball
from brains import waypoint


def getChosenBall():
    ball = []
    ball = waypoint.waypoints(singleton.Singleton.chosenBall)
    return ball


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

        # # If it is a easy ball outside dangerzone
        # if cirX > track.bottomLeftCorner.x + danger and cirX < track.bottomRightCorner.x - track.pixelConversion * 5 and cirY > track.bottomRightCorner.y + track.pixelConversion * 5 and cirY < track.topLeftCorner.y - track.pixelConversion * 5:
        #     print("Koordinat udregning nr. : " + str(1))
        #     return chosenBall
        #
        # # If ball is in top-left corner
        # elif cirX < track.topLeftCorner.x + danger and cirY > track.topLeftCorner.y - danger:
        #     chosenBall.x = int(cirX + cornerSafePointX)
        #     chosenBall.y = int(cirY - cornerSafePointY)
        #     print("Koordinat udregning nr. : " + str(2))
        #
        #
        # # If ball is in bottom-left corner
        # elif cirX < track.bottomLeftCorner.x + danger and cirY < track.bottomLeftCorner.y + danger:
        #     chosenBall.x = int(cirX + cornerSafePointX)
        #     chosenBall.y = int(cirY - cornerSafePointY)
        #     print("Koordinat udregning nr. : " + str(3))
        #
        #
        # # If ball is in top-right corner
        # elif cirX > track.topRightCorner.x - danger and cirY > track.topRightCorner.y - danger:
        #     chosenBall.x = int(cirX - cornerSafePointX)
        #     chosenBall.y = int(cirY + cornerSafePointY)
        #     print("Koordinat udregning nr. : " + str(4))
        #
        #
        # # If ball is in bottom-right corner
        # elif cirX > track.bottomRightCorner.x - danger and cirY < track.bottomRightCorner.y + danger:
        #     chosenBall.x = int(cirX - cornerSafePointX)
        #     chosenBall.y = int(cirY + cornerSafePointY)
        #     print("Koordinat udregning nr. : " + str(4))
        #
        #
        # # If ball is close to left side
        # elif cirX < track.bottomLeftCorner.x + danger:
        #     chosenBall.x = int(cirX + sideSafePoint)
        #     chosenBall.y = int(cirY)
        #     print("Koordinat udregning nr. : " + str(5))
        #
        #
        # # If ball is close to right side
        # elif cirX > track.bottomRightCorner.x - danger:
        #     chosenBall.x = int(cirX - sideSafePoint)
        #     chosenBall.y = int(cirY)
        #     print("Koordinat udregning nr. : " + str(6))
        #
        #
        # # If ball is close to bottom side
        # elif cirY < track.bottomRightCorner.y + danger:
        #     chosenBall.x = int(cirX)
        #     chosenBall.y = int(cirY + sideSafePoint)
        #     print("Koordinat udregning nr. : " + str(7))
        #
        #
        # # If ball is close to top side
        # elif cirY > track.topLeftCorner.x + danger:
        #     chosenBall.x = int(cirX)
        #     chosenBall.y = int(cirY + sideSafePoint)
        #     print("Koordinat udregning nr. : " + str(8))

        return tempBall
