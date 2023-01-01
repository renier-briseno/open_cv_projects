import numpy as np
import cv2

#Accessing default Camera resource
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Converting frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Setting range for blue detection
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Creating mask for the color blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Applying mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", result)
    #cv2.imshow("mask", mask)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

