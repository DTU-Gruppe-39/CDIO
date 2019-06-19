import math
import brains.singleton as singleton
from model.ball import Ball
from model import point
from brains import waypoint


def getChosenBall():
    return singleton.Singleton.chosenBall


def is_ball_in_obstacle(endPoint):
    obstacle = singleton.Singleton.obstacle
    if obstacle.square_bottom_right_corner.x >= endPoint.x >= obstacle.square_top_left_corner.x and obstacle.square_bottom_right_corner.y >= endPoint.y >= obstacle.square_top_left_corner.y:
        return True
    else:
        return False


def getWaypoints():
    way_points = []
    if singleton.Singleton.chosenBall is not None:
        way_points = waypoint.waypoints(singleton.Singleton.chosenBall)
        return way_points
    else:
        return None

def setChosenBall(ball):
    singleton.Singleton.chosenBall = ball


def findBestBall(balls):
    robot = singleton.Singleton.robot
    track = singleton.Singleton.track

    minDist = 0
    dist = 0
    maxNumberOfTries = 5
    numberOfBallsLeft = len(singleton.Singleton.balls)
    danger = track.pixelConversion * 5
    ball_dist = []
    cornerSafePointX = track.pixelConversion * 3
    cornerSafePointY = track.pixelConversion * 12
    sideSafePoint = track.pixelConversion * 7
    tempBall = Ball
    firstBall = True

    print("Choose ball")
    # return ball
    if numberOfBallsLeft == 0:
        return None
    else:
        for ball in balls:
            dist = math.sqrt(pow(robot.centrumX - ball.x, 2) + pow(robot.centrumY - ball.y, 2))
            ball_point = point.Point(ball.x, ball.y)
            ball_dist.append((dist, ball_point))
            if minDist == 0:
                minDist = dist
                tempBall.x = ball.x
                tempBall.y = ball.y

            elif dist < minDist:
                minDist = dist
                tempBall.x = ball.x
                tempBall.y = ball.y
        ball_dist.sort()
        chosen_ball = ball_dist[0][1]
        
        if is_ball_in_obstacle(chosen_ball):
            chosen_ball = ball_dist[1][1]
            tempBall.x = chosen_ball.x
            tempBall.y = chosen_ball.y
            return tempBall
        elif firstBall:
            chosen_ball = ball_dist[1][1]
            tempBall.x = chosen_ball.x
            tempBall.y = chosen_ball.y
            firstBall = False
            return tempBall
        else:
            tempBall.x = chosen_ball.x
            tempBall.y = chosen_ball.y
            return tempBall
