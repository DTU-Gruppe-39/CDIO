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


numberOfTries = 0
maxNumberOfTries = 10
turnSpeed = 25
forwardSpeed = 80
slow_forwardSpeed = 35
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
                if numberOfBallsLeft() == 1:
                    print("\033[1;33m" + "Cant reach last ball, so going for goal to get a better position" + "\033[0m")
                    goForGoal(0)

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
        twoBallsLeft = True
        zeroBallsLeft = False
        # print("Unexpected extra ball, ABORTING go for goal")
        # break
    elif numberOfBall > 2:
        twoBallsLeft = True
        zeroBallsLeft = False
        # print("Unexpected extra ball, ABORTING go for goal")
        # break
    elif numberOfBall > 0:
        zeroBallsLeft = False


def checker(angle):
    if angle is not None:
        if angle >= 5:
            return True
        else:
            return False
    else:
        return True

def goForGoal(expectedNumberOfBallsLeft):
    global zeroBallsLeft, twoBallsLeft, sixBallsLeft
    print("\n\n\033[1;32m" + "Driving to goal" + "\033[0m")
    singleton.Singleton.is_going_for_goal = True
    completed = False
    aligned = False
    numberOfTriesToAlign = 0
    # robotController.turn(360, True, 40)
    # robotController.createCommandDeliver()
    #False for left goal
    goalCord = wpGoal.getWpGoal(False)
    waypoint.waypoints(goalCord)
    waypoints = singleton.Singleton.way_points
    print("Goal cord: " + str(waypoints))
    while not completed:
        if len(waypoints) is not 0:
            visionController.captureFrame()
            # balls = singleton.Singleton.balls
            robot = singleton.Singleton.robot
            # obstacle = Singleton.obstacle
            track = singleton.Singleton.track
            pix_pr_cm = track.pixelConversion
            angle = calculateAngle((waypoints[0].x, waypoints[0].y), robot)
        if angle >= 5:
            if len(waypoints) is not 0:
                robotController.turn(angle, getclockWise(), turnSpeed)
                if numberOfBallsLeft() > expectedNumberOfBallsLeft:
                    print("\033[1;33m" + "Unexpected extra ball, ABORTING go for goal" + "\033[0m")
                    moreBallsThanExpected()
                    singleton.Singleton.way_points.clear()
                    setChosenBall(None)
                    break
                numberOfTriesToAlign = numberOfTriesToAlign + 1
                if numberOfTriesToAlign >= 3:
                    # bak robotten, og prøv at align igen
                    # Tjek evt hvilken vej den peger, så man kan køre væk fra målet
                    # robotController.createCommandTank(-20, -20, 720)
                    numberOfTriesToAlign = 0
        else:
            # Drive forward to waypoint/ball
            if len(waypoints) != 0:
                numberOfTriesToAlign = 0
                dist = distanceToWaypoint((waypoints[0].x, waypoints[0].y), [robot.centrumX, robot.centrumY])
                robotController.drive_forward(dist, pix_pr_cm, 50)
                waypoint.pop_waypoint()
            if len(waypoints) == 0:
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
                    print("\nRealvector angle: " + str(angle) + "\n")
                    if numberOfBallsLeft() > expectedNumberOfBallsLeft:
                        print("\033[1;33m" + "Unexpected extra ball, ABORTING go for goal" + "\033[0m")
                        moreBallsThanExpected()
                        singleton.Singleton.way_points.clear()
                        setChosenBall(None)
                        break
                    if angle >= 3:
                        robotController.turn(angle, getclockWise(), turnSpeed)
                        numberOfTriesToAlign = numberOfTriesToAlign + 1
                        # if numberOfTriesToAlign > 5:
                            #bak robotten, og prøv at align igen
                            # robotController.createCommandTank(-20, -20, 360)
                            # numberOfTriesToAlign = 0
                    else:
                        moreBallsThanExpected()
                        robotController.createCommandTank(20, 20, 590)
                        robotController.createCommandDeliver()
                        robotController.createCommandTank(-50, -50, 400)
                        print("\n\n\033[1;32m" + "Balls delivered to goal" + "\033[0m")
                        aligned = True
                        singleton.Singleton.way_points.clear()
                        setChosenBall(None)
                        break
                completed = True
                singleton.Singleton.way_points.clear()
                setChosenBall(None)
                break
    print("Go for goal done\n\n")
    singleton.Singleton.way_points.clear()
    setChosenBall(None)
    moreBallsThanExpected()


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
        moreBallsThanExpected()
        ball = chooseBall(balls)

        if len(singleton.Singleton.way_points) == 0:
            waypoint.waypoints(ball)
            waypoints = singleton.Singleton.way_points
            visionOutputView.showImage()
            if len(singleton.Singleton.way_points) is not 0:
                print("List af wawypoints: " + str(singleton.Singleton.way_points))
                print("waypoint x: " + str(waypoints[0].x))
        numberOfBalls = numberOfBallsLeft()

        if not numberOfBalls == 0 and not zeroBallsLeft:
            angle = calculateAngle((waypoints[0].x, waypoints[0].y), robot)
            if numberOfBalls == 6 and sixBallsLeft:
                sixBallsLeft = False
                goForGoal(numberOfBalls)
            elif numberOfBalls == 2 and twoBallsLeft:
                twoBallsLeft = False
                goForGoal(numberOfBalls)
            else:
                if len(waypoints) > 1:
                    if math.sqrt(pow(robot.centrumX - waypoints[0].x, 2) + pow(robot.centrumY - waypoints[0].y, 2)) < track.pixelConversion * 5:
                        print("\033[1;33m" + "DIST TO WAYPOINT IS TOO SMALL, DROPPING WAYPOINT" + "\033[0m")
                        waypoint.pop_waypoint()
                if not angle < 5:
                    robotController.turn(angle, getclockWise(), turnSpeed)
                    numberOfTries = numberOfTries + 1
                    print("PRØVER AT TURNE TIL PUNKT")
                elif (distanceToBall(waypoints[0], robot) / pix_pr_cm) > distanceCutOffPoint:
                    #Drive forward to waypoint/ball
                    # robotController.drive_forward(robot.x, robot.y, waypoint.x, waypoint.y, pix_pr_cm, forwardSpeed)
                    # print("Foran drive")
                    if len(waypoints) > 1:
                        if singleton.Singleton.is_in_obstacle:
                            print("dist to ball: " + str(distanceToWaypoint([waypoints[0].x, waypoints[0].y], [robot.centrumX, robot.centrumY]) / pix_pr_cm))
                            print("MERE END 1 WAYPOINT TILBAGE")
                            print("Antal af Waypoints: " + str(len(waypoints)))
                            robotController.drive_forward(
                                distanceToWaypoint([waypoints[0].x, waypoints[0].y], [robot.centrumX, robot.centrumY]),
                                pix_pr_cm, forwardSpeed)
                            waypoint.pop_waypoint()
                            print("POPPER ET WAYPOINT")
                            print("Antal af Waypoints: " + str(len(waypoints)))
                        else:
                            print("dist to ball: " + str(distanceToWaypoint([waypoints[0].x, waypoints[0].y], [robot.centrumX, robot.centrumY]) / pix_pr_cm))
                            print("MERE END 1 WAYPOINT TILBAGE")
                            print("Antal af Waypoints: " + str(len(waypoints)))
                            robotController.drive_forward(distanceToWaypoint([waypoints[0].x, waypoints[0].y], [robot.centrumX, robot.centrumY]), pix_pr_cm, forwardSpeed)
                            waypoint.pop_waypoint()
                            print("POPPER ET WAYPOINT")
                            print("Antal af Waypoints: " + str(len(waypoints)))
                    else:
                        print("dist to ball: " + str(distanceToBall(waypoints[0], robot) / pix_pr_cm))
                        print("1 WAYPOINT TILBAGE")
                        print("Antal af Waypoints: " + str(len(waypoints)))
                        robotController.drive_forward(distanceToBall(waypoints[0], robot) - distanceCutOffPoint * pix_pr_cm + pix_pr_cm * 10, pix_pr_cm, forwardSpeed)
                    # waypoint.pop_waypoint()
                elif (distanceToBall(waypoints[0], robot) / pix_pr_cm) <= distanceCutOffPoint:
                    print("ER UNDER CUTOFFPOINTET")
                    # degrees = robotController.drive_degrees(distanceToBall(ball, robot), pix_pr_cm)
                    # print("degrees" + str(degrees))
                    if len(waypoints) > 1:
                        dist = distanceToWaypoint((waypoints[0].x, waypoints[0].y), (robot.centrumX, robot.centrumY))
                        robotController.drive_forward(dist, pix_pr_cm, slow_forwardSpeed)
                    else:
                        dist = distanceToBall(waypoints[0], robot)
                        robotController.drive_forward(round(math.fabs(dist - 40)), pix_pr_cm, slow_forwardSpeed)
                    if len(waypoints) == 1:
                        if singleton.Singleton.is_dangerous:
                            #TODO might need to be added again
                            # robotController.drive_forward(-5 * pix_pr_cm, pix_pr_cm, slow_forwardSpeed)
                            robotController.createCommandWall(15, 110, 600, 400)
                            if singleton.Singleton.wallOnLeftCorner:
                                robotController.createCommandTank(-40, -30, 400)
                                singleton.Singleton.wallOnLeftCorner = False
                            if singleton.Singleton.wallOnRightCorner:
                                robotController.createCommandTank(-30, -40, 400)
                                singleton.Singleton.wallOnRightCorner = False
                            setChosenBall(None)
                            # robotController.drive_forward(-15 * pix_pr_cm, pix_pr_cm, slow_forwardSpeed)
                        elif singleton.Singleton.is_in_obstacle:
                            robotController.drive_forward(-5 * pix_pr_cm, pix_pr_cm, slow_forwardSpeed)
                            print("Før cross attack")
                            robotController.createCommandCrossAttack(15, 110, 15, 600, 360)
                            print("Cross attack")
                            robotController.createCommandTank(-slow_forwardSpeed, -slow_forwardSpeed, 360)
                            setChosenBall(None)
                            # robotController.drive_forward(-15 * pix_pr_cm, pix_pr_cm, slow_forwardSpeed)
                            singleton.Singleton.is_in_obstacle = False
                        else:
                            robotController.createCommandAttack(attackSpeed, 200, frontArmDegrees)
                            setChosenBall(None)
                        # robotController.createCommandAttack(attackSpeed, degrees, frontArmDegrees)
                    waypoint.pop_waypoint()
        else:
            #no balls left
            if zeroBallsLeft:
                timer.cancel()
                end = time.time()
                run_time = end - start
                min_run = math.floor(run_time/60)
                sec_run = run_time % 60
                print("\033[1;33m" + "Time: " + str(min_run) + " min " + str(sec_run) + " sec")
                print("\n\n\nRobot is Done!!!\n\n\n")
                print("\033[0m")
                while True:
                    #Play sound to mark it is done
                    robotController.createCommandSound()
            else:
                zeroBallsLeft = True
                goForGoal(numberOfBalls)


    # visionController.releaseImage()









if __name__ == "__main__":
    main()
