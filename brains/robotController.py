import math
import sys
import brains.networkingController as networking
import time
wheelCircunference = 3 * math.pi
wheelBase = 12.5


def createCommandTank(left, right, degrees):
    message = {
        "type": "tank_drive",
        "left": left,
        "right": right,
        "degrees": degrees
    }
    return networking.sendCommand(message)


def createCommandFront(speed, degrees):
    message = {
        "type": "front",
        "speed": speed,
        "degrees": degrees
    }
    return networking.sendCommand(message)


def createCommandBack(speed, degrees):
    message = {
        "type": "back",
        "speed": speed,
        "degrees": degrees
    }
    return networking.sendCommand(message)


def createCommandAttack(speed, tank_degrees, front_degrees):
    message = {
        "type": "attack",
        "left": speed,
        "right": speed,
        "tank_degrees": tank_degrees,
        "front_degrees": front_degrees
    }
    return networking.sendCommand(message)


def createCommandDeliver():
    message = {
        "type": "deliver"
    }
    return networking.sendCommand(message)


def createCommandSound():
    message = {
        "type": "sound"
    }
    return networking.sendCommand(message)


def calc_pix_dist(start_x, start_y, end_x, end_y):
    par1 = math.pow((end_x - start_x), 2)
    par2 = math.pow((end_y - start_y), 2)
    pix_dist = math.sqrt(par1 + par2)
    return pix_dist


def drive_degrees(pix_dist, pix_pr_cm):
    dist = pix_dist / pix_pr_cm
    drive_deg = round((dist / wheelCircunference) * 360.0)
    return drive_deg


def drive_forward(start_x, start_y, end_x, end_y, pix_pr_cm, speed):
    # Speed can be changed to hardcoded values corresponding to the scenario
    pix_dist = calc_pix_dist(start_x, start_y, end_x, end_y)
    degrees = drive_degrees(pix_dist-14, pix_pr_cm)
    # Send msg NetworkCon
    return createCommandTank(speed, speed, degrees)


def turn(angle, clockwise, speed):
    # Turn_speed can be changed to hardcoded values corresponding to the scenario
    degrees = round((((wheelBase * math.pi) / 360)*angle / wheelCircunference) * 360.0)
    if clockwise :
      return createCommandTank(speed, -speed, degrees)

    else:
        return createCommandTank(-speed, speed, degrees)
    # Send msg to NetworkCon


# def attack(speed, start_x, start_y, end_x, end_y, pix_pr_cm, angle, rotation, turn_speed):
#     # Speed and turn_speed can be changed to hardcoded values corresponding to the scenario
#     pix_dist = calc_pix_dist(start_x, start_y, end_x, end_y)
#     tank_degrees = drive_degrees(pix_dist, pix_pr_cm)
#     turn(angle, rotation, turn_speed)
#     msg = createCommandTank(speed, speed, tank_degrees)
#     # Send msg to NetworkCon
#     return


def keyW():
    message = {
        "type": "w"
    }
    return message

def keyA():
    message = {
        "type": "a"
    }
    return message

def keyS():
    message = {
        "type": "s"
    }
    return message

def keyD():
    message = {
        "type": "d"
    }
    return message

def stop():
    message = {
        "type": "stop"
    }
    return message

def keyF():
    message = createCommandFront(25, 1080)
    return message

def keyG():
    message = createCommandDeliver()
    return message





# def main():
#     # while True:
#     #     networking.sendCommand(createCommandTank(30, 30, 360))
#     #     time.sleep(3)
#     #     networking.sendCommand(createCommandTank(-30, -30, 720))
#     #     time.sleep(10)


#     while True:
#         key = input()
#         if key == 'w':
#             networking.sendCommand(keyW())
#             while True:
#                 if not input() == 'w':
#                     # key = input()
#                     networking.sendCommand(stop())
#                     break
#         elif key == 'a':
#             networking.sendCommand(keyA())
#             while True:
#                 if not input() == 'a':
#                     # key = input()
#                     networking.sendCommand(stop())
#                     break
#         elif key == 's':
#             networking.sendCommand(keyS())
#             while True:
#                 if not input() == 's':
#                     # key = input()
#                     networking.sendCommand(stop())
#                     break
#         elif key == 'd':
#             networking.sendCommand(keyD())
#             while True:
#                 if not input() == 'd':
#                     # key = input()
#                     networking.sendCommand(stop())
#                     break
#         elif key == 'f':
#             networking.sendCommand(keyF())
#         elif key == 'g':
#             networking.sendCommand(keyG())

# if __name__ == "__main__":
#     main()