import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture('/Users/thomasmattsson/Documents/GitHub/CDIO/Test_images/bane_video.mp4')
cap.set(cv2.CAP_PROP_FPS, 24)


boundaries = [
    ([60, 40, 40], [86, 255, 255]),
    # ([86, 0, 0], [255, 0, 0])
]

while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    img_hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0, 70, 70])
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

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
