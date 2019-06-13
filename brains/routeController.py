import brains.singleton as singleton
import model
from model import ball, robot
from brains import visionController
from brains import robotController
import math

numberOfTries = 0
maxNumberOfTries = 5
chosenBall = None
turnSpeed = 20
forwardSpeed = 30
attackSpeed = 10
distanceCutOffPoint = 20
frontArmDegrees = 1080
clockwise = False
# fakeBall = ball.Ball
# fakeRobot = robot.Robot


def getAngle(cenBox, blPoint, cenBall):
    global clockwise
    ang = math.degrees(math.atan2(cenBall[1] - blPoint[1], cenBall[0] - blPoint[0]) - math.atan2(cenBox[1] - blPoint[1], cenBox[0] - blPoint[0]))
    rotation = (blPoint[0] - cenBox[0]) * (cenBall[1] - cenBox[1]) - (blPoint[1] - cenBox[1]) * (cenBall[0] - cenBox[0])
    if ang < 0 and rotation > 0:
        ang = ang + 180
        clockwise = True
    if ang > 180:
        ang = ang - 180
        clockwise = True
    if rotation < 0:
            ang = 180 - ang
            clockwise = False
            if ang > 180:
                ang = ang - 360
                clockwise = False
    return ang

def calc_pix_dist(start_x, start_y, end_x, end_y):
    par1 = math.pow((end_x - start_x), 2)
    par2 = math.pow((end_y - start_y), 2)
    pix_dist = math.sqrt(par1 + par2)

    return pix_dist

def chooseBall(balls, robot):
    global chosenBall, numberOfTries

    print("Choose ball")
    # return ball
    if chosenBall is None:
        chosenBall = balls[0]
        return chosenBall
    else:
        if numberOfTries >= maxNumberOfTries:
            numberOfTries = 0
            chosenBall = balls[0]
            return chosenBall
        else:
            return chosenBall


def calculateAngle(ball, robot):
    print("Calculate angle")
    ang = getAngle((robot.centrumX, robot.centrumY), (robot.blSquareX, robot.blSquareY), (ball.x, ball.y))
    print("routeCon: angle is " + str(ang))
    return ang


def distanceToBall(ball, robot):
    print("Calculate distance")
    return calc_pix_dist(robot.blSquareX, robot.blSquareY, ball.x, ball.y)

def numberOfBallsLeft():
    print("Number of balls left on track")

    return len(singleton.Singleton.balls)



def goForGoal():
    print("Driving to goal")
    robotController.turn(360, True, 40)
    robotController.createCommandDeliver()







def main():
    global chosenBall, numberOfTries
    print("hej")
    while True:
        print("While loop start")
        visionController.captureFrame()
        balls = singleton.Singleton.balls
        robot = singleton.Singleton.robot
        # obstacle = Singleton.obstacle
        track = singleton.Singleton.track
        pix_pr_cm = track.pixelConversion


        # fakeBall.x = 1013
        # fakeBall.y = 570
        # fakeBall.radius = 0
        #
        # fakeBalls = []
        # fakeBalls.append(fakeBall)
        #
        # fakeRobot.blSquareX = 685
        # fakeRobot.blSquareY = 602
        # fakeRobot.centrumX = 656
        # fakeRobot.centrumY = 696

        # pix_pr_cm = 7
        # robot = fakeRobot

        ball = chooseBall(balls, robot)
        angle = calculateAngle(ball, robot)



        if not numberOfBallsLeft() == 0:
            if numberOfBallsLeft() == 6:
                goForGoal()
            elif numberOfBallsLeft() == 2:
                goForGoal()
            else:
                if not angle < 5:
                    robotController.turn(angle, clockwise, turnSpeed)
                    numberOfTries = numberOfTries + 1
                # elif distanceToWaypoint() > 5:
                elif distanceToBall(ball, robot) > distanceCutOffPoint:
                    #Drive forward to waypoint/ball
                    # robotController.drive_forward(robot.x, robot.y, waypoint.x, waypoint.y, pix_pr_cm, forwardSpeed)
                    print("Foran drive")
                    robotController.drive_forward(robot.blSquareX, robot.blSquareY, ball.x, ball.y, pix_pr_cm, forwardSpeed)
                    robotController.createCommandAttack(attackSpeed, 90, frontArmDegrees)
                    chosenBall = None
                    print("efter drive")
                elif distanceToBall(ball, robot) <= distanceCutOffPoint:
                    degrees = robotController.drive_degrees(distanceToBall, pix_pr_cm)
                    print("degrees" + str(degrees))
                    robotController.createCommandAttack(attackSpeed, degrees, frontArmDegrees)
        else:
            #no balls left
            goForGoal()

    visionController.releaseImage()









if __name__ == "__main__":
    main()
