import cv2
import random  # Заменяем на случайный цвет выбранные пиксели

img = cv2.imread('python_hero.jpg', -1)

# print (img.shape)
# (995, 845, 3)  (img.shape[0], img.shape[1], img.shape[2])
# (HEIGHT, WIDTH, CHANNELS)
#
# Each pixel:
# blue green red  (BGR)
# [0,    0,    0]
# 0-255 0-255 0-255

# (rows, columns, channels)
for i in range(200):                # rows HEIGHT
    for j in range(img.shape[1]):   # columns WIDTH (на всю ширину картинки)
        # Заменяем цвета в выбранных ячейках на случайные
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#============Вырезать/Вставить пиксели в заданном диапазоне ==============================
import cv2

img = cv2.imread('python_hero.jpg', -1)

# Кол-во пикселей должно быть ОДИНАКОВЫМ!
tag = img[500:700, 600:860]  # Вырезать пиксели в этом диапазоне
img[180:380, 620:880] = tag  # Вставить пиксели в этом диапазоне

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
