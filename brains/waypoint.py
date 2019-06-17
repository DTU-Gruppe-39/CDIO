import math
import brains.singleton as singleton
from model.ball import Ball
from brains.robotController import calc_pix_dist
from shapely.geometry import LineString
from brains import lines
from model import point


def pop_waypoint():
    singleton.Singleton.way_points.pop(0)


def get_waypoint():
    return singleton.Singleton.way_points

def waypoints(endPoint):
    minDist = 0
    closestToBall_index = 0
    track = singleton.Singleton.track
    danger = round(track.pixelConversion * 15)
    cornerSafePointX = round(track.pixelConversion * 5)
    cornerSafePointY = round(track.pixelConversion * 45)
    sideSafePoint = round(track.pixelConversion * 32)
    robot = singleton.Singleton.robot
    robot_center = (robot.centrumX, robot.centrumY)
    obstacle = singleton.Singleton.obstacle
    waypoint_list = []
    safe_points = singleton.Singleton.safe_points
    safe_point_dist_to_robot = []
    # If it is a easy ball outside dangerzone
    # if endPoint.x > track.bottomLeftCorner.x + danger and endPoint.x < track.bottomRightCorner.x - track.pixelConversion * 5 and endPoint.y > track.bottomRightCorner.y + track.pixelConversion * 5 \
    # and endPoint.y < track.topLeftCorner.y - track.pixelConversion * 5:
    #     print("Ball is an easy ball")
    #     waypoint_list.append(point.Point(endPoint.x, endPoint.y))
    #     singleton.Singleton.way_points = waypoint_list
    #     singleton.Singleton.danger_pos = False
    #     return

    if endPoint is not None:
        direct_path_line = LineString([(robot_center[0], robot_center[1]), (endPoint.x,  endPoint.y)])
        # If ball is in top-left corner
        if endPoint.x < track.topLeftCorner.x + danger and endPoint.y < track.topLeftCorner.y + danger:
            last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y + cornerSafePointY))
            print("Ball is in top left corner")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

        # If ball is in bottom-left corner
        elif endPoint.x < track.bottomLeftCorner.x + danger and endPoint.y > track.bottomLeftCorner.y - danger:
            last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y - cornerSafePointY))
            print("Ball is in bottom left corner")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

        # If ball is in top-right corner
        elif endPoint.x > track.topRightCorner.x - danger and endPoint.y < track.topRightCorner.y + danger:
            last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y + cornerSafePointY))
            print("Ball is in top right corner")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

            # If ball is in bottom-right corner
        elif endPoint.x > track.bottomRightCorner.x - danger and endPoint.y > track.bottomRightCorner.y - danger:
            last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y - cornerSafePointY))
            print("Ball is in bottom right corner")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

            # If ball is close to left side
        elif endPoint.x < track.bottomLeftCorner.x + danger:
            last_waypoint = point.Point(round(endPoint.x + sideSafePoint), round(endPoint.y))
            print("Ball is close to left side")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

            # If ball is close to right side
        elif endPoint.x > track.bottomRightCorner.x - danger:
            last_waypoint = point.Point(round(endPoint.x - sideSafePoint), round(endPoint.y))
            print("Ball is close to right side")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

            # If ball is close to bottom side
        elif endPoint.y > track.bottomRightCorner.y - danger:
            last_waypoint = point.Point(round(endPoint.x), round(endPoint.y - sideSafePoint))
            print("Ball is close to bottom side")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return

            # If ball is close to top side
        elif endPoint.y < track.topLeftCorner.y + danger:
            last_waypoint = point.Point(round(endPoint.x), round(endPoint.y + sideSafePoint))
            print("Ball is close to top side")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = True
            return
        else:
            print("Ball is an easy ball")
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                for i in range(len(safe_points)):
                    dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
                    if minDist == 0:
                        minDist = dist
                    elif dist < minDist:
                        minDist = dist
                        closestToBall_index = i
                for i in range(len(safe_points)):
                    dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
                    index_and_dist = (dist2, i)
                    safe_point_dist_to_robot.append(index_and_dist)
                    safe_point_dist_to_robot.sort()
                for i in range(2):
                    if i == 0:
                        safe_point_index1 = safe_point_dist_to_robot[i][1]
                        dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y,
                                              safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                    if i == 1:
                        safe_point_index = safe_point_dist_to_robot[i][1]
                        dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y,
                                              safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                        if dist3 < dist4:
                            first_waypoint = safe_points[safe_point_index1]
                        else:
                            first_waypoint = safe_points[safe_point_index]
                waypoint_list.append(first_waypoint)
                waypoint_list.append(safe_points[closestToBall_index])

            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.way_points = waypoint_list
            singleton.Singleton.is_dangerous = False
            print("Are lines touching: " + str(lines.areLineTouchingObstacleSquare(direct_path_line)))
            return

