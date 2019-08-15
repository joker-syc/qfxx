#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 0001 9:27
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm

#用yield关键字生成斐波那契数列
# def feibo(n):
#     b=1
#     c=1
#     for a in range(1,n+1):
#         if a == 1:
#             yield 1
#         elif a==2:
#             yield 1
#         else:
#             b,c=b+c,b
#             yield b
#
#
#
# if __name__ == '__main__':
#     a=feibo(5)
#     print(next(a))
#     print(next(a))
#     print(next(a))
#     print(next(a))
#     print(next(a))

# from greenlet import greenlet
# import time
#
# def  fun1():
#     print("协程1...")
#     time.sleep(3)
#     g2.switch() #切换到协程g2
#     print("节日快乐。。。")
#
#
# def fun2():
#     print("协程2...")
#     time.sleep(3)
#     g1.switch() #切换到协程g1
#
#
# if __name__ == '__main__':
#     g1 = greenlet(fun1)
#     g2 = greenlet(fun2)
#     g1.switch() #切换到协程1

from gevent import monkey;monkey.patch_all()#导入猴子补丁#可以实现协程的自动切换
import requests
import gevent
import threading
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

def get_data(url):
    print("协程",url)
    response = requests.get(url,headers=headers)
    print(url,"response",response.text)
    time.sleep(3)


if __name__ == '__main__':
    #协程爬取数据
    t1 = time.time()
    url_list = [
        'http://www.baidu.com',
        'http://www.qq.com',
        'http://www.ifeng.com',
        'http://www.sina.com.cn',
        'http://www.taobao.com',
    ]
    g_list = []
    for url in url_list:
        g = gevent.spawn(get_data,url)
        g_list.append(g)

    gevent.joinall(g_list)
    #3.4110121726989746
    #多线程爬取数据
    # t_list = []
    # for url in url_list:
    #     t = threading.Thread(target=get_data,args=(url,))
    #     t.start()
    #     t_list.append(t)
    # for t in t_list:
    #     t.join()
    print(time.time()-t1)
    #4.9332239627838135