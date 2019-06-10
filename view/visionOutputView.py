import cv2
import numpy as np

def showImage(img):

    # cv2.imshow('frame', img)
    cv2.imshow("images", np.hstack([img]))
