import singleton.Singleton as singleton
import model
from model import ball
from brains import visionController
from brains import robotController
import math

turnSpeed = 20
forwardSpeed = 30
attackSpeed = 10
distanceCutOffPoint = 20
frontArmDegrees = 1080


def getAngle(cenBox, blPoint, cenBall):
    ang = math.degrees(math.atan2(cenBall[1] - blPoint[1], cenBall[0] - blPoint[0]) - math.atan2(cenBox[1] - blPoint[1], cenBox[0] - blPoint[0]))
    if ang < 0:
        ang = ang + 180
    if cenBox[0] < blPoint[0] and cenBox[1] > cenBall[1] or cenBox[1] < cenBall[1] and cenBox[0] > blPoint[0]:
        ang = 180 - ang
    return ang

def calc_pix_dist(start_x, start_y, end_x, end_y):
    par1 = math.pow((end_x - start_x))
    par2 = math.pow((end_y - start_y))
    pix_dist = math.sqrt(par1 + par2)
    return pix_dist

def chooseBall(balls, robot):
    print("Choose ball")
    # return ball
    return balls[0]

def calculateAngle(ball, robot):
    print("Calculate angle")
    return getAngle(robot.cenBox, robot.blPoint, ball.cenBall)

def distanceToBall(ball, robot):
    print("Calculate distance")
    return calc_pix_dist(robot.blSquareX, robot.blSquareY, ball.x, ball.y)

def numberOfBallsLeft():
    print("Number of balls left on track")
    # return numberOfBalls
    return 1



def goForGoal():
    print("Driving to goal")
    robotController.turn(360, True, 50)
    robotController.createCommandDeliver()








def main():
    print("hej")
    while True:
        print("While loop start")
        visionController.captureFrame()
        balls = singleton.Singleton.balls
        robot = singleton.Singleton.robot
        # obstacle = Singleton.obstacle
        track = singleton.Singleton.track
        pix_pr_cm = track.pixelConversion

        ball = chooseBall(balls, robot)
        angle = calculateAngle(ball, robot)

        if not numberOfBallsLeft() == 0:
            if numberOfBallsLeft() == 6:
                goForGoal()
            elif numberOfBallsLeft() == 2:
                goForGoal()
            else:
                if not angle == 0:
                    clockwise = True #TODO Find which way to turn
                    robotController.turn(angle, clockwise, turnSpeed)
                # elif distanceToWaypoint() > 5:
                elif distanceToBall(ball, robot) > distanceCutOffPoint:
                    #Drive forward to waypoint/ball
                    # robotController.drive_forward(robot.x, robot.y, waypoint.x, waypoint.y, pix_pr_cm, forwardSpeed)
                    robotController.drive_forward(robot.blSquareX, robot.blSquareY, ball.x, ball.y, pix_pr_cm, forwardSpeed)
                elif distanceToBall(ball, robot) <= distanceCutOffPoint:
                    degrees = robotController.drive_degrees(distanceToBall, pix_pr_cm)
                    robotController.createCommandAttack(attackSpeed, degrees, frontArmDegrees)
        else:
            #no balls left
            goForGoal()
    
    visionController.releaseImage()

            







if __name__ == "__main__":
    main()
