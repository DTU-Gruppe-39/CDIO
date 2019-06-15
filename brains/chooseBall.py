import math
import brains.singleton as singleton


def getChosenBall(balls, numberOfTries):
    robot = singleton.Singleton.robot
    track = singleton.Singleton.track

    minDist = 0
    maxNumberOfTries = 5
    numberOfBallsLeft = len(singleton.Singleton.balls)
    danger = track.pixelConversion * 5
    cornerSafePointX = track.pixelConversion * 3
    cornerSafePointY = track.pixelConversion * 12
    sideSafePoint = track.pixelConversion * 7

    print("Choose ball")
    # return ball
    if numberOfBallsLeft == 0:
        return None
    elif robot.numberOfTries >= maxNumberOfTries:
        robot.numberOfTries = 0
        chosenBall = balls[0]
        return chosenBall
    else:
        for ball in balls:
            dist = math.sqrt(pow(robot.centrumY - ball[0], 2) + pow(robot.centrumY - ball[0], 2))

            if (minDist == 0):
                minDist = dist
            elif (dist < minDist):
                minDist = dist
                cirX = ball[0]
                cirY = ball[1]

            chosenBall = (cirX, cirY)

            # If it is a easy ball outside dangerzone
            if cirX > track.bottomLeftCorner.x + danger and cirX < track.bottomRightCorner.x - track.pixelConversion * 5 and cirY > track.bottomRightCorner.y + track.pixelConversion * 5 and cirY < track.topLeftCorner.y - track.pixelConversion * 5:
                return chosenBall
            # If ball is in top-left corner
            elif cirX < track.topLeftCorner.x + danger and cirY > track.topLeftCorner.y - danger:
                chosenBall = (cirX + cornerSafePointX, cirY - cornerSafePointY)

            # If ball is in bottom-left corner
            elif cirX < track.bottomLeftCorner.x + danger and cirY < track.bottomLeftCorner.y + danger:
                chosenBall = (cirX + cornerSafePointX, cirY + cornerSafePointY)

            # If ball is in top-right corner
            elif cirX > track.topRightCorner.x - danger and cirY > track.topRightCorner.y - danger:
                chosenBall = (cirX - cornerSafePointX, cirY - cornerSafePointY)

            # If ball is in bottom-right corner
            elif cirX > track.bottomRightCorner.x - danger and cirY < track.bottomRightCorner.y + danger:
                chosenBall = (cirX - cornerSafePointX, cirY + cornerSafePointY)

            # If ball is close to left side
            elif cirX < track.bottomLeftCorner.x + danger:
                chosenBall = (cirX + sideSafePoint, cirY)

            # If ball is close to right side
            elif cirX > track.bottomRightCorner.x - danger:
                chosenBall = (cirX - sideSafePoint, cirY)

            # If ball is close to bottom side
            elif cirY < track.bottomRightCorner.y + danger:
                chosenBall = (cirX, cirY + sideSafePoint)

            # If ball is close to top side
            elif cirY > track.topLeftCorner.x + danger:
                chosenBall = (cirX, cirY + sideSafePoint)


        return chosenBall
