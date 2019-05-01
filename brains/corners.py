import cv2
import numpy as np

img = cv2.imread("image2.jpg")
img = cv2.resize(img, (960, 540))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([12,100,58])
upper_red = np.array([36,80,58])

mask = cv2.inRange(hsv, lower_red, upper_red)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 150, 0.01, 10, mask)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 255, 0), -1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
