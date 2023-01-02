import cv2
import numpy as np
import os


current_path = os.path.dirname(__file__)
print(current_path)
img = cv2.imread(current_path + "/assets/soccer_game.jfif", 0)

# Here we can uncomment which template we would like to use (which object to find)
template = cv2.imread(current_path + "/assets/ball_template.png", 0)
#template = cv2.imread(current_path + "/assets/patch_template.png", 0)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
 cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img_copy = img.copy()

    #Result in size (base_width - templ_wid + 1, base_Height - templ_height +1)
    result = cv2.matchTemplate(img_copy, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)

    #These use minimum value
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    #Other methods use max value
    else:
        location = max_loc

    bottom_right = (location[0]+w, location[1]+h)

    cv2.rectangle(img_copy, location, bottom_right, 0, 3)

    cv2.imshow("Match", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()