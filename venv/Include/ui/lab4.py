import cv2
import numpy as np
import time

# 截取视频帧的函数
# cap = cv2.VideoCapture("./Input.mp4")
cap = cv2.VideoCapture(0)
# time.sleep(4)
background = 0

# 第一个参数ret 为True 或者False,代表有没有读取到图片第二个参数background表示截取到一帧的图片。
ret, background = cap.read()

# print(ret)
#
# cv2.imshow('???',background)
# # 让程序停下来,不要执行完就退出
# cv2.waitKey(0)

while (True):
    ret, img = cap.read()
    if ret == True and cv2.waitKey(1) != ord("q"):
        # 进行颜色空间的转换,从BGR转换到HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # light1 = (0, 120, 70)
        light1 = (0, 0, 0)
        dark1 = (0, 255, 255)
        '''第一个参数：hsv指的是原图
           第二个参数：light1指的是图像中低于这个light1的值，图像值变为0
           第三个参数：dark1指的是图像中高于这个dark1的值，图像值变为0
        '''
        mask1 = cv2.inRange(img_hsv, light1, dark1)

        light2 = (170, 120, 70)
        dark2 = (180, 255, 255)
        mask2 = cv2.inRange(img_hsv, light2, dark2)

        mask1 = mask1 + mask2

        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
        mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
        mask2 = cv2.bitwise_not(mask1)

        result1 = cv2.bitwise_and(background, background, mask=mask1)
        result2 = cv2.bitwise_and(img, img, mask=mask2)
        final_result = cv2.addWeighted(result1, 1, result2, 1, 0)

        cv2.imshow("final_result", final_result)

    else:
        break

cap.release()
cv2.destroyAllWindows()
