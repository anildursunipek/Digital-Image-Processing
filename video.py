import cv2
import numpy as np


# KAMERADAN GÖRÜNTÜ ÇEKME **************************
"""
Resimler pixellerden videolar karelerden oluşur
Kareler arka arkaya gelerek videoyu oluşturur
Frame = kare
"""

"""
cam = cv2.VideoCapture(0)
#Video yakalamak için kamerayı tanımladık. Parametre olarak kamerayı seçiyoruz.0=Default
# 1 , 2 değerleri 1. ve 2. kameraları açmamızı sağlar
0,1,2 Değişkenleri yerine eğer bir video konumu girilirse o videoyu okur

if not cam.isOpened():
    print('Kamera tanınmadı')
    exit()
#İsOpened mödülü ile kameranın tanınıp tanınmadığını anlayabiliriz
"""

"""
while cam.isOpened():
    ret, frame = cam.read()#2 adet değeri geri döndürür. Eğer frame'ler okunduysa ret true olur okunmadıysa false
    #ret true yada false olarak değer döndürür. Kameranın okunup okunmadığını belirtir
    #frame ise okunan değerlerin aktarıldığı değişkendir
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
    if not ret:
        print("Kameradan görüntü alınamadı")
        break
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        #Her bir frame 1 ms duracak şekilde ayarlanıyor
        print("Görüntü sonlandırıldı.")
        break
#cv2.waitKey() içine yazılan paramtere her bir frame'in ne kadar ekranda kalacağını belirler
cam.release()
#Kameranın çalışmasını durdurur.
cv2.destroyAllWindows()
"""

#VİDEODAN GÖRÜNTÜ OKUMA **************************
"""
vid = cv2.VideoCapture("e.mp4")

while vid.isOpened():
    ret,frame= vid.read()
    
    if not ret:
        print("Video okunamadı")
        break
    cv2.imshow("video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Görüntü sonlandırıldı.")
        break
vid.release()
cv2.destroyAllWindows()
"""


#VİDEOYU KAYIT ETME

cam = cv2.VideoCapture(0)

fourrc = cv2.VideoWriter_fourcc(*'MJPG')
# Videonun hangi formatta kayıt edileceğini belirliyoruz
#FourCC, video codec bileşenini belirtmek için kullanılan 4 baytlık bir koddur.

out = cv2.VideoWriter("deneme.mp4",fourrc,30.0,(640,480))
#Çıktı olarak videonun ismini,türünü,fpsini,ölçülerini belirliyoruz
while cam.isOpened():
    ret,frame = cam.read()
    
    if not ret:
        print("Kayıt alınamadı")
        break
    
    out.write(frame)
 #Videoyu çıktı olarak yazdırıyoruz   
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Görüntü sonlandırıldı.")
        break
cam.release()
out.release()
cv2.destroyAllWindows()