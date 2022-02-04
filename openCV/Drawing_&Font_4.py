import numpy as np
import cv2

cap = cv2.VideoCapture(0) #'rtsp://artyom:5497336@192.168.1.113:8554/unicast'

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)   # Параметры линии (источник, начало координат, конец координат, цвет, толщина линии)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128,128,0), 5)  # Квадрат
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)            # Круг

    cv2.imshow('camera', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#============================ФИГУРЫ И ТЕКСТ=======================================

import numpy as np
import cv2

cap = cv2.VideoCapture(0) #'rtsp://artyom:5497336@192.168.1.113:8554/unicast'

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Начало координат в левом ВЕРХНЕМ углу
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)   # Параметры линии (источник, начало координат, конец координат, цвет, толщина линии)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128,128,0), 5)  # Квадрат
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)            # Круг

    font = cv2.FONT_HERSHEY_SIMPLEX                                   # Font
    img = cv2.putText(img, 'ArtyomLe!', (240, 120), font, 1, (64, 180, 155), 2, cv2.LINE_AA)

    cv2.imshow('camera', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
