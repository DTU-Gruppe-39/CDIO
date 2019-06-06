import cv2
import imutils
import numpy as np

img = cv2.imread("/Users/thomasmattsson/Documents/GitHub/CDIO/Test_images/ImageOfBane2.jpg")
img = cv2.resize(img, (960, 540))

#

boundaries = [
    ([36, 30, 30], [86, 255,255]),
    # ([86, 0, 0], [255, 0, 0])
]

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(hsv, hsv, mask=mask)

    # show the images
    cv2.imshow("images", np.hstack([img, output]))

#h, s, v = cv2.split(mask)

cv2.imshow("gray-image",mask)

#Get coordinates that are in mask
coord = cv2.findNonZero(mask)

# find contours in the thresholded image
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#print(coord)

# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 3, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show the image
    ##cv2.waitKey(0)
    print("X: " + str(cX))
    print("Y: " + str(cY))

cv2.imshow("Image", img)

#cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
