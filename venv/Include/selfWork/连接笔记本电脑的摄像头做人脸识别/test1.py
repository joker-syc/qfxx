#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 0031 11:00
# @Author  : joker-syc
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
import cv2

def test():
    '''
   调用摄像头，捕捉图像
   '''
    import time
    # 读取摄像头，0表示系统默认摄像头
    cap = cv2.VideoCapture(0)
    while True:
        # 读取图像
        ret, photo = cap.read()
        # 将图像传送至窗口
        cv2.imshow('Please Take Your Photo!!', photo)

        # 设置等待时间，若数字为0则图像定格
        key = cv2.waitKey(2)
        # 按空格获取图像
        if key == ord(" "):
            # 以当前时间存储
            filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"
            # 保存位置
            cv2.imwrite(filename, photo)
        # 按“q”退出程序
        if key == ord("q"):
            cap.release()
            break
            pass

if __name__ == '__main__':
    test()