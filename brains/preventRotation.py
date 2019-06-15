from brains.singleton import Singleton

def preventRotation():
    robot = Singleton.robot
    track = Singleton.track

    if robot.centrumX < track.bottomLeftCorner.x + track.pixelConversion * 25:
        return True
    elif robot.centrumX > track.bottomRightCorner.x - track.pixelConversion * 25:
        return True
    elif robot.centrumY < track.bottomRightCorner.y + track.pixelConversion * 25:
        return True
    elif robot.centrumY > track.topLeftCorner.y - track.pixelConversion * 25:
        return True
    else:
        return False
