#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 0031 14:15
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm
'''
此种方式创建的进程是最常用的(创建的的线程默认是非守护线程)
不过创建进程之后,一定要开启进程,不然就没用
.join()函数是让主线程在子线程结束前主线程不能结束
'''



import threading
import time
from Include.day18.爬虫 import getData
# def func(dd,a):
#     print(dd)
#     print(getData(a))
#
# def cnthread(a):
#     t=threading.Thread(target=func,args=('线程'+str(a),a))
#     t.start()
#     t.join()

class Mythread(threading.Thread):

    def run(self):
        print(getData())

if __name__ == '__main__':
    # for a in range(10):
    #     cnthread(a)
    mythread=Mythread()
    mythread.start()