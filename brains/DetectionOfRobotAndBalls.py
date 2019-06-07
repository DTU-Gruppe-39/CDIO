import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 24)
cv2.namedWindow("test")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=500, param2=26, minRadius=1, maxRadius=20)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    boundaries = [
        # ([119, 182, 143], [136, 199, 169]),
        ([0, 230, 230], [130, 255, 255])  # Robot yellow
        # ([0, 150, 0], [150, 255, 150]) #Bander red
        # ([86, 0, 0], [255, 0, 0])

    ]

    # roed: ([17, 15, 100], [50, 56, 200])
    # blaa: ([86, 31, 4], [220, 88, 50]),
    # gul: ([25, 146, 190], [62, 174, 250])
    # graa: ([103, 86, 65], [145, 133, 128])

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(frame, center, 1, (0, 100, 100), 5)
            # circle outline
            radius = i[2]
            cv2.circle(frame, center, radius, (255, 0, 255), 3)

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)


        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(output, center, 1, (0, 100, 100), 5)
                # circle outline
                radius = i[2]
                cv2.circle(output, center, radius, (255, 0, 255), 3)

    # show the images
    cv2.imshow("images", np.hstack([frame, output]))

    # Display the resulting frame
    #cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()









