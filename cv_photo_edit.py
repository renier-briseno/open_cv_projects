import cv2
import random
import os


linus = os.path.dirname(__file__)


#Note how it saves the image as a numpy array!
# We can print the type, or the array itself

# print(type(linus))

#Since this is a Numpy array, we can use all the numpy commands on it
print(linus.shape) # (3024, 4032, 3)

# (Height(rows), Columns(width), channels (bgr, none for grayscale etc))

# Looking at first row and individual pixels
print(linus[0][255])


for i in range(linus.shape[0]):
    for j in range(linus.shape[1]):
        if i < 25 or j < 25 or i > (linus.shape[0]-25) or j > (linus.shape[1]-25):
            linus[i][j] = [150, 0 , 250]


#cv2.imshow("Bruh", linus)
# cv2.waitKey(0)
# cv2.destroyAllWindows

print(linus.shape)

#150, 350, 20, 420

face = linus[150:450, 100:420]


linus[linus.shape[0]-300:linus.shape[0], linus.shape[1]-320:linus.shape[1]] = face


cv2.imshow("Bruh", linus)
cv2.waitKey(0)
cv2.destroyAllWindows





