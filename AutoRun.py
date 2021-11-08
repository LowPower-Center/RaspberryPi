import numpy as np

import communication

import cv2.cv2 as cv

import picture_transform
import recognize

#init
cap = cv.VideoCapture(0)  # 开启摄像头
port=communication.port_communicate()
classifier=recognize.classfier()
mission=False
index=0
cross=0
cap.set(3, 640)  # 设置分辨率
cap.set(4, 480)


def get_input():
    global mission_number
    ok, img = cap.read()  # 读取摄像头图像
    if port.response() == "t":
        mission = True

        while mission:
            number=np.zeros(8)
            for i in range(5):
                ok, img = cap.read()  # 读取摄像头图像
                # 展示图像
                img = cv.flip(img, 1)
                transformer = picture_transform.Transformer(img)
                #        f,img=transformer.calculate_line()
                #        cv.imshow("img",img)
                try:
                    num = classifier.recognize(transformer.img_binary)
                    number[num-1] += 1
                except:
                    pass
            try:
                mission_number=np.argmax(number)+1
                port.publish_mission(mission_number)
                break
            except:
                pass
            k = cv.waitKey(1)  # 键盘值
            if k == 27:  # 通过esc键退出摄像
                break
            elif k == ord("p"):
                cv.imwrite('samples/{}.png'.format(index), img)
                print("save")
            elif k == ord("w"):
                port.forward(0.1)
            elif k == ord("s"):
                port.backward(0.1)
            elif k == ord("a"):
                port.left(0.1)
            elif k == ord("d"):
                port.right(0.1)
    else:
        k = cv.waitKey(1)  # 键盘值
        if k == 27:  # 通过esc键退出摄像
            mission_number=99
        elif k == ord("p"):
            cv.imwrite('samples/{}.png'.format(index), img)
            print("save")
        elif k == ord("w"):
            port.forward(0.1)
        elif k == ord("s"):
            port.backward(0.1)
        elif k == ord("a"):
            port.left(0.1)
        elif k == ord("d"):
            port.right(0.1)
def cross_recognize():
    if port.response() == "e":
        global cross
        global mission_number
        cross += 1
        while (2 - cross):
            ok, img = cap.read()  # 读取摄像头图像
            img = cv.flip(img, 1)
            img_left = img[:, :320]
            img_right = img[:, 320:]
            transformer_left = picture_transform.Transformer(img_left)
            transformer_right = picture_transform.Transformer(img_right)
            try:
                ground_number_left = classifier.recognize(transformer_left.img_binary)
                ground_number_right = classifier.recognize(transformer_right.img_binary)
                if ground_number_left == mission_number:
                    port.publish_mission("l")
                    break
                elif ground_number_right == mission_number:
                    port.publish_mission("r")
                    break
                else:
                    port.publish_mission("g")
                    break
            except:
                pass

    else:
        pass

while True:  #总任务
    while True:    #识别拍照图像任务
        get_input()
        if mission_number:break
    while True:
        cross_recognize()
        if cross>2:break
# 关闭摄像头
cap.release()
cv.destroyAllWindows()


