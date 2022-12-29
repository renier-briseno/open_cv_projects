import cv2
import os

current_path = os.path.dirname(__file__)
os.chdir(current_path + "/assets")
file_path = current_path + "/assets/Linypoo.png"

Linus = cv2.imread(file_path, 1)

"""
-1, cv2.IMREAD_COLOR : Loads a color image, transperency neglected (by default flag)
0, cv2.IMREAD_GRAYSCALE : Loads in grayscale
1, cv2.IMREAD_UNCHANGED : Loads image as such including all pixels alpha channel (transparency)
# """
#Resizing (exact measure)
# Linus = cv2.resize(Linus, (700, 770))

#Rotating
# Linus = cv2.rotate(Linus, cv2.ROTATE_90_CLOCKWISE)


#Resizing (proportional measure)
Linus = cv2.resize(Linus, (0, 0), fx=.17, fy=.17)

#Writing an image
cv2.imwrite('new_linus.jpg', Linus)


#Display
cv2.imshow("Dog", Linus)
cv2.waitKey(0)
cv2.destroyAllWindows()