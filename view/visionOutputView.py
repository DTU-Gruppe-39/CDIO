import cv2
import numpy as np
from model import Track


def showImage(img, track):

    #--Draw border-lines--#
    # Convert corners tuples:
    bottomLineA = (Track.Track.bottomLeftCorner.x, Track.Track.bottomLeftCorner.y)
    bottomLineB = (Track.Track.bottomRightCorner.x, Track.Track.bottomRightCorner.y)
    leftLineA = (Track.Track.bottomLeftCorner.x, Track.Track.bottomLeftCorner.y)
    leftLineB = (Track.Track.topLeftCorner.x, Track.Track.topLeftCorner.y)
    rightLineA = (Track.Track.bottomRightCorner.x, Track.Track.bottomRightCorner.y)
    rightLineB = (Track.Track.topRightCorner.x, Track.Track.topRightCorner.y)
    topLineA = (Track.Track.topRightCorner.x, Track.Track.topRightCorner.y)
    topLineB = (Track.Track.topLeftCorner.x, Track.Track.topLeftCorner.y)

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
    bigGoal = (Track.Track.bigGoal.x, Track.Track.bigGoal.y)
    smallGoal = (Track.Track.smallGoal.x, Track.Track.smallGoal.y)

    cv2.circle(img, bigGoal, 7, (255, 255, 255), -1)
    cv2.circle(img, smallGoal, 7, (255, 255, 255), -1)

    # cv2.imshow('frame', img)
    cv2.imshow("images", np.hstack([img]))
