import singleton


def preventRotation():
    robot = singleton.Singleton.robot
    track = singleton.Singleton.track

    if robot.blSquareX < track.bottomLeftCorner.x + track.pixelConversion * 32:
        return True
    elif robot.blSquareX > track.bottomRightCorner.x - track.pixelConversion * 32:
        return True
    elif robot.blSquareY < track.bottomRightCorner.y + track.pixelConversion * 32:
        return True
    elif robot.blSquareY > track.topLeftCorner.y - track.pixelConversion * 32:
        return True
    else:
        return False
