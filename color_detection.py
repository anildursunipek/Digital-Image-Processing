import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
#cv.CAP_DSHOW hataları düzeltti
kernel = np.ones((7,7),np.uint8)
y = 0
toplamFps = 0

while cap.isOpened():
    start = time.time()
    ret , frame = cap.read()
    frame = cv.flip(frame,1)
    #Görüntünün y eksenine göre yansımasını alır. Ayna görüntüsü elde ederiz
    # 0 x eksenine -1 orjine göre 1 yansımasını alır
    
    if not ret:
        print("Görüntü okunamadı")
        break
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #Burada renk uzayları arasında geçiş yapıyoruz. BGR uzayındaki renkleri hsv ye dönüştürüyoruz.
    #Amacımız daha kolay bir uzayda renk tespiti yapmak.Hsv de renkleri ayırmak daha kolay
    """
    Hue:Renk anlamına gelir
    Saturation:Bir rengin solukluğu yada yoğunluğu
    Value:Brigtness ile ilgilidir. Parlaklık degeri.
    """
    lower = np.array([24,40,100],dtype="uint8")#Hangi rengi tespit etmek istiyorsanız onun degerlerini girmelisiniz
    upper = np.array([54,255,255],dtype="uint8")
    red_mask = cv.inRange(hsv_frame,lower,upper)#Lower ve upper değerlerini inRange fonksiyonuna aktararak hsv uzayında aralık belirtiyoruz

    red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)#Siyah bölgeden gereksiz beyaz noktaları kaldırır
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_CLOSE, kernel)#Beyaz bölgeden gereksiz siyah noktaları kaldırır
    red = cv.bitwise_and(frame, frame, mask = red_mask)#Mantıksal and operatörü ile eşleşen matrislerin görüntüde çıkmasını sağlıyoruz
    contours, hierarchy = cv.findContours(red_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #findCountours metodu siyah arka plan üzerindeki beyaz nesneleri bulur
    #Nesneler üzerindeki renk ve yoğunluğu aynı olan noktaları sürekli bir çizgi halinde algılar
    #Nense ve kenar tespit etmede kullanılan bir yöntemdir
    #contours parametresi görüntüdeki her bir counter'ın (x,y) olarak listesidri
    #cv.CHAIN_APPROX_SIMPLE metodu tüm counter noktalarını saklamaz düz bir çizgi üzerindeki iki uç noktayı saklar
    #bu sayede daha az yer kaplar ve işlem hızı artar
    #Bir çizgiyi çizmek için iki uç noktasını bulmamız yeterlidir.

    output = cv.drawContours(red, contours,-1, (0, 0, 255), 3)

    """
    Burada and operatörü kullanılarak mantıksal bir işlem yapılıyor. Frame ile yellow_mask
    değişkenleri 2lik sistemde and mantıksal işlemine sokulup sonucunda 1 and 1 ise 1 ,
    1 and 0 ise 0 değerini döndürüyor. Bu da yeşillerle yeşiller karşılaştığında 1 olarak kalır
    ancak yeşil olmayan ile başka bir değer karşılaştığında ekrana aktarılmaz.
    """
    cv.imshow("Red", red)
    end = time.time()
    cv.imshow("Video", frame)
    cv.imshow("Red Mask", red_mask)
    fps = 1 / (end - start)
    y = y + 1
    toplamFps += fps
    ortalamaFps = toplamFps / y
    print('Ortalama Fps: ', round(ortalamaFps, 1))
    print('Anlık Fps: ', round(fps, 1))
    print('İşlem Sayısı: ',y,'\n*******')

    cv.putText(frame, f'{round(fps, 1)}', (30, 30), cv.FONT_HERSHEY_SIMPLEX, 1, 255)
    cv.imshow("Video", frame)
    cv.imshow("Red Mask", red_mask)
    if cv.waitKey(1) & 0xFF == 27:
        print("Görüntü kapatıldı.")
        break
cap.release()
cv.destroyAllWindows()