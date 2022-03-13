import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),dtype=np.uint8)
#Burada 512x512 boyutunda 3 kanallı bir görsel oluşturuyoruz ve dtype olarak uint8 ayarlıyoruz

def nothing(x):
    pass

cv.namedWindow("title_window")

cv.createTrackbar("R", "title_window", 0,255, nothing)
cv.createTrackbar("G", "title_window", 0,255, nothing)
cv.createTrackbar("B", "title_window", 0,255, nothing)
"""
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
Trackbar oluştururken sırasıyla 5 parametre girilir. Barın ismi, pencere ismi, min değer,
max değer, fonksiyon olmak üzeri 5 farklı parametre tanımlanırsa çalışır.
"""

while True:
    cv.imshow("title_window", img)
    
    if cv.waitKey(1) & 0xFF == 27:
        break
    r = cv.getTrackbarPos("R", "title_window")
    g = cv.getTrackbarPos("G", "title_window")
    b = cv.getTrackbarPos("B", "title_window")
    #Burada getTrackbarPos modülü ile title_window penceresindeki r,g,b değerlerini
    #belirlenen r,g,b değişkenlerine aktardır
    #cv.getTrackbarPos("Aktarılacak bar ismi","bulunduğu pencere")
    
    img[:] =[b,g,r]


cv.destroyAllWindows()