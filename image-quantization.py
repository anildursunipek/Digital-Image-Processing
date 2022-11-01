import cv2
import matplotlib.pyplot as plt
import numpy as np

img_8bit = cv2.imread("img/bozukpara.jpg")
img_8bit = cv2.cvtColor(img_8bit, cv2.COLOR_BGR2RGB)
img_8bit = cv2.cvtColor(img_8bit, cv2.COLOR_RGB2GRAY)
# print(img_8bit.shape)
# print(img_8bit[0][0])

img_4bit = cv2.imread("img/bozukpara.jpg")
img_4bit = cv2.cvtColor(img_4bit, cv2.COLOR_BGR2RGB)
img_4bit = cv2.cvtColor(img_4bit, cv2.COLOR_RGB2GRAY)

img_2bit = cv2.imread("img/bozukpara.jpg")
img_2bit = cv2.cvtColor(img_2bit, cv2.COLOR_BGR2RGB)
img_2bit = cv2.cvtColor(img_2bit, cv2.COLOR_RGB2GRAY)

img_1bit = cv2.imread("img/bozukpara.jpg")
img_1bit = cv2.cvtColor(img_1bit, cv2.COLOR_BGR2RGB)
img_1bit = cv2.cvtColor(img_1bit, cv2.COLOR_RGB2GRAY)


def changeTo1Bit(img):
    img_width = img.shape[1]
    img_height = img.shape[0]
    print("img_width: ", img_width, "img_height: ", img_height)
    for i in range(img_height):
        for j in range(img_width):
            if(img[i][j] <= 127):
                img[i][j] = 64
            if(img[i][j] > 127 and img[i][j] <= 255):
                img[i][j] = 192
    print(np.unique(img))
    return img

def changeTo2Bit(img):
    img_width = img.shape[1]
    img_height = img.shape[0]
    print("img_width: ", img_width, "img_height: ", img_height)
    for i in range(img_height):
        for j in range(img_width):
            if(img[i][j] <= 63):
                img[i][j] = 31
            if(img[i][j] > 63 and img[i][j] <= 127):
                img[i][j] = 95
            if(img[i][j] > 127 and img[i][j] <= 191):
                img[i][j] = 159
            if(img[i][j] > 191 and img[i][j] <= 255):
                img[i][j] = 223
    print(np.unique(img))
    return img


def changeTo4Bit(img):
    img_width = img.shape[1]
    img_height = img.shape[0]
    print("img_width: ", img_width, "img_height: ", img_height)
    for i in range(img_height):
        for j in range(img_width):
            if(img[i][j] <= 15):
                img[i][j] = 7
            if(img[i][j] > 15 and img[i][j] <= 31):
                img[i][j] = 23
            if(img[i][j] > 31 and img[i][j] <= 47):
                img[i][j] = 39
            if(img[i][j] > 47 and img[i][j] <= 63):
                img[i][j] = 55
            if(img[i][j] > 63 and img[i][j] <= 79):
                img[i][j] = 71
            if(img[i][j] > 79 and img[i][j] <= 95):
                img[i][j] = 87
            if(img[i][j] > 95 and img[i][j] <= 111):
                img[i][j] = 103
            if(img[i][j] > 111 and img[i][j] <= 127):
                img[i][j] = 119
            if(img[i][j] > 127 and img[i][j] <= 143):
                img[i][j] = 135
            if(img[i][j] > 143 and img[i][j] <= 159):
                img[i][j] = 151
            if(img[i][j] > 159 and img[i][j] <= 175):
                img[i][j] = 167
            if(img[i][j] > 175 and img[i][j] <= 191):
                img[i][j] = 183
            if(img[i][j] > 191 and img[i][j] <= 207):
                img[i][j] = 199
            if(img[i][j] > 207 and img[i][j] <= 223):
                img[i][j] = 215
            if(img[i][j] > 223 and img[i][j] <= 239):
                img[i][j] = 231
            if(img[i][j] > 239 and img[i][j] <= 255):
                img[i][j] = 247
    print(np.unique(img))
    return img

img_1bit = changeTo1Bit(img_1bit)
img_2bit = changeTo2Bit(img_2bit)
img_4bit = changeTo4Bit(img_4bit)

cv2.imshow("window-1bit",img_1bit)
cv2.imshow("window-2bit",img_2bit)
cv2.imshow("window-4bit",img_4bit)
cv2.imshow("window-8bit",img_8bit)

cv2.waitKey()
cv2.destroyAllWindows()


# plt.subplot(2,2,1)
# plt.imshow(img_1bit)
# plt.title("1 Bit")
# plt.xticks([])
# plt.yticks([])
#
# plt.subplot(2,2,2)
# plt.imshow(img_2bit)
# plt.title("2 Bit")
# plt.xticks([])
# plt.yticks([])
#
# plt.subplot(2,2,3)
# plt.imshow(img_4bit)
# plt.title("4 Bit")
# plt.xticks([])
# plt.yticks([])
#
# plt.subplot(2,2,4)
# plt.imshow(img_8bit)
# plt.title("8 Bit")
# plt.xticks([])
# plt.yticks([])
#
# plt.show()