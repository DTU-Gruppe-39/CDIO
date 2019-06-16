import time

import brains.singleton as singleton
import model
from model import ball, robot
import numpy as np
from brains import visionController
from brains import robotController
from brains import wpGoal
import math
import threading
import _thread
from brains.angle import *
from view import visionOutputView
from brains.chooseBall import *
from brains.preventRotation import preventRotation



numberOfTries = 0
maxNumberOfTries = 10
turnSpeed = 20
forwardSpeed = 80
slow_forwardSpeed = 30
attackSpeed = 10
distanceCutOffPoint = 30
frontArmDegrees = 360
pix_pr_cm = None
zeroBallsLeft = False
sixBallsLeft = True
twoBallsLeft = True
# fakeBall = ball.Ball
# fakeRobot = robot.Robot

def endingRun():
    print("8 min has passed.\n Ending run.")
    _thread.interrupt_main()


def calc_pix_dist(start_x, start_y, end_x, end_y):
    par1 = math.pow((end_x - start_x), 2)
    par2 = math.pow((end_y - start_y), 2)
    pix_dist = math.sqrt(par1 + par2)

    return pix_dist


def chooseBall(balls):
    global numberOfTries

    print("Choose ball")
    # return ball
    if numberOfBallsLeft() == 0:
        return None
    else:
        if getChosenBall() is None:
            numberOfTries = 0
            setChosenBall(findBestBall(balls))
            return getChosenBall()
        else:
            if numberOfTries >= maxNumberOfTries:
                print("\033[1;33m" + "Maximum number of tries reached, picking a new ball" + "\033[0m")
                numberOfTries = 0
                singleton.Singleton.way_points.clear()
                setChosenBall(balls[0])
                return getChosenBall()
            else:
                return getChosenBall()


def distanceToBall(ball, robot):
    print("Calculate distance in pix")
    return calc_pix_dist(robot.blSquareX, robot.blSquareY, ball.x, ball.y)


def distanceToWaypoint(point, robotpos):
    print("Calculate distance in pix")
    return calc_pix_dist(robotpos[0], robotpos[1], point[0], point[1])


def numberOfBallsLeft():
    print("\033[1m" + "Number of balls left on track: " + "\033[0m" + "\033[1;34m" + str(len(singleton.Singleton.balls)) + "\033[0m")

    return len(singleton.Singleton.balls)


def moreBallsThanExpected():
    global zeroBallsLeft, twoBallsLeft, sixBallsLeft
    numberOfBall = numberOfBallsLeft()
    if numberOfBall > 6:
        sixBallsLeft = True
        # print("Unexpected extra ball, ABORTING go for goal")
        # break
    elif numberOfBall > 2:
        twoBallsLeft = True
        # print("Unexpected extra ball, ABORTING go for goal")
        # break
    elif numberOfBall > 0:
        zeroBallsLeft = False


def goForGoal(robot, expectedNumberOfBallsLeft):
    global zeroBallsLeft, twoBallsLeft, sixBallsLeft
    print("\n\nDriving to goal")
    completed = False
    aligned = False
    numberOfTriesToAlign = 0
    # robotController.turn(360, True, 40)
    # robotController.createCommandDeliver()
    #False for left goal
    goalCord = wpGoal.getWpGoal(False)
    print("\033[1;32m" + "Goal cord: " + str(goalCord) + "\033[0m")
    while not completed:
        visionController.captureFrame()
        # balls = singleton.Singleton.balls
        robot = singleton.Singleton.robot
        # obstacle = Singleton.obstacle
        track = singleton.Singleton.track
        pix_pr_cm = track.pixelConversion
        angle = calculateAngle(goalCord, robot)
        if angle >= 5:
            robotController.turn(angle, getclockWise(), turnSpeed)
            if numberOfBallsLeft() > expectedNumberOfBallsLeft:
                print("\033[1;33m" + "Unexpected extra ball, ABORTING go for goal" + "\033[0m")
                moreBallsThanExpected()
                break
            numberOfTriesToAlign = numberOfTriesToAlign + 1
            if numberOfTriesToAlign > 5:
                # bak robotten, og prøv at align igen
                # Tjek evt hvilken vej den peger, så man kan køre væk fra målet
                robotController.createCommandTank(-20, -20, 360)
                numberOfTriesToAlign = 0
        else:
            # Drive forward to waypoint/ball
            numberOfTriesToAlign = 0
            dist = distanceToWaypoint(goalCord, [robot.centrumX, robot.centrumY])
            robotController.drive_forward(dist, pix_pr_cm, forwardSpeed)
            while not aligned:
                visionController.captureFrame()
                # balls = singleton.Singleton.balls
                robot = singleton.Singleton.robot
                # obstacle = Singleton.obstacle
                track = singleton.Singleton.track
                pix_pr_cm = track.pixelConversion
                goalCord = (track.bigGoal.x, track.bigGoal.y)
                # angle = realVectorAngle(goalCord, [robot.centrumX, robot.centrumY], goalCord)
                angle = calculateAngle(goalCord, robot)
                print ("\nRealvector angle: " + str(angle) + "\n")
                if numberOfBallsLeft() > expectedNumberOfBallsLeft:
                    print("\033[1;33m" + "Unexpected extra ball, ABORTING go for goal" + "\033[0m")
                    moreBallsThanExpected()
                    break
                if angle >= 5:
                    robotController.turn(angle, getclockWise(), turnSpeed)
                    numberOfTriesToAlign = numberOfTriesToAlign + 1
                    if numberOfTriesToAlign > 5:
                        #bak robotten, og prøv at align igen
                        robotController.createCommandTank(-20, -20, 360)
                        numberOfTriesToAlign = 0
                else:
                    moreBallsThanExpected()
                    robotController.createCommandTank(20, 20, 360)
                    robotController.createCommandDeliver()
                    robotController.createCommandTank(-20, -20, 360)
                    aligned = True
                    break
            completed = True
            break
    print("Go for goal done\n")


