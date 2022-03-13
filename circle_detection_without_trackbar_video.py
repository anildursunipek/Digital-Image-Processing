import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
transactionsNumber = 0
totalFps = 0
while cap.isOpened():
    start = time.time()
    ret, frame = cap.read()
    if not ret:
        print("Görüntü Okunamadı")
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3.5)
    cv2.imshow('Deneme', th)


    circles = cv2.HoughCircles(th, cv2.HOUGH_GRADIENT, 1.1, 120 , param1=70, param2=35, minRadius=30, maxRadius=130)

    if circles is not None:
        circles_round = np.uint16(np.around(circles))
        for i in circles_round[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (50, 200, 200), 5)
            cv2.circle(frame, (i[0], i[1]), 2, (255, 0, 0), 3)

    cv2.imshow('resim', frame)
    end = time.time()
    fps = 1 / (end - start)
    transactionsNumber += 1
    totalFps += fps
    avarageFps = totalFps / transactionsNumber
    print('Avarage Fps: ',round(avarageFps,1))
    print('İnstant Fps: ',round(fps,1))
    print('Number of transactions: ',transactionsNumber,'\n*******')

    cv2.putText(frame,f'{round(fps,1)}',(30,30),cv2.FONT_HERSHEY_SIMPLEX,1, 255)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Image acquisition stopped.")
        break
cap.release()
cv2.destroyAllWindows()