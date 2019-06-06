import numpy as np
import cv2
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FPS, 80)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 10, param1=150, param2=14, minRadius=1, maxRadius=20)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(gray, center, 1, (0, 100, 100), 5)
            # circle outline
            radius = i[2]
            cv2.circle(gray, center, radius, (255, 0, 255), 3)

    # Display the resulting frame
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()