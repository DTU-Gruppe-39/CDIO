import math
import brains.singleton as singleton


def getChosenBall(balls, numberOfTries):
    robot = singleton.Singleton.robot
    track = singleton.Singleton.track

    destBall = (0, 0)
    minDist = 0
    maxNumberOfTries = 5
    numberOfBallsLeft = len(singleton.Singleton.balls)

    print("Choose ball")
    # return ball
    if numberOfBallsLeft == 0:
        return None
    elif numberOfTries >= maxNumberOfTries:
        numberOfTries = 0
        chosenBall = balls[0]
        return chosenBall
    else:
        for ball in balls:
            if ball[0] > track.bottomLeftCorner.x + track.pixelConversion*5  and ball[0] < track.bottomRightCorner.x - track.pixelConversion*5:
                if ball[1] > track.bottomRightCorner.y + track.pixelConversion*5 and ball[1] > track.topLeftCorner.y - track.pixelConversion*5:

                    # Smallest distance from robot to ball
                    dist = math.sqrt(pow(robot.centrumY - ball[0], 2) + pow(robot.centrumY - ball[0], 2))

                    if (minDist == 0):
                        minDist = dist
                    elif (dist < minDist):
                        minDist = dist
                        cirX = ball[0]
                        cirY = ball[1]

                chosenBall = (cirX, cirY)

        return chosenBall




