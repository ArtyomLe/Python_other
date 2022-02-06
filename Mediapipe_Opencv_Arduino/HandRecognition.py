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
#===========================================Финальная версия==============================

