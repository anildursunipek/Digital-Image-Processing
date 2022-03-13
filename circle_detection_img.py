import cv2
import numpy as np

para = cv2.imread('img/bozukpara.jpg')
gray = cv2.cvtColor(para,cv2.COLOR_BGR2GRAY) #Görüntüyü griye çevirdik
gray = cv2.medianBlur(gray,5) #Blur yaparak görüntüdeki kirliliği azalttık

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,120, param1=100,param2=30,minRadius=1,maxRadius=80)
circles_round = np.uint16(np.around(circles))

for i in circles_round[0, : ]:
    cv2.circle(para, (i[0],i[1]),i[2],(50,200,200),5)
    cv2.circle(para,(i[0],i[1]),2,(255,0,0),3)

print(circles.shape)
print(circles_round)
print(str(circles_round.shape[1]) + ' adet para bulundu.')

cv2.imshow('Para',para)
#cv2.imshow('Gri',gray)
#cv2.imshow('Blur',img)

cv2.waitKey()
cv2.destroyAllWindows()