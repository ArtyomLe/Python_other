import numpy as np
import cv2

cap = cv2.VideoCapture(0)           # Индекс веб камеры

while True:
    ret, frame = cap.read()
    cv2.imshow('WebCamera', frame)
    if cv2.waitKey(1) == ord('q'):  # Читать кадры с камеры пока не нажата клавиша q
        break
cap.release()
cv2.destroyAllWindows()

#=================================== Делим окно на четыре зоны отображения ===================================
import numpy as np
import cv2

cap = cv2.VideoCapture(0)           # Индекс веб камеры

while True:
    ret, frame = cap.read()         # Читаем кадры
    width = int(cap.get(3))         # Находим ширину окна
    height = int(cap.get(4))        # Находим высоту окна

    image = np.zeros(frame.shape, np.uint8) # Создаём окно для отображения видеоряда
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # Урезаем изображение вдвое
    image[:height // 2, :width // 2] = smaller_frame   # Отображаем в верхнем левом окне
    image[height // 2:, :width // 2] = smaller_frame   # Отображаем в нижнем левом окне
    image[:height // 2, width // 2:] = smaller_frame   # Отображаем в верхнем правом окне
    image[height // 2:, width // 2:] = smaller_frame   # Отображаем в нижнем правом окне

    cv2.imshow('WebCamera', image)  # Отображаем окно видеоряда
    if cv2.waitKey(1) == ord('q'):  # Читать кадры с камеры пока не нажата клавиша q
        break
cap.release()
cv2.destroyAllWindows()

#====================================Поворачиваем кажое из разделённых окон==================

