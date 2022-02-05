import numpy as np
import cv2

img = cv2.imread('soccer_practice.jpg', 0)       # Источник для поиска (картинка)
template = cv2.imread('ball.png', 0)             # ВАЖНО чтобы образцы для поиска были такого же размера как на оригинале (по пикселям)
h,w = template.shape

# Список методов для определения искомого объекта на изображении
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# С помощью цикла пробегаемся по всем методам для определения наилучшего в данной ситуации
for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
