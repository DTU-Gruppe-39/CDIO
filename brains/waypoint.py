import math
import brains.singleton as singleton
from model.ball import Ball
from model import point


def pop_waypoint():
    singleton.Singleton.way_points.pop(0)


def get_waypoint():
    return singleton.Singleton.way_points


def waypoints(endPoint):
    track = singleton.Singleton.track
    danger = round(track.pixelConversion * 15)
    cornerSafePointX = round(track.pixelConversion * 32)
    cornerSafePointY = round(track.pixelConversion * 47)
    sideSafePoint = round(track.pixelConversion * 32)
    waypoint_list = []
    # If it is a easy ball outside dangerzone
    if endPoint.x > track.bottomLeftCorner.x + danger and endPoint.x < track.bottomRightCorner.x - track.pixelConversion * 5 and endPoint.y > track.bottomRightCorner.y + track.pixelConversion * 5 \
    and endPoint.y < track.topLeftCorner.y - track.pixelConversion * 5:
        print("Ball is an easy ball")
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = False
        return

    # If ball is in top-left corner
    elif endPoint.x < track.topLeftCorner.x + danger and endPoint.y < track.topLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Ball is in top left corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is in bottom-left corner
    elif endPoint.x < track.bottomLeftCorner.x + danger and endPoint.y > track.bottomLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y - cornerSafePointY))
        print("Ball is in bottom left corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is in top-right corner
    elif endPoint.x > track.topRightCorner.x - danger and endPoint.y > track.topRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y + cornerSafePointY))
        print("Ball is in top right corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is in bottom-right corner
    elif endPoint.x > track.bottomRightCorner.x - danger and endPoint.y > track.bottomRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y - cornerSafePointY))
        print("Ball is in bottom right corner")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is close to left side
    elif endPoint.x < track.bottomLeftCorner.x + danger:
        last_waypoint = point.Point(round(endPoint.x + sideSafePoint), round(endPoint.y ))
        print("Ball is close to left side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is close to right side
    elif endPoint.x > track.bottomRightCorner.x - danger:
        last_waypoint = point.Point(round(endPoint.x - sideSafePoint), round(endPoint.y))
        print("Ball is close to right side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is close to bottom side
    elif endPoint.y > track.bottomRightCorner.y - danger:
        last_waypoint = point.Point(round(endPoint.x), round(endPoint.y - sideSafePoint))
        print("Ball is close to bottom side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return

    # If ball is close to top side
    elif endPoint.y < track.topLeftCorner.y + danger:
        last_waypoint = point.Point(round(endPoint.x), round(endPoint.y + sideSafePoint))
        print("Ball is close to top side")
        waypoint_list.append(last_waypoint)
        waypoint_list.append(point.Point(endPoint.x, endPoint.y))
        singleton.Singleton.way_points = waypoint_list
        singleton.Singleton.danger_pos = True
        return
    test = point.Point(0, 0)
    waypoint_list.append(test)
    singleton.Singleton.way_points = waypoint_list
    return
