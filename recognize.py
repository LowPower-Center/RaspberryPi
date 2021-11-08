import cv2.cv2 as cv
import numpy as np

class classfier():
    def __init__(self):
        self.root = 'samples/'
        self.num = 80
        self.row = 300
        self.col = 200
        a = np.zeros((self.num, self.row, self.col))
        n = 0
        for i in range(1, 9):
            for j in range(1, 11):
                a[n, :, :] = cv.imread(self.root + str(i) + '/' + str(j) + '.png', 0)
                n += 1
        feature = np.zeros((self.num, round(self.row / 5), round(self.col / 5)))

        for ni in range(0, self.num):
            for nr in range(0, self.row):
                for nc in range(0, self.col):
                    if a[ni, nr, nc] == 255:
                        feature[ni, nr // 5, nc // 5] += 1
        self.f = feature


    def recognize(self,img):
        self.o=img
        self.of = np.zeros((round(self.row / 5), round(self.col / 5)))
        for nr in range(0,self.row):
            for nc in range(0,self.col):
                if self.o[nr,nc]==255:
                    self.of[nr//5,nc//5]+=1

        d=np.zeros(80)
        for i in range(0,80):
            d[i]=np.sum((self.of-self.f[i,:,:])*(self.of-self.f[i,:,:]))

        d=d.tolist()
        temp=[]
        Inf=max(d)
        k=7
        for i in range(k):
            temp.append(d.index(min(d)))
            d[d.index(min(d))]=Inf

        temp=[i/10 for i in temp]
        r=np.zeros(8)
        for i in temp:
            r[int(i)]+=1
        print("当前数字可能为:"+str(np.argmax(r)+1))
        self.result=np.argmax(r)+1

        return self.result