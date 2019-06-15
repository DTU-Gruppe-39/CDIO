import math
from model import point
cam_height = 162.2
robot_height = 15.5
scale = 162.2 / 15.5


def point_correction(cam_cen, bl_point):
    p = point.Point
    x_correction = (cam_cen.x - bl_point.x) * scale
    y_correction = (cam_cen.y - bl_point.y) * scale
    p.x = bl_point.x + x_correction
    p.y = bl_point.y + y_correction
    return p

def main():
    cp = point.Point
    cp.x = 500
    cp.y = 500
    bl = point.Point
    bl.x = 1250
    bl.y = 250
    real = point_correction(cp, bl)
    print("" + real.x + "" + real.y)
