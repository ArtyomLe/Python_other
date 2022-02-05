import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # Haar cascade(face)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')                   # Haar cascade(eye)

while True:
    ret, frame = cap.read()

    # Для использования этого алгоритма переопределяем цветовое пространство источника
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Определение лица
    for (x, y, w, h) in faces:                          # Обвод синим квадратом
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 5)
        artyom_gray = gray[y:y+w, x:x+w]
        artyom_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(artyom_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:                    # eyeX, eyeY, eyeWIDTH, eyeHEIGHT
            cv2.rectangle(artyom_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 5)

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
