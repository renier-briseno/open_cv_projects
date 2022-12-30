import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))


    # Drawing lines on screen
    """
    #(which array, start, end, color, thickness)
    img = cv2.line(frame, (0, 0), (width, height), (255,0,0), 1)

    img = cv2.line(img, (0, height), (width, 0), (0,255,0), 1)
    """
    
    #Drawing rectangle on image
    """
    # (which array, (topleft, bottomright), (color), thickness or fill(-1))
    img = cv2.rectangle(frame, (100, 100), (200, 200), (128,128,128), 5)
    """

    #Drawing Circle on image
    """
    # (frame, (center coor), radius, (color), thickness )
    img = cv2.circle(frame, (300, 300), 60, (0, 0, 255), -1)
    """

    #Drawing text on image
    # Creating font
    font = cv2.FONT_HERSHEY_SIMPLEX
    #(frame, text,  bottomleft, font, font_scale, (color), 5, linetype=cv2.LINE_AA)
    img = cv2.putText(frame, "BOTTOM TEXT", (width//6, 50), font, 2, (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow("Cam", img)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()