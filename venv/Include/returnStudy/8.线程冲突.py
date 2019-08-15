#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import threading
'''
lock = threading.Lock() #创建锁
lock.acquire() #加锁
lock.release() #释放锁
with lock:
    pass
此语句可以自动的加锁，运行完毕之后，自动释放锁。
内部实现__enter__()与__exit__()函数，在enter的时候自动加锁，
在exit自动的释放锁
'''


lock = threading.Lock()


def func():
    # 加锁
    # lock.acquire()
    with lock:
        global num
        # cpu分配的时间片不足以完成一百万次加法运算
        # num还没来得及存储，就被其他线程抢占了
        for x in range(1000000):
            num += 1
    # print(num)
    # lock.release()
    #释放锁


if __name__ == '__main__':
    num = 0
    tList = []
    for x in range(5):
        t = threading.Thread(target=func)
        t.start()
        tList.append(t)

    for t in tList:
        t.join()
    print(num)