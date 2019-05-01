"""Funktioner og klasser relateret til billed-genkendelse"""

import numpy as np
import cv2
import threading
import time
import random
import brains.globals as globals



class Ball():
    """Ball der er blevet genkendt"""
    def __init__(self, xpos, ypos, radius):
        self.ballid = random.randint(10000, 99999) #5-cifret ballid - lad os håbe de ikke bliver ens
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius


def ballCheck(ballarr, xpos, ypos, radius):
    """Tjekker om bolden er blevet genkendt før - returnere et Ball-objekt hvis den er ny"""
    #TODO: Threshold for positionen
    for i in ballarr:
        if i.xpos == xpos and i.ypos == ypos:
            return None

    ball = Ball(xpos, ypos, radius)
    return ball


def imageCaptureBalls(ballarr):
    """Funktion der bruger OpenCV til at lokalisere bolde på banen"""
    time.sleep(1)
    cap = cv2.imread('image.png')
    # Capture frame-by-frame
    #ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 10, param1=150, param2=40, minRadius=1, maxRadius=120)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:

            center = (i[0], i[1])
            # der tegnes cirkel i center af boldene
            cv2.circle(gray, center, 1, 50, 5)
            #og outline
            radius = i[2]
            xpos,ypos = center
            cv2.circle(gray, center, radius, 0, 5)
            cv2.line(gray, center, (300, 300), 0, 5)
            ball = ballCheck(ballarr, i[0], i[1], i[2])
            if ball != None:
                ballarr.append(ball)

        print("Numballs", len(ballarr))
        for b in ballarr:
            print("Ballid:", b.ballid, "Xpos:", b.xpos, "Ypos", b.ypos, "Radius: ", b.radius)


    #Display the resulting frame
    if globals.MODE == "gfx" or globals.MODE == "gfxdebug":
        cv2.imshow('frame', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
