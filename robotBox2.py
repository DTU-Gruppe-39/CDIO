import numpy as np
import imutils
import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("RobotWithMarkings.mov")
cap.set(cv2.CAP_PROP_FPS, 24)
cv2.namedWindow("test")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
#    frame = cv2.imread("../Test_images/ImageOfRobot8.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.medianBlur(gray, 3)
    rows = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=550, param2=17, minRadius=5, maxRadius=8)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # find contours in the thresholded image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)



    boundaries = [
        # ([119, 182, 143], [136, 199, 169]),
        #([0, 230, 230], [130, 255, 255])  # Robot yellow
        ([180, 0, 0], [255, 190, 50])
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


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(mask, 1, 2, cv2.THRESH_BINARY)[1]

        # find contours in the thresholded image
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)


        # M = cv2.moments(cnt)
       # print(M)

        # loop over the contours
        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)


            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                center = (cX, cY)
            else:
                # set values as what you need in the situationq
                cX, cY = 0, 0
            #
            # # draw the contour and center of the shape on the image


            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            point = cv2.circle(frame, (cX, cY), 1, (0, 255, 255), 2)
            print(cnts[1])
            cv2.line(frame, tuple(cnts[0][0], cnts[0][1]), tuple(cnts[1][0], cnts[1][1]), (0, 0, 255), 1)




        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(output, center, 1, (0, 100, 100), 5)

                # circle outline
                radius = i[2]
                cv2.circle(output, center, radius, (255, 0, 255), 3)


                x, y, w, h = cv2.boundingRect(mask)
                rect1 = cv2.rectangle(frame.copy(), (x - 15, y - 35), (x + w + 15, y + h + 35), (255, 0, 0), 2)
                cv2.circle(frame, (x + 10, y + 10), 5, (255, 255, 255), 1)
                cv2.putText(frame, "Robo bot", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                #cv2.line(frame, (x, y), (i[0], i[1]), (0, 0, 255), 1)



    # show the images
    cv2.imshow("images", np.hstack([rect1, output]))

    # Display the resulting frame
    #cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()






