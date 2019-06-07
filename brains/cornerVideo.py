import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 1)


boundaries = [
    ([60, 40, 40], [86, 255, 255]),
    # ([86, 0, 0], [255, 0, 0])
]

while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    points = []

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(hsv, hsv, mask=mask)



    # find contours in the thresholded image
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    count = 0

    # loop over the contours
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        count = count + 1
        print(str(count))
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            print("count: " + str(count) + " cX: " + str(cX) + " cY: " + str(cY))

            # draw the contour and center of the shape on the image
            cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
            cv2.circle(img, (cX, cY), 3, (255, 255, 255), -1)
            cv2.putText(img, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # print("X: " + str(cX))
            # print("Y: " + str(cY))

            # Top right corner
            if cX > 800 & cY > 500:
                points.insert(2, [cX, cY])

            # Bottom left corner
            elif cX < 800 & cY > 500:
                points.insert(3, [cX, cY])

            # Bottom right corner
            elif cX < 800 & cY < 500:
                points.insert(0, [cX, cY])

            # Top left corner
            elif cX > 800 & cY < 500:
                points.insert(1, [cX, cY])

            # Add points to array of points
            # points.append([cX, cY])


    if points.count() == 4:
        # Draw bottom line, 180 cm
        cv2.line(img, tuple(points[3]), tuple(points[0]), (0, 255, 0), thickness=3, lineType=8)
        # # Draw left line, 120 cm
        cv2.line(img, tuple(points[3]), tuple(points[1]), (0, 255, 0), thickness=3, lineType=8)
        # # Draw right line, 120 cm
        cv2.line(img, tuple(points[2]), tuple(points[0]), (0, 255, 0), thickness=3, lineType=8)
        # # Draw top line, 180 cm
        cv2.line(img, tuple(points[1]), tuple(points[2]), (0, 255, 0), thickness=3, lineType=8)

    # Punkters lokation i points array [nederst venstre, nederst højre, øverst højre, øverst venstre]
    # print(points)

    # npPoints = np.array((points[0], points[1], points[2], points[3]), np.int32)
    #
    # npPoints = npPoints.reshape((-1, 1, 2))
    # print(points)
    #
    # cv2.polylines(img, [npPoints], True, (255, 255, 255), thickness=3, lineType=8)

    # show the images
    cv2.namedWindow('images', cv2.WINDOW_NORMAL)
    cv2.imshow("images", np.hstack([img, output]))
    cv2.resizeWindow('images', 1400, 1000)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
