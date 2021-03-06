import cv2
from dao import singleton


def showImage():

    img = singleton.Singleton.img
    track = singleton.Singleton.track
    balls = singleton.Singleton.balls
    robot = singleton.Singleton.robot

    obstacle = singleton.Singleton.obstacle
    safePoints = singleton.Singleton.safe_points
    danger = round(track.pixelConversion * 15)

    #--Draw border-lines--#
    # Convert corners tuples:
    bottomLineA = (track.bottomLeftCorner.x, track.bottomLeftCorner.y)
    bottomLineB = (track.bottomRightCorner.x, track.bottomRightCorner.y)
    leftLineA = (track.bottomLeftCorner.x, track.bottomLeftCorner.y)
    leftLineB = (track.topLeftCorner.x, track.topLeftCorner.y)
    rightLineA = (track.bottomRightCorner.x, track.bottomRightCorner.y)
    rightLineB = (track.topRightCorner.x, track.topRightCorner.y)
    topLineA = (track.topRightCorner.x, track.topRightCorner.y)
    topLineB = (track.topLeftCorner.x, track.topLeftCorner.y)


    if singleton.Singleton.chosenBall is not None:
        cv2.line(img, (singleton.Singleton.robot.centrumX, singleton.Singleton.robot.centrumY),
                 (singleton.Singleton.chosenBall.x, singleton.Singleton.chosenBall.y), (0, 0, 255), 2)

    if len(singleton.Singleton.way_points) != 0:
        cv2.line(img, (singleton.Singleton.robot.centrumX, singleton.Singleton.robot.centrumY),
                 (int(singleton.Singleton.way_points[0].x), int(singleton.Singleton.way_points[0].y)), (0, 255, 0), thickness=3, lineType=8)
        count = 0
        for wp in singleton.Singleton.way_points:
            cv2.circle(img, (int(wp.x), int(wp.y)), 3, (255, 0, 0), 5)
            cv2.putText(img, "WP: " + str(count), (int(wp.x), int(wp.y)), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (255, 255, 255), 2)
            count +=1

    if track.bottomLeftCorner.x is not None:
        # Draw bottom line, 180 cm
        cv2.line(img, bottomLineA, bottomLineB, (0, 255, 0), thickness=3, lineType=8)
        # # Draw left line, 120 cm
        cv2.line(img, leftLineA, leftLineB, (0, 255, 0), thickness=3, lineType=8)
        # # Draw right line, 120 cm
        cv2.line(img, rightLineA, rightLineB, (0, 255, 0), thickness=3, lineType=8)
        # # Draw top line, 180 cm
        cv2.line(img, topLineA, topLineB, (0, 255, 0), thickness=3, lineType=8)


    #--Draw goals--#
    # Convert to tuple
    bigGoal = (track.bigGoal.x, track.bigGoal.y)
    smallGoal = (track.smallGoal.x, track.smallGoal.y)

    if track.bottomLeftCorner.x is not None:
        cv2.circle(img, bigGoal, 7, (255, 255, 255), -1)
        cv2.circle(img, smallGoal, 7, (255, 255, 255), -1)


    #--Draw balls--#

    for ball in balls:
        center = (ball.x, ball.y)
        cv2.circle(img, center, 1, (0, 100, 100), 5)
        # circle outline
        cv2.circle(img, center, ball.radius, (255, 0, 255), 3)

    if robot.blSquareX is not None:
        # contour point
        cv2.circle(img, (robot.blSquareX, robot.blSquareY), 3, 255, -1)

        # center of robot
        cv2.circle(img, (robot.centrumX, robot.centrumY), 4, 255, -1)
        cv2.putText(img, "Robo bot", (robot.centrumX, robot.centrumY), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        # drawing robot outline
        cv2.drawContours(img, [robot.box], 0, (0, 255, 0), 2)

        # danger zone
        cv2.line(img, (bottomLineA[0] + danger, bottomLineA[1] - danger), (bottomLineB[0] - danger ,bottomLineB[1] - danger), (0,0,255), 2)
        cv2.line(img, (topLineA[0] - danger, topLineA[1] + danger), (topLineB[0] + danger, topLineB[1] + danger),(0, 0, 255), 2)
        cv2.line(img, (rightLineA[0] - danger, rightLineA[1] - danger), (rightLineB[0] - danger, rightLineB[1] + danger),(0, 0, 255), 2)
        cv2.line(img, (leftLineA[0] + danger, leftLineA[1] - danger), (leftLineB[0] + danger, leftLineB[1] + danger),(0, 0, 255), 2)


    # Draw obstacle
    if obstacle.center_x is not None:
        cv2.circle(img, (obstacle.center_x, obstacle.center_y), 4, 255, -1)

        count = 0
        index = 0
        for sp in safePoints:
            if count == 0:
                x = obstacle.bottom_line
            elif count == 1:
                x = obstacle.top_line
            elif count == 2:
                x = obstacle.left_line
            elif count == 3:
                x = obstacle.right_line

            # Draw safepoints
            cv2.circle(img, (int(sp.x) ,int(sp.y)), 4, (255, 255, 255), -1)

            # Draw dangerzone lines
            a = (int(list(x.coords)[index][0]), int(list(x.coords)[index][1]))
            index += 1
            b = (int(list(x.coords)[index][0]), int(list(x.coords)[index][1]))
            index -= 1
            cv2.line(img, a, b, (255, 255, 255), 2)
            count += 1

        # robot to ball line
        # cv2.line(img, (robot.x, robot.y), (ball.x, ball.y), (0, 0, 255), 1)

    # cv2.imshow('frame', img)

    # y_val1 = len(np.amax(img, axis=1))
    # x_val1 = len(np.amax(img, axis=0))
    # y_val = int(y_val1/ 2)
    # x_val = int(x_val1 / 2)
    #
    # cv2.line(img, (x_val, 0), (x_val, y_val1), (0,0,255), 2)

    scale_percent = 30  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


    cv2.imshow("images", resized)
