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

    cornerboundaries = [
        ([60, 40, 40], [86, 255, 255]),
        # ([86, 0, 0], [255, 0, 0])
    ]

    boundaries = [
        # ([119, 182, 143], [136, 199, 169]),
        # ([0, 230, 230], [130, 255, 255])  # Robot yellow
        # ([0, 150, 0], [150, 255, 150]) #Bander red
        ([150, 0, 0], [255, 165, 100])  # Robot blue
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

        ##########################################

        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

        hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

        points = []

        # loop over the boundaries
        for (clower, cupper) in cornerboundaries:
            # create NumPy arrays from the boundaries
            clower = np.array(clower, dtype="uint8")
            cupper = np.array(cupper, dtype="uint8")

            # find the colors within the specified boundaries and apply
            # the mask
            cmask = cv2.inRange(hsv, clower, cupper)
            coutput = cv2.bitwise_and(hsv, hsv, mask=cmask)

        # find contours in the thresholded image
        cnts = cv2.findContours(cmask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        count = 0

        # loop over the contours
        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)
            count = count + 1
            #print(str(count))
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                #print("count: " + str(count) + " cX: " + str(cX) + " cY: " + str(cY))

                # draw the contour and center of the shape on the image
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cX, cY), 3, (255, 255, 255), -1)
                cv2.putText(frame, "center", (cX - 20, cY - 20),
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

        if len(points) == 4:
            # Draw bottom line, 180 cm
            cv2.line(frame, tuple(points[3]), tuple(points[0]), (0, 255, 0), thickness=3, lineType=8)
            # # Draw left line, 120 cm
            cv2.line(frame, tuple(points[3]), tuple(points[1]), (0, 255, 0), thickness=3, lineType=8)
            # # Draw right line, 120 cm
            cv2.line(frame, tuple(points[2]), tuple(points[0]), (0, 255, 0), thickness=3, lineType=8)
            # # Draw top line, 180 cm
            cv2.line(frame, tuple(points[1]), tuple(points[2]), (0, 255, 0), thickness=3, lineType=8)

            ####Draw on output image
            # Draw bottom line, 180 cm
            cv2.line(output, tuple(points[3]), tuple(points[0]), (0, 255, 0), thickness=3, lineType=8)
            # # Draw left line, 120 cm
            cv2.line(output, tuple(points[3]), tuple(points[1]), (0, 255, 0), thickness=3, lineType=8)
            # # Draw right line, 120 cm
            cv2.line(output, tuple(points[2]), tuple(points[0]), (0, 255, 0), thickness=3, lineType=8)
            # # Draw top line, 180 cm
            cv2.line(output, tuple(points[1]), tuple(points[2]), (0, 255, 0), thickness=3, lineType=8)

        ##########################################




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









