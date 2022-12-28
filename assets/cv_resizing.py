import cv2

Linus = cv2.imread(r".\Linypoo.JPEG", -1)

"""
-1, cv2.IMREAD_COLOR : Loads a color image, transperency neglected (by default flag)
0, cv2.IMREAD_GRAYSCALE : Loads in grayscale
1, cv2.IMREAD_UNCHANGED : Loads image as such including all pixels alpha channel (transparency)
"""
#Resizing (exact)
#Linus = cv2.resize(Linus, (400, 400))

#Rotating first,
Linus = cv2.rotate(Linus, cv2.ROTATE_90_CLOCKWISE)


#Resizing (proportion)
Linus = cv2.resize(Linus, (0, 0), fx=0.20, fy=0.17)

#Writing an image
cv2.imwrite('new_linus.jpg', Linus)


#Display
cv2.imshow("Bruh", Linus)
cv2.waitKey(0)
cv2.destroyAllWindows()