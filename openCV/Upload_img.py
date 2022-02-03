import cv2

img = cv2.imread('python_hero.jpg', 1)   # Опции для отображения (-1, 0, 1)
img = cv2.resize(img, (400, 400))

cv2.imshow('Image', img)
cv2.waitKey(0)                           # Закрыть окно
cv2.destroyAllWIndows()
