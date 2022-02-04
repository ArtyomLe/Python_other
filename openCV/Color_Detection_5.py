import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Конвертируем цветовое пространство из BGR в HSV
    # Определяем границы цвета пикселя для дальнейшего отображения
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Применяем маску and
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('camera', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
