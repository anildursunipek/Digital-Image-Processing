import cv2
import matplotlib.pyplot as plt
import numpy as np

img_old = cv2.imread("img/test.jpg")
img_old = cv2.cvtColor(img_old,cv2.COLOR_BGR2GRAY)
print(img_old.shape)
cv2.imshow("OLD",img_old)


def gama(img,a,b,a1,b1):
    counter = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            counter += 1
            if(counter % 100 == 0):
                print("counter -> ", counter)
            x = img[i][j]
            if(x <= a):
                x = (x / a) * a1
                img[i][j] = x
            if(x < a and x > b):
                x = ((x - a) / (b - a)) * (b1 - a1) + a1
                img[i][j] = x
            if(x >= b):
                x = ((x - b ) / (255 - b )) * (255 - b1) + b1
    return img

img_new = cv2.imread("img/test.jpg")
img_new = cv2.cvtColor(img_new,cv2.COLOR_BGR2GRAY)
img_new = gama(img_new,52,92,22,162)
cv2.imshow("NEW",img_new)


plt.subplot(1,2,1)
plt.hist(img_old.ravel(),256,[0,256])
plt.ylim(ymax = 3500, ymin = 0)

plt.subplot(2,2,2)
plt.hist(img_new.ravel(),256,[0,256])
plt.ylim(ymax = 3500, ymin = 0)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()