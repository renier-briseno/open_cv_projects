import numpy as np
import cv2
import os

current_dir = os.path.dirname(__file__)
image_dir = current_dir + "/assets/squares.jpg"


img = cv2.imread(image_dir, -1)
img = cv2.resize(img, None, fx=.17, fy=.17)

#converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# goodfeatures(scr, Num_of_corners to return, confidence(0-1), min Euclidean distance between corners)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.50, 10 )

#We can note that these "corner" items are floating point values
print(corners)

#Converting the corners to integers
corners = np.int0(corners)

#Flattening and returning corner components
for corner in corners:
    x, y = corner.ravel()
    #Plotting circles over each corner
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)


"""
Uncommenting the code below will draw lines between all detected corners
"""
# for i in range(len(corners)):
#     for j in range(i+1, len(corners)):
#         corner1 = tuple(corners[i][0])
#         corner2 = tuple(corners[j][0])
#         color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
#         cv2.line(img, corner1, corner2, color, 1)


#Displaying image
cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
