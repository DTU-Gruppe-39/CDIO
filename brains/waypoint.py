import math
import brains.singleton as singleton
from model.ball import Ball
from model import point

robot = singleton.Singleton.robot
track = singleton.Singleton.track

minDist = 0
dist = 0
maxNumberOfTries = 5
numberOfBallsLeft = len(singleton.Singleton.balls)
danger = track.pixelConversion * 15
cornerSafePointX = track.pixelConversion * 15
cornerSafePointY = track.pixelConversion * 30
sideSafePoint = track.pixelConversion * 15
tempBall = Ball
waypoint_list = []

# Should use the center of the robot instead of the yellow square. So it can lineup properly
def waypoints(endPoint):
    # If it is a easy ball outside dangerzone
    if endPoint.x > track.bottomLeftCorner.x + danger and endPoint.x < track.bottomRightCorner.x - track.pixelConversion * 5 and \
    endPoint.y > track.bottomRightCorner.y + track.pixelConversion * 5 \
    and endPoint.y < track.topLeftCorner.y - track.pixelConversion * 5:
        print("Ball is an easy ball")
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in top-left corner
    elif endPoint.x < track.topLeftCorner.x + danger and endPoint.y < track.topLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Ball is in top left corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in bottom-left corner
    elif endPoint.x < track.bottomLeftCorner.x + danger and endPoint.y > track.bottomLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y - cornerSafePointY))
        print("Ball is in bottom left corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in top-right corner
    elif endPoint.x > track.topRightCorner.x - danger and endPoint.y > track.topRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Ball is in top right corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in bottom-right corner
    elif endPoint.x > track.bottomRightCorner.x - danger and endPoint.y > track.bottomRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y - cornerSafePointY))
        print("Ball is in bottom right corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to left side
    elif endPoint.x < track.bottomLeftCorner.x + danger:
        last_waypoint = point.Point(round(endPoint.x + sideSafePoint), round(endPoint.y ))
        print("Ball is close to left side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to right side
    elif endPoint.x > track.bottomRightCorner.x - danger:
        last_waypoint = point.Point(round(endPoint.x - sideSafePoint), round(endPoint.y))
        print("Ball is close to right side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to bottom side
    elif endPoint.y > track.bottomRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x), round(endPoint.y - sideSafePoint))
        print("Ball is close to bottom side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to top side
    elif endPoint.y < track.topLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x), round(endPoint.y + sideSafePoint))
        print("Ball is close to top side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list
    test = point.Point(666, 666)
    waypoint_list.append(test)
