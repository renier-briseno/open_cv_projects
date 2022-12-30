import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)


    image = np.zeros(frame.shape, dtype = np.uint8)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    
    """
    Below is another algorithm to multiply the number of captures 
    When tried, we note a substantial amount of lag
    Although this algorithm is essentially doing the same thing,
    we can see the Runtime Complexity of it is O(n^2) since we
    are writing every pixel by a doube for loop,  whereas
    the Runtime Complexity of the above algorithm is O(n)
    (Need 4 operations to slice the screen 4 ways, 16 operations
    to slice the screen into 16ths, etc.)
    """
    # for j in range(frame.shape[0]):
    #     for i in range(frame.shape[1]):
    #         image[j][i] = smaller_frame[j % smaller_frame.shape[0]][i % smaller_frame.shape[1]]

    cv2.imshow('videocam', image)
    

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
