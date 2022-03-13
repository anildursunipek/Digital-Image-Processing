import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass
cv2.namedWindow("resim")
cv2.createTrackbar("dist", "resim", 10, 255, nothing)
cv2.createTrackbar("Param1", "resim", 0, 255, nothing)
cv2.createTrackbar("Param2", "resim", 0, 255, nothing)
cv2.createTrackbar("MinRadius", "resim", 0, 255, nothing)
cv2.createTrackbar("MaxRadius", "resim", 0, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Görüntü Okunamadı")
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)


    dist = cv2.getTrackbarPos("dist", "resim")
    param1 = cv2.getTrackbarPos("Param1", "resim")
    param2 = cv2.getTrackbarPos("Param2", "resim")
    minRadius = cv2.getTrackbarPos("MinRadius", "resim")
    maxRadius = cv2.getTrackbarPos("MaxRadius", "resim")

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, dist , param1=100, param2=30, minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles_round = np.uint16(np.around(circles))
        for i in circles_round[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (50, 200, 200), 5)
            cv2.circle(frame, (i[0], i[1]), 2, (255, 0, 0), 3)

    cv2.imshow('resim',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Görüntü alma durduruldu.")
        break
cap.release()
cv2.destroyAllWindows()