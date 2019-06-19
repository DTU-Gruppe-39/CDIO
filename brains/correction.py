import math
from model import point
cam_height = 164
robot_height = 15.5
ball_height = 4
cam_robot_scale = cam_height / robot_height
cam_ball_scale = cam_height / ball_height


def point_correction(cam_cen, bl_point):
    x_correction = round((cam_cen.x - bl_point.x) / cam_robot_scale)
    y_correction = round((cam_cen.y - bl_point.y) / cam_robot_scale)
    px = bl_point.x + x_correction
    py = bl_point.y + y_correction
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
