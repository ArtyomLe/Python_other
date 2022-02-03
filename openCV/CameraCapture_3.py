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

#=============================================================================================
