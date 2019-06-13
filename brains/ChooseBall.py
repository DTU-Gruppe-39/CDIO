import math
import brains.singleton as singleton


def getChosenBall(balls):
    robot = singleton.Singleton.robot
    track = singleton.Singleton.track

    destBall = (0, 0)
    minDist = 0

    for ball in balls:
        if ball[0] > track.bottomLeftCorner.x + 40  and ball[0] < track.bottomRightCorner.x - 40:
            if ball[1] > track.bottomRightCorner.y + 40 and ball[1] > track.topLeftCorner.y - 40:

                # Smallest distance from robot to ball
                dist = math.sqrt(pow(robot.centrumY - ball[0], 2) + pow(robot.centrumY - ball[0], 2))

                if (minDist == 0):
                    minDist = dist
                elif (dist < minDist):
                    minDist = dist
                    cirX = ball[0]
                    cirY = ball[1]

            destBall = (cirX, cirY)

    return destBall
