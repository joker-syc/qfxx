#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
回调函数：就是将函数作为参数传递到另外一个函数中，这个被传递进去后来又
被调用的函数我们称之为回调函数。
'''

'''
回调函数的使用：
典型：装饰器

偏函数
'''
import time
import functools

def outer(func):
    def inner():
        print("***************")
        func()
    return inner


@outer
def now():
    print(time.ctime())

# now()

# max2 = functools.partial(max,10)


def wake_up1(t):
    print("在%s点，使用掐大腿的方式叫醒"%t)


def wake_up2(t):
    print("在%s点，使用揪头发的方式叫醒"%t)


def call_wake(func,t):
    return func(t)

call_wake(wake_up1,"2")
