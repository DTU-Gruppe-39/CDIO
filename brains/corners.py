import cv2
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

coord = cv2.findNonZero(mask)

print(coord)


#cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
