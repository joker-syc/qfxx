#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import threading
import time
'''
# 创建线程
# target 要运行的目标函数
# 运行函数的时候需要传递的参数
# name 线程的名字
# deamo 为True的为守护线程，默认为False 
t1 = threading.Thread(target=func,args=("haha",),name="线程1")
# 开启线程
t1.start()
'''

'''
使用多线程爬取糗事百科，并且将爬取到的内容写到文件夹中。
https://www.qiushibaike.com/text/page/1/
'''


def func(str1):
    print(str1)
    time.sleep(1)
    print(threading.current_thread().name)

def func2(str1):
    print(str1)
    time.sleep(2)
    print(threading.current_thread().name)

def func3(str1):
    print(str1)
    time.sleep(3)
    print(threading.current_thread().name)



def creatThread():
    t1 = threading.Thread(target=func,args=("haha",),name="线程1")
    t1.start()

    t2 = threading.Thread(target=func2, args=("haha2",))
    t2.start()

    t3 = threading.Thread(target=func3, args=("haha3",))
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    t1 = time.time()
    creatThread()
    print(threading.current_thread().name)
    # time.sleep(2)
    print("over")
    t2 = time.time()
    print(t2-t1)