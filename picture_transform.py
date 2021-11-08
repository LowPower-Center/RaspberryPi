import cv2.cv2 as cv
import numpy as np

class Transformer():
    def __init__(self,img):
        self.img = img
        self.img_gray = cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        self.img_binary=cv.threshold(self.img_gray,127,255,cv.THRESH_BINARY)[1]
        self.img_binary_inv = cv.bitwise_not(self.img_binary)
        self.canvas=[[0,0],[224,0],[0,224],[224,224]]

    def get_wordpespective(self):
        M=cv.getPerspectiveTransform(self.corners,self.canvas)
        return cv.warpPerspective(self.img,M,(0,0))

    def calculate_line(self):
        self.k = []
        img2 = cv.Canny(self.img, 20, 250)  # 边缘检测
        line = 5
#        cv.imshow("img2", img2)
        self.minLineLength = 15
        self.maxLineGap = 150
        # HoughLinesP函数是概率直线检测，注意区分HoughLines函数
        lines = cv.HoughLinesP(img2, 1, np.pi / 180, 160, lines=line, minLineLength=self.minLineLength,
                               maxLineGap=self.maxLineGap)
        try:
            lines1 = lines[:, 0, :]  # 降维处理
            for x1, y1, x2, y2 in lines1:
                cv.line(self.img, (x1, y1), (x2, y2), (255, 255, 255), 5)
                self.k.append((y2-y1)/(x2-x1))
            return self.k, self.img
        except:
            return self.k, self.img
cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if ret==True:
        transformer=Transformer(frame)
        k,img=transformer.calculate_line()
        cv.imshow("img",img)

        if cv.waitKey(1)==ord('q'):
            break
    else:
        break







