import math
from model import point
cam_height = 163.5
robot_height = 15.5
ball_height = 4
goal_height = 7.5
obstacle_height = 3.5
cam_robot_scale = cam_height / robot_height
cam_ball_scale = cam_height / ball_height
cam_goal_scale = cam_height / goal_height
cam_obstacle_scale = cam_height / obstacle_height


def point_correction(cam_cen, bl_point):
    x_correction = round((cam_cen.x - bl_point.x) / cam_robot_scale)
    y_correction = round((cam_cen.y - bl_point.y) / cam_robot_scale)
    px = bl_point.x + x_correction
    py = bl_point.y + y_correction
    p = point.Point(px, py)
    return p


def goal_cen_correction(cam_cen, goal_cen):
    x_correction = round((cam_cen.x - goal_cen.x) / cam_goal_scale)
    y_correction = round((cam_cen.y - goal_cen.y) / cam_goal_scale)
    px = goal_cen.x + x_correction
    py = goal_cen.y + y_correction
    p = point.Point(px, py)
    return p


def obstacle_cen_correction(cam_cen, obstacle_cen):
    x_correction = round((cam_cen.x - obstacle_cen.x) / cam_obstacle_scale)
    y_correction = round((cam_cen.y - obstacle_cen.y) / cam_obstacle_scale)
    px = obstacle_cen.x + x_correction
    py = obstacle_cen.y + y_correction
    p = point.Point(px, py)
    return p


def ball_cen_correction(cam_cen, ball_cen):
    x_correction = round((cam_cen.x - ball_cen.x) / cam_ball_scale)
    y_correction = round((cam_cen.y - ball_cen.y) / cam_ball_scale)
    px = round(ball_cen.x + x_correction / 2)
    py = round(ball_cen.y + y_correction / 2)
    p = point.Point(px, py)
    return p


# def main():
#     bl = point.Point(1250, 250)
#     cp = point.Point(500, 500)
#     real = point_correction(cp, bl)
#     print("x:" + str(real.x) + ", y: " + str(real.y))


# if __name__ == "__main__":
#     main()
