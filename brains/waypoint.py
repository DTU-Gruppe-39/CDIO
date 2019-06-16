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
danger = track.pixelConversion * 5
cornerSafePointX = track.pixelConversion * 15
cornerSafePointY = track.pixelConversion * 30
sideSafePoint = track.pixelConversion * 15
tempBall = Ball
waypoint_list = []


def waypoints(endPoint):
    # If it is a easy ball outside dangerzone
    if endPoint.x > track.bottomLeftCorner.x + danger and endPoint.x < track.bottomRightCorner.x - track.pixelConversion * 5 and \
    endPoint.y > track.bottomRightCorner.y + track.pixelConversion * 5 \
    and endPoint.y < track.topLeftCorner.y - track.pixelConversion * 5:
        print("Koordinat udregning nr. : " + str(1))
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in top-left corner
    elif endPoint.x < track.topLeftCorner.x + danger and endPoint.y > track.topLeftCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y - cornerSafePointY))
        print("Koordinat udregning nr. : " + str(2))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in bottom-left corner
    elif endPoint.x < track.bottomLeftCorner.x + danger and endPoint.y < track.bottomLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Koordinat udregning nr. : " + str(3))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in top-right corner
    elif endPoint.x > track.topRightCorner.x - danger and endPoint.y > track.topRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Koordinat udregning nr. : " + str(4))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is in bottom-right corner
    elif endPoint.x > track.bottomRightCorner.x - danger and endPoint.y < track.bottomRightCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Koordinat udregning nr. : " + str(4))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to left side
    elif endPoint.x < track.bottomLeftCorner.x + danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y ))
        print("Koordinat udregning nr. : " + str(5))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to right side
    elif endPoint.x > track.bottomRightCorner.x - danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y))
        print("Koordinat udregning nr. : " + str(6))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to bottom side
    elif endPoint.y < track.bottomRightCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x), round(endPoint.y + cornerSafePointY))
        endPoint.x = int(endPoint.x)
        endPoint.y = int(endPoint.y + sideSafePoint)
        print("Koordinat udregning nr. : " + str(7))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list

    # If ball is close to top side
    elif endPoint.y > track.topLeftCorner.x + danger:
        last_waypoint = point.Point(round(endPoint.x), round(endPoint.y - cornerSafePointY))
        print("Koordinat udregning nr. : " + str(8))
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        return waypoint_list
