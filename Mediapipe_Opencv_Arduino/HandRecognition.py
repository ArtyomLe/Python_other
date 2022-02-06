import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands        # Подключаем алгоритмы поиска рук
hands = mpHands.Hands()             # Hands обьект руки с настройками (можно поменять на одну руку)
mpDraw = mp.solutions.drawing_utils # Утилиты для рисования

while True:
    good, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)    # .process(один кадр) - поиск руки в кадре
    if results.multi_hand_landmarks:   # .multi_hand_landmarks - получаем точки на руке
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # .draw_landmarks - нарисовать по точкам

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break

        
#==============================Указываем точку на руке и определяем её координаты для дальнейшего управления=======================

import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands        # Подключаем алгоритмы поиска рук
hands = mpHands.Hands()             # Hands обьект руки с настройками
mpDraw = mp.solutions.drawing_utils # Утилиты для рисования

while True:
    good, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)    # .process(один кадр) - поиск руки в кадре
    if results.multi_hand_landmarks:   # .multi_hand_landmarks - получаем точки на руке
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # .draw_landmarks - нарисовать по точкам
            for id, point in enumerate(handLms.landmark): # enumerate() - получить индекс элемента и значение
                width, height, color = img.shape         # img.shape - узнаём размер кадра
                width, height = int(point.x * height), int(point.y * width)
                if id == 8:
                    cv2.circle(img, (width, height), 15, (0, 125, 225), -1) # Рисуем окружность на выбранной точке 8 (указ. палец)



    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
        
#============================================ Отправляем в порт =========================================================

import cv2
import mediapipe as mp
import serial

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands        # Подключаем алгоритмы поиска рук
hands = mpHands.Hands()             # Hands обьект руки с настройками
mpDraw = mp.solutions.drawing_utils # Утилиты для рисования

portNo = "COM9"                      # Порт для подключения ардуино
uart = serial.Serial(portNo, 9600)   # Скорость передачи данных

while True:
    good, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)    # .process(один кадр) - поиск руки в кадре
    if results.multi_hand_landmarks:   # .multi_hand_landmarks - получаем точки на руке
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # .draw_landmarks - нарисовать по точкам
            for id, point in enumerate(handLms.landmark): # enumerate() - получить индекс элемента и значение
                width, height, color = img.shape         # img.shape - узнаём размер кадра
                width, height = int(point.x * height), int(point.y * width)
                if id == 8:
                    cv2.circle(img, (width, height), 15, (225, 0, 225), -1) # Рисуем окружность на выбранной точке 8 (указ. палец)
                    
                    # Если точка найдена выводим её через протокол в ардуино
                    msg = '#' + str(width) + ';'
                    msg = bytes(str(msg), 'utf-8') # Кодировка текста (8 бит)
                    uart.write(msg) # Отправляем байты в шину serial




    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
#==========================================условие если сжат в кулак==============================================
import cv2
import mediapipe as mp
import serial

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands        # Подключаем алгоритмы поиска рук
hands = mpHands.Hands()             # Hands обьект руки с настройками
mpDraw = mp.solutions.drawing_utils # Утилиты для рисования

portNo = "COM9"                      # Порт для подключения ардуино
uart = serial.Serial(portNo, 9600)   # Скорость передачи данных
points = [0 for i in range(21)]

while True:
    good, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)    # .process(один кадр) - поиск руки в кадре
    if results.multi_hand_landmarks:   # .multi_hand_landmarks - получаем точки на руке
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # .draw_landmarks - нарисовать по точкам
            for id, point in enumerate(handLms.landmark): # enumerate() - получить индекс элемента и значение
                width, height, color = img.shape         # img.shape - узнаём размер кадра
                width, height = int(point.x * height), int(point.y * width)
                points[id] = height
                if id == 8:
                    cv2.circle(img, (width, height), 15, (225, 0, 225), cv2.FILLED) # Рисуем окружность на выбранной точке 8 (указ. палец)
            distance_0_5 = abs(points[0] - points[5])
            distance_0_8 = abs(points[0] - points[8])
            distanceGood = distance_0_5 + (distance_0_5/2)
            if distance_0_8 > distanceGood:
                # Если точка найдена и не кулак выводим её через протокол в ардуино
                msg = '#' + str(width) + ';'
                msg = bytes(str(msg), 'utf-8') # Кодировка текста (8 бит)
                uart.write(msg) # Отправляем байты в шину serial
                print(msg)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
