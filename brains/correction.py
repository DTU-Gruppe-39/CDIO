import math
from model import point
cam_height = 162.2
robot_height = 15.5
scale = 162.2 / 15.5


def point_correction(cam_cen, bl_point):
    x_correction = int((cam_cen.x - bl_point.x) / scale)
    y_correction = int((cam_cen.y - bl_point.y) / scale)
    px = bl_point.x + x_correction
    py = bl_point.y + y_correction
    p = point.Point(px, py)
    return p


def ball_cen_correction():

    return


# def main():
#     bl = point.Point(1250, 250)
#     cp = point.Point(500, 500)
#     real = point_correction(cp, bl)
#     print("x:" + str(real.x) + ", y: " + str(real.y))


# if __name__ == "__main__":
#     main()
