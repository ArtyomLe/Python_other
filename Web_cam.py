import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()         # Считываем изображение
    cv2.imshow("camera", img)     # Отображаем изображение
    if cv2.waitKey(10) == 27:     # каждые 10 секунд опрашиваем клавишу esp для выхода из цикла
        break

cap.release()
cv2.destroyAllWindows()