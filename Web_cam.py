# Установка библиотеки (pip install opencv-python)
# ================= Версия для подключённой по usb web камере =====================
import cv2

cap = cv2.VideoCapture(0)         # Индекс веб камеры

while True:
    ret, img = cap.read()         # Считываем изображение
    cv2.imshow("camera", img)     # Отображаем изображение
    if cv2.waitKey(10) == 27:     # каждые 10 секунд опрашиваем клавишу esp для выхода из цикла
        break

cap.release()
cv2.destroyAllWindows()

# ================= Версия для ip web камеры ==============================
import cv2

cap = cv2.VideoCapture('rtsp://username:password@ip-address:port/unicast')

while True:
    ret, image = cap.read()
    cv2.imshow("Test", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # каждые 10 секунд опрашиваем клавишу q для выхода из цикла
        break
cv2.destroyAllWindows()
