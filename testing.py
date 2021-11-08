import cv2.cv2 as cv
import recognize

import communication
cap=cv.VideoCapture(0)
index=0
port=communication.port_communicate()
classfier=recognize.classfier()
while True:
    ret,frame=cap.read()
    frame=cv.resize(frame,(640,480))
    try:
        print()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)[1]
        contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for i in range(len(contours)):
            aera = cv.contourArea(contours[i])
            if 20000 > aera > 4000:
                x, y, w, h = cv.boundingRect(contours[i])
                img_cut = binary[y:y + h, x:x + w]
                img_cut = cv.resize(img_cut, (200, 300))
                a=classfier.recognize(img_cut)
                if a==1:
                    port.send_chracter('u')
                elif a==2:
                    port.send_chracter("i")
                elif a==3:
                    port.send_chracter("o")
                index+=1
                print("order:%d" % index)

    except:
        pass
    cv.imshow('frame',frame)
    k=cv.waitKey(1)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()

