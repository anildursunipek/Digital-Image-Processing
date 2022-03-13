import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255
print(canvas)

"""Line Drawing"""
cv2.line(canvas,(0,0),(512,512),(255,0,0),5)#def line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None):
#cv2.line(tual,başlangıç,bitiş,renk,kalınlık)
"""Rectangle Drawing"""

cv2.rectangle(canvas,(50,50),(100,100),(0,255,0),thickness=-1)#İçi dolu thickness= -1
cv2.rectangle(canvas,(150,150),(500,500),(0,255,0),thickness=3)#İçi boş
#cv2.rectangle(tual,başlangıç,bitiş,renk,kalınlık)
"""Circle Drawing"""
cv2.circle(canvas,(200,200),100,(0,0,255),thickness=-1)
#cv2.circle(tual,start,end,color,thickness)

"""Polyline Drawing"""
points = np.array([[75,50],[50,255],[100,100],[255,50]],dtype=np.int32)

cv2.polylines(canvas,[points],True,(100,100,100),2)

"""Elipse Drawing"""

cv2.ellipse(canvas,(200,200),(150,40),10,0,360,(150,150,150),thickness=-1)
#cv.ellipse(tual,(center),(axis0,axis1),angle,start,end,(color),thickness)



cv2.imshow('Test',canvas)
cv2.waitKey()
cv2.destroyAllWindows()