#=========================================== ФИНАЛЬНАЯ ВЕРСИЯ =========================================
# Project from LabRazum

import cv2                              # библиотека opencv (получение и обработка изображения)
import mediapipe as mp                  # библиотека mediapipe (распознавание рук)
import serial                           # библиотека pyserial (отправка и прием информации)


camera = cv2.VideoCapture(0)            # получаем изображение с камеры (0 - порядковый номер камеры в системе)
mpHands = mp.solutions.hands            # подключаем раздел распознавания рук
hands = mpHands.Hands()                 # создаем объект класса "руки"
mpDraw = mp.solutions.drawing_utils     # подключаем инструменты для рисования


portNo = "COM8"                         # указываем последовательный порт, к которому подключена Arduino
uart = serial.Serial(portNo, 9600)      # инициализируем последовательный порт на скорости 9600 Бод


p = [0 for i in range(21)]              # создаем массив из 21 ячейки для хранения высоты каждой точки
finger = [0 for i in range(5)]          # создаем массив из 5 ячеек для хранения положения каждого пальца

# функция, возвращающая расстояние по модулю (без знака)
def distance(point1, point2):
    return abs(point1 - point2)


while True:
    good, img = camera.read()                                   # получаем один кадр из видеопотока
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)               # преобразуем кадр в RGB


    results = hands.process(imgRGB)                             # получаем результат распознавания
    if results.multi_hand_landmarks:                            # если обнаружили точки руки
        for handLms in results.multi_hand_landmarks:            # получаем координаты каждой точки

            # при помощи инструмента рисования проводим линии между точками
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # работаем с каждой точкой по отдельности
            # создаем список от 0 до 21 с координатами точек
            for id, point in enumerate(handLms.landmark):
                # получаем размеры изображения (окна) с камеры и масштабируем
                width, height, color = img.shape
                width, height = int(point.x * height), int(point.y * width)

                p[id] = height           # заполняем массив высотой каждой точки
                if id == 8:              # выбираем нужную точку
                    # рисуем нужного цвета кружок вокруг выбранной точки
                    cv2.circle(img, (width, height), 15, (255, 0, 255), cv2.FILLED)
                if id == 12:
                    cv2.circle(img, (width, height), 15, (0, 0, 255), cv2.FILLED)

            # получаем расстояние, с которым будем сравнивать каждый палец
            distanceGood = distance(p[0], p[5]) + (distance(p[0], p[5]) / 2)
            # заполняем массив 1 (палец поднят) или 0 (палец сжат)
            finger[1] = 1 if distance(p[0], p[8]) > distanceGood else 0
            finger[2] = 1 if distance(p[0], p[12]) > distanceGood else 0
            finger[3] = 1 if distance(p[0], p[16]) > distanceGood else 0
            finger[4] = 1 if distance(p[0], p[20]) > distanceGood else 0
            finger[0] = 1 if distance(p[4], p[17]) > distanceGood else 0

            # готовим сообщение для отправки
            msg = ''
            # 0 - большой палец, 1 - указательный, 2 - средний, 3 - безымянный, 4 - мизинец
            if not (finger[0]) and finger[1] and not (finger[2]) and not (finger[3]) and finger[4]:
                msg = '@'                    # rock&roll (жест "коза" - 01001)
            if finger[0] and not (finger[1]) and not (finger[2]) and not (finger[3]) and not (finger[4]):
                msg = '^'                    # like (10000)
            if not(finger[0]) and finger[1] and finger[2] and not(finger[3]) and not(finger[4]):
                msg = '$' + str(width) + ';' # victory (011000)
            if not(finger[0]) and finger[1] and not(finger[2]) and not(finger[3]) and not(finger[4]):
                msg = '#' + str(width) + ';' # pointer (010000)

            # отправляем сообщение в Arduino
            if msg != '':
                msg = bytes(str(msg), 'utf-8') # Кодировка текста (8 бит)
                uart.write(msg)                # Отправляем байты в шину serial
                print(msg)                     # Для отладки (необязательно)

    cv2.imshow("Image", img)           # выводим окно с нашим изображением
    if cv2.waitKey(1) == ord('q'):     # ждем нажатия клавиши q в течение 1 мс
        break                          # если нажмут, всё закрываем
