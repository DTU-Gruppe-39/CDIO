import math
import brains.singleton as singleton
from model.ball import Ball
from brains.robotController import calc_pix_dist
from shapely.geometry import LineString
from brains import lines
from model import point
from model import obstacle


def pop_waypoint():
    singleton.Singleton.way_points.pop(0)


def get_waypoint():
    return singleton.Singleton.way_points


def avoid_obstacle(endPoint):
    if endPoint is not None:
        minDist = 0
        closestToBall_index = 0
        robot = singleton.Singleton.robot
        robot_center = (robot.centrumX, robot.centrumY)
        waypoint_list = singleton.Singleton.way_points
        safe_points = singleton.Singleton.safe_points
        safe_point_dist_to_robot = []
        direct_path_line = LineString([(robot_center[0], robot_center[1]), (endPoint.x, endPoint.y)])
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
                        first_waypoint = point.Point(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y)
                    else:
                        first_waypoint = point.Point(safe_points[safe_point_index].x, safe_points[safe_point_index].y)
            waypoint_list.append(first_waypoint)
            direct_path_line = LineString([(first_waypoint.x, first_waypoint.y), (endPoint.x, endPoint.y)])
            if lines.areLineTouchingObstacleSquare(direct_path_line):
                second_waypoint = point.Point(safe_points[closestToBall_index].x, safe_points[closestToBall_index].y)
                waypoint_list.append(second_waypoint)


def waypoints(endPoint):
    minDist = 0
    closestToBall_index = 0
    track = singleton.Singleton.track
    danger = round(track.pixelConversion * 15)
    cornerSafePointX = round(track.pixelConversion * 20)
    cornerSafePointY = round(track.pixelConversion * 45)
    sideSafePoint = round(track.pixelConversion * 32)
    line_length = round(track.pixelConversion * 22)
    robot = singleton.Singleton.robot
    robot_center = (robot.centrumX, robot.centrumY)
    obstacle = singleton.Singleton.obstacle
    singleton.Singleton.way_points.clear()
    waypoint_list = singleton.Singleton.way_points
    safe_points = singleton.Singleton.safe_points
    safe_point_dist_to_robot = []
    obstacleDanger = round(track.pixelConversion * 12)

    
    # for i in range(len(safe_points)):
    #     dist = calc_pix_dist(endPoint.x, endPoint.y, safe_points[i].x, safe_points[i].y)
    #     if minDist == 0:
    #         minDist = dist
    #     elif dist < minDist:
    #         minDist = dist
    #         closestToBall_index = i
    # for i in range(len(safe_points)):
    #     dist2 = calc_pix_dist(robot.centrumX, robot.centrumY, safe_points[i].x, safe_points[i].y)
    #     index_and_dist = (dist2, i)
    #     safe_point_dist_to_robot.append(index_and_dist)
    #     safe_point_dist_to_robot.sort()
    # for i in range(2):
    #     if i == 0:
    #         safe_point_index1 = safe_point_dist_to_robot[i][1]
    #         dist3 = calc_pix_dist(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y, projected_point_x,
    #                               projected_point_y)
    #     if i == 1:
    #         safe_point_index = safe_point_dist_to_robot[i][1]
    #         dist4 = calc_pix_dist(safe_points[safe_point_index].x, safe_points[safe_point_index].y, projected_point_x,
    #                               projected_point_y)
    #         if dist3 < dist4:
    #             first_waypoint = safe_points[safe_point_index1]
    #         else:
    #             first_waypoint = safe_points[safe_point_index]

    if endPoint is not None:
        direct_path_line = LineString([(robot_center[0], robot_center[1]), (endPoint.x,  endPoint.y)])
        # If the ball is inside the bounding square of the obstacle
        if obstacle.square_bottom_right_corner.x >= endPoint.x >= obstacle.square_top_left_corner.x and obstacle.square_bottom_right_corner.y >= endPoint.y >= obstacle.square_top_left_corner.y:
            print("Ball is inside the obstacle!")
            scale = line_length / calc_pix_dist(obstacle.center_x, obstacle.center_y, endPoint.x, endPoint.y)
            projected_point_x = round(((endPoint.x - obstacle.center_x) * scale) + obstacle.center_x)
            projected_point_y = round(((endPoint.y - obstacle.center_y) * scale) + obstacle.center_y)
            projected_point = point.Point(projected_point_x, projected_point_y)
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
                        first_waypoint = point.Point(safe_points[safe_point_index1].x, safe_points[safe_point_index1].y)
                    else:
                        first_waypoint = point.Point(safe_points[safe_point_index].x, safe_points[safe_point_index].y)

            waypoint_list.append(first_waypoint)
            waypoint_list.append(safe_points[closestToBall_index])
            waypoint_list.append(projected_point)
            waypoint_list.append(endPoint)
            singleton.Singleton.is_in_obstacle = True
            singleton.Singleton.is_dangerous = False


        # If ball is in top-left corner
        elif endPoint.x < track.topLeftCorner.x + danger and endPoint.y < track.topLeftCorner.y + danger:
            last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y + cornerSafePointY))
            print("Ball is in top left corner")
            avoid_obstacle(endPoint)
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            singleton.Singleton.wallOnLeftCorner = True
            singleton.Singleton.wallOnRightCorner = False
            return

        # If ball is in bottom-left corner
        elif endPoint.x < track.bottomLeftCorner.x + danger and endPoint.y > track.bottomLeftCorner.y - danger:
            last_waypoint = point.Point(round(endPoint.x + cornerSafePointX), round(endPoint.y - cornerSafePointY))
            print("Ball is in bottom left corner")
            avoid_obstacle(endPoint)
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            singleton.Singleton.wallOnRightCorner = True
            singleton.Singleton.wallOnLeftCorner = False
            return

        # If ball is in top-right corner
        elif endPoint.x > track.topRightCorner.x - danger and endPoint.y < track.topRightCorner.y + danger:
            last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y + cornerSafePointY))
            print("Ball is in top right corner")
            avoid_obstacle(endPoint)
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            singleton.Singleton.wallOnRightCorner = True
            singleton.Singleton.wallOnLeftCorner = False
            return

            # If ball is in bottom-right corner
        elif endPoint.x > track.bottomRightCorner.x - danger and endPoint.y > track.bottomRightCorner.y - danger:
            last_waypoint = point.Point(round(endPoint.x - cornerSafePointX), round(endPoint.y - cornerSafePointY))
            print("Ball is in bottom right corner")
            avoid_obstacle(endPoint)
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            singleton.Singleton.wallOnLeftCorner = True
            singleton.Singleton.wallOnRightCorner = False
            return

            # If ball is close to left side
        elif endPoint.x < track.bottomLeftCorner.x + danger:
            last_waypoint = point.Point(round(endPoint.x + sideSafePoint), round(endPoint.y))
            print("Ball is close to left side")
            avoid_obstacle(endPoint)
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False

            return

            # If ball is close to right side
        elif endPoint.x > track.bottomRightCorner.x - danger:
            last_waypoint = point.Point(round(endPoint.x - sideSafePoint), round(endPoint.y))
            print("Ball is close to right side")
            avoid_obstacle(endPoint)
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            return

            # If ball is close to bottom side
        elif endPoint.y > track.bottomRightCorner.y - danger:
            print("Ball is close to bottom side")
            avoid_obstacle(endPoint)
            if obstacle.center_x - obstacleDanger < endPoint.x < obstacle.center_x + obstacleDanger:
                if robot.centrumX < endPoint.x:
                    last_waypoint = point.Point(round(obstacle.center_x - track.pixelConversion*12), round(endPoint.y - sideSafePoint))
                elif obstacle.center_x > endPoint.x:
                    last_waypoint = point.Point(round(obstacle.center_x + track.pixelConversion*12), round(endPoint.y - sideSafePoint))
            else:
                last_waypoint = point.Point(round(endPoint.x), round(endPoint.y - sideSafePoint))

            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            return

            # If ball is close to top side
        elif endPoint.y < track.topLeftCorner.y + danger:
            print("Ball is close to top side")
            avoid_obstacle(endPoint)
            if obstacle.center_x - obstacleDanger < endPoint.x < obstacle.center_x + obstacleDanger:
                if robot.centrumX < endPoint.x:
                    last_waypoint = point.Point(round(obstacle.center_x - track.pixelConversion*12), round(endPoint.y + sideSafePoint))
                elif robot.centrumX > endPoint.x:
                    last_waypoint = point.Point(round(obstacle.center_x + track.pixelConversion*12), round(endPoint.y + sideSafePoint))
            else:
                last_waypoint = point.Point(round(endPoint.x), round(endPoint.y + sideSafePoint))
            waypoint_list.append(last_waypoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = True
            singleton.Singleton.is_in_obstacle = False
            return
        elif singleton.Singleton.is_going_for_goal:
            print("Is going for goal")
            avoidance = round(10 * track.pixelConversion)
            avoid_obstacle(endPoint)
            waypoint_list.append(point.Point(endPoint.x - avoidance, endPoint.y))
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = False
            singleton.Singleton.is_in_obstacle = False
            singleton.Singleton.is_going_for_goal = False
        else:
            print("Ball is an easy ball")
            avoid_obstacle(endPoint)
            waypoint_list.append(point.Point(endPoint.x, endPoint.y))
            singleton.Singleton.is_dangerous = False
            singleton.Singleton.is_in_obstacle = False
            print("Are lines touching: " + str(lines.areLineTouchingObstacleSquare(direct_path_line)))
            return

