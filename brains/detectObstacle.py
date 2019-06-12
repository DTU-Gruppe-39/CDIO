import cv2
import math
import imutils
import numpy as np
import brains.singleton as singleton
from model import obstacle


def getObstacle(img):

    tempObstacle = obstacle.Obstacle

    tempTrack = singleton.Singleton.track


    LenghtX = tempTrack.topRightCorner.x - tempTrack.topLeftCorner.x
    LenghtY = tempTrack.topRightCorner.y - tempTrack.topLeftCorner.y

    HeightX = tempTrack.topRightCorner.x - tempTrack.bottomLeftCorner.x
    HeightY = tempTrack.topRightCorner.y - tempTrack.bottomLeftCorner.y

    trackLenght = math.sqrt(pow(LenghtX, 2) + pow(LenghtY, 2))
    trackHeight = math.sqrt(pow(HeightX, 2) + pow(HeightY, 2))
    print("trackLenght: " + str(trackLenght))

    cropX = int(tempTrack.topLeftCorner.x + trackLenght/10)
    cropY = int(tempTrack.topLeftCorner.y - trackLenght/10)

    cropLenghtX = int((trackLenght/10) * 8)
    cropLenghtY = int((trackHeight/10) * 8)

    # crop image
    crop = img[cropX:cropLenghtX, cropY:cropLenghtY]
    cv2.imshow("image", img)
    cv2.imshow("cropped", crop)

    blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    img_hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0, 100, 20])
    upper_red = np.array([6, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([176, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    mask = mask0 + mask1

    # set my output img to zero everywhere except my mask
    output_img = img.copy()
    output_img[np.where(mask == 0)] = 0

    # or your HSV image, which I *believe* is what you want
    output_hsv = img_hsv.copy()
    output_hsv[np.where(mask == 0)] = 0

    # show the images
    cv2.namedWindow('images', cv2.WINDOW_NORMAL)
    cv2.imshow("images", np.hstack([img, output_hsv]))
    cv2.resizeWindow('images', 1400, 1000)
