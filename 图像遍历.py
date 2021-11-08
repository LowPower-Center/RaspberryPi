
#快速提取样本
#根据拍摄图片直接划分样本
import os
import cv2.cv2 as cv
import numpy as np

index=0

for i in range(31):
    frame=cv.imread("2/{}.png".format(i))

#       print(os.path.join(root, file))
#此处直接均分图片，划分到两个文件夹下
    frame=frame[:,:]
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)[1]



    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        aera=cv.contourArea(contours[i])
        print(aera)
        if  20000>aera>4000:
            x,y,w,h=cv.boundingRect(contours[i])
            img_cut=binary[y:y+h,x:x+w]
            img_cut=cv.resize(img_cut,(200,300))
            cv.imwrite('samples/1/{}.png'.format(index),img_cut)

            index+=1
