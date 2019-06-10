import math
wheelCircunference = 3 * math.pi
wheelBase = 12.5


def calc_pix_dist(start_x, start_y, end_x, end_y):
    par1 = math.pow((end_x - start_x))
    par2 = math.pow((end_y - start_y))
    pix_dist = math.sqrt(par1 + par2)
    return pix_dist


def drive_degrees(pix_dist, pix_pr_cm):
    dist = pix_dist * pix_pr_cm
    drive_deg = math.floor((dist / wheelCircunference) * 360.0)
    return drive_deg


def drive_forward(start_x, start_y, end_x, end_y, pix_pr_cm):
    pix_dist = calc_pix_dist(start_x, start_y, end_x, end_y)
    degrees = drive_degrees(pix_dist, pix_pr_cm)
    # Send degrees to NetworkCon
    return


def turn(angle, direction):
    # Send to angle and direction to NetworkCon
    return


def attack():
    # Send attack to NetworkCon
    return

