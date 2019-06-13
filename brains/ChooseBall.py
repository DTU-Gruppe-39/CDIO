import math
import brains.singleton as singleton


def getChosenBall(balls):
    singleton.Singleton.balls
    singleton.Singleton.robot

    destBall = (0, 0)
    minDist = 0
    for i, ball in balls:
        if i[0] > singleton.track.Track.bottomLeftCorner.x + 40  and i[0] < singleton.track.Track.bottomRightCorner.x - 40:
            if i[1] > singleton.track.Track.bottomRightCorner.y + 40 and i[1] > singleton.track.Track.topLeftCorner.y - 40:

                # Smallest distance from robot to ball
                dist = math.sqrt(pow(singleton.robot.Robot.centrumY - i[0], 2) + pow(singleton.robot.Robot.centrumY - i[0], 2))

                if (minDist == 0):
                    minDist = dist
                elif (dist < minDist):
                    minDist = dist
                    cirX = i[0]
                    cirY = i[1]
            destBall = (cirX, cirY)

    return destBall