def main():
    global numberOfTries, pix_pr_cm, zeroBallsLeft, twoBallsLeft, sixBallsLeft
    #print("hej")
    # 480 seconds is 8 minutes
    timer = threading.Timer(480.0, endingRun)
    timer.start()
    start = time.time()
    while True:
        print("\033[1;36m" + "While loop start" + "\033[0m")
        visionController.captureFrame()
        balls = singleton.Singleton.balls
        robot = singleton.Singleton.robot
        # obstacle = Singleton.obstacle
        track = singleton.Singleton.track
        pix_pr_cm = track.pixelConversion

        # Check if robot point is in rotation danger zone
        # if preventRotation():
        #     robotController.createCommandTank(-20, -20, 360)
        ball = chooseBall(balls)

        if len(singleton.Singleton.way_points) == 0:
            waypoint.waypoints(ball)
            waypoints = singleton.Singleton.way_points
            visionOutputView.showImage()
            if len(singleton.Singleton.way_points) != 0:
                print("List af wawypoints: " + str(singleton.Singleton.way_points)   )
                print("waypoint x: " + str(waypoints[0].x))
        numberOfBalls = numberOfBallsLeft()

        if not numberOfBalls == 0 and not zeroBallsLeft:
            angle = calculateAngle((waypoints[0].x, waypoints[0].y), robot)
            if numberOfBalls == 6 and sixBallsLeft:
                sixBallsLeft = False
                goForGoal(robot, numberOfBalls)
            elif numberOfBalls == 2 and twoBallsLeft:
                twoBallsLeft = False
                goForGoal(robot, numberOfBalls)
            else:
                if not angle < 5:
                    robotController.turn(angle, getclockWise(), turnSpeed)
                    numberOfTries = numberOfTries + 1
                    print("PRØVER AT TURNE TIL PUNKT")
                elif (distanceToBall(waypoints[0], robot) / pix_pr_cm) > distanceCutOffPoint:
                    #Drive forward to waypoint/ball
                    # robotController.drive_forward(robot.x, robot.y, waypoint.x, waypoint.y, pix_pr_cm, forwardSpeed)
                    # print("Foran drive")
                    if len(waypoints) > 1:
                        print("dist to ball: " + str(distanceToWaypoint([waypoints[0].x, waypoints[0].y], [robot.centrumX, robot.centrumY]) / pix_pr_cm))
                        print("MERE END 1 WAYPOINT TILBAGE")
                        print("Antal af Waypoints: " + str(len(waypoints)))
                        robotController.drive_forward(distanceToWaypoint([waypoints[0].x, waypoints[0].y], [robot.centrumX, robot.centrumY]), pix_pr_cm, forwardSpeed)
                        waypoint.pop_waypoint()
                        print("POPPER ET WAYPOINT")
                        print("Antal af Waypoints: " + str(len(waypoints)))
                    else:
                        print("dist to ball: " + str(distanceToBall(waypoints[0], robot) / pix_pr_cm))
                        print("MINDRE END 1 WAYPOINT TILBAGE")
                        print("Antal af Waypoints: " + str(len(waypoints)))
                        robotController.drive_forward(distanceToBall(waypoints[0], robot) - distanceCutOffPoint * pix_pr_cm + pix_pr_cm * 10, pix_pr_cm, forwardSpeed)
                    # waypoints.pop(0)
                elif (distanceToBall(waypoints[0], robot) / pix_pr_cm) <= distanceCutOffPoint:
                    print("ER UNDER CUTOFFPOINTET")
                    # degrees = robotController.drive_degrees(distanceToBall(ball, robot), pix_pr_cm)
                    # print("degrees" + str(degrees))
                    dist = distanceToBall(waypoints[0], robot)
                    robotController.drive_forward(dist, pix_pr_cm, slow_forwardSpeed)
                    if len(waypoints) == 1:
                        if singleton.Singleton.danger_pos:
                            robotController.createCommandWall(10, 35)
                            setChosenBall(None)
                        else:
                            robotController.createCommandAttack(attackSpeed, 90, frontArmDegrees)
                            setChosenBall(None)
                        # robotController.createCommandAttack(attackSpeed, degrees, frontArmDegrees)
                    waypoints.pop(0)
        else:
            #no balls left
            if zeroBallsLeft:
                timer.cancel()
                end = time.time()
                run_time = end - start
                min_run = math.floor(run_time/60)
                sec_run = run_time % 60
                print("\033[1;33m" + "Time: " + str(min_run) + "min" + str(sec_run) + "sec")
                print("\n\n\nRobot is Done!!!\n\n\n")
                print("\033[0m")
                while True:
                    #Play sound to mark it is done
                    robotController.createCommandSound()
            else:
                zeroBallsLeft = True
                goForGoal(robot, numberOfBalls)


    # visionController.releaseImage()









if __name__ == "__main__":
    main()
