# Установка билиотеки через терминал (один из вариантов)
# pip install opencv-python
# pip3 install opencv-python
# python -m pip install opencv-python
# python3 -m pip install opencv-python


import cv2

img = cv2.imread('python_hero.jpg', 1)         # Режимы отображения (1, -1 ,0)
img  = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Отобразить половину от изначального размера
# img = cv2.resize(img, (400, 400))            # Отобразить в пикселях
img = cv2.rotate(img, cv2.cv2.ROTATE_180)      # Повернуть на 180 градусов

cv2.imwrite('new_img.jpg', img)                # Создать новый файл со всеми изменениями

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWIndows()
