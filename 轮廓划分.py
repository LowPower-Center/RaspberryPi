#查看单个图像的cut
import cv2.cv2 as cv
import numpy as np


frame=cv.imread('7-8/0.png')
frame=cv.resize(frame,(640,480))
frame_left=frame[:,:320]
frame_right=frame[:,320:]
gray=cv.cvtColor(frame_left,cv.COLOR_BGR2GRAY)
binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)[1]
contours,hierarchy=cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)



for i in range(len(contours)):
    aera=cv.contourArea(contours[i])
    print(aera)
    if 15000>aera>4000:
        print("a")
        x,y,w,h=cv.boundingRect(contours[i])
        img_cut=binary[y:y+h,x:x+w]
        img_cut=cv.resize(img_cut,(200,300))
        cv.imshow("img_cut%d" %i,img_cut)


gray=cv.cvtColor(frame_right,cv.COLOR_BGR2GRAY)
binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)[1]
contours,hierarchy=cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    aera=cv.contourArea(contours[i])
    print(aera)
    if 15000>aera>4000:
        print("b")
        x,y,w,h=cv.boundingRect(contours[i])
        img_cut=binary[y:y+h,x:x+w]
        img_cut=cv.resize(img_cut,(200,300))
        cv.imshow("img_cut%d" %i,img_cut)


cv.imshow('contours',frame)
cv.waitKey(0)
cv.destroyAllWindows()