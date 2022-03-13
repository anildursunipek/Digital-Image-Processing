import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

def nothing(x):
    pass
cv.namedWindow("resim")
cv.createTrackbar("H-low", "resim", 0, 255, nothing)
cv.createTrackbar("S-low", "resim", 0, 255, nothing)    
cv.createTrackbar("V-low", "resim", 0, 255, nothing)
cv.createTrackbar("H-up", "resim", 0, 255, nothing)
cv.createTrackbar("S-up", "resim", 0, 255, nothing)    
cv.createTrackbar("V-up", "resim", 0, 255, nothing)       


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Görüntü Okunamadı")
        break
    frame = cv.flip(frame, 1)
    hsv_color = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
       
       
    h_low = cv.getTrackbarPos("H-low", "resim")
    s_low = cv.getTrackbarPos("S-low", "resim")
    v_low = cv.getTrackbarPos("V-low", "resim")
    h_up = cv.getTrackbarPos("H-up", "resim")
    s_up = cv.getTrackbarPos("S-up", "resim")
    v_up = cv.getTrackbarPos("V-up", "resim")
    
    lower_color = np.array([h_low,s_low,v_low],dtype="uint8")
    upper_color = np.array([h_up,s_up,v_up],dtype="uint8")
    hsv_mask = cv.inRange(hsv_color, lower_color, upper_color)
    color = cv.bitwise_and(frame,frame, mask=hsv_mask)

    cv.imshow("resim2", frame)
    cv.imshow("resim", color)
    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Görüntü alma durduruldu.")
        break
cap.release()
cv.destroyAllWindows()