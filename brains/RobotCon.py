import math
import sys
import networking
import time
wheelCircunference = 3 * math.pi
wheelBase = 12.5


def createCommandTank (left, right, degrees):
    message = {
        "type": "tank_drive",
        "left": left,
        "right": right,
        "degrees": degrees
    }
    return message


def createCommandFront (speed, degrees):
    message = {
        "type": "front",
        "speed": speed,
        "degrees": degrees
    }
    return message


def createCommandBack (speed, degrees):
    message = {
        "type": "back",
        "speed": speed,
        "degrees": degrees
    }
    return message


def createCommandAttack (left, right, tank_degrees, front_degrees):
    message = {
        "type": "attack",
        "left": left,
        "right": right,
        "tank_degrees": tank_degrees,
        "front_degrees": front_degrees
    }
    return message


def createCommandDeliver ():
    message = {
        "type": "deliver"
    }
    return message


def calc_pix_dist(start_x, start_y, end_x, end_y):
    par1 = math.pow((end_x - start_x))
    par2 = math.pow((end_y - start_y))
    pix_dist = math.sqrt(par1 + par2)
    return pix_dist


def drive_degrees(pix_dist, pix_pr_cm):
    dist = pix_dist * pix_pr_cm
    drive_deg = math.floor((dist / wheelCircunference) * 360.0)
    return drive_deg


def drive_forward(start_x, start_y, end_x, end_y, pix_pr_cm, speed):
    # Speed can be changed to hardcoded values corresponding to the scenario
    pix_dist = calc_pix_dist(start_x, start_y, end_x, end_y)
    degrees = drive_degrees(pix_dist, pix_pr_cm)
    msg = createCommandTank(speed, speed, degrees)
    # Send msg NetworkCon
    return


def turn(angle, rotation, speed):
    # Turn_speed can be changed to hardcoded values corresponding to the scenario
    degrees = math.floor((((wheelBase * math.pi) / 360)*angle / wheelCircunference) * 360.0)
    if rotation == "clockwise" :
        msg = createCommandTank(speed, -speed, degrees)

    else:
        msg = createCommandTank(-speed, speed, degrees)
    # Send msg to NetworkCon
    return


def attack(speed, start_x, start_y, end_x, end_y, pix_pr_cm, angle, rotation, turn_speed):
    # Speed and turn_speed can be changed to hardcoded values corresponding to the scenario
    pix_dist = calc_pix_dist(start_x, start_y, end_x, end_y)
    tank_degrees = drive_degrees(pix_dist, pix_pr_cm)
    turn(angle, rotation, turn_speed)
    msg = createCommandTank(speed, speed, tank_degrees)
    # Send msg to NetworkCon
    return


def dump_balls():
    msg = createCommandDeliver()
    # Send msg to NetworkCon
    return



def main():
    while True:
        networking.sendCommand(createCommandTank(30, 30, 360))
        time.sleep(3)
        networking.sendCommand(createCommandTank(-30, -30, 720))
        time.sleep(10)

if __name__ == "__main__":
    main()