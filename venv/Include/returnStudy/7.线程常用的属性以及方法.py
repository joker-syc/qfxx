#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import threading
import time
'''
join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或
到达指定的timeout（可选参数）。

'''



def func():
    time.sleep(1)
    print(threading.current_thread().name)
    print(threading.current_thread())


if __name__ == '__main__':
    t = threading.Thread(target=func,name="hahaha")
    t.start()
    # 判断线程是否正在运行
    print(t.isAlive())
    # 获取线程的名字
    print(t.getName())
    # 设置线程名
    t.setName("good")
    # 判断此线程是否为守护线程／后台线程
    print(t.isDaemon())
    # 获取线程id
    print(t.ident)
    # 获取当前环境下正在运行的线程
    print(threading.active_count())
    # 枚举当前所有线程
    print(threading.enumerate())
    # 获取当前所在的线程对象
    print(threading.current_thread())