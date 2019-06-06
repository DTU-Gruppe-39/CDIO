import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 24)
cv2.namedWindow("test")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #cv2.imshow("test", frame)

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

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)

        # show the images
        cv2.imshow("images", np.hstack([frame, output]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()









