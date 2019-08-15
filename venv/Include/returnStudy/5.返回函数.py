#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
将函数作为返回值，我们称这个函数为返回函数。
'''

'''
最典型的使用：装饰器

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



max2 = functools.partial(max,10)


def mysum(*args):
    res = 0
    for x in args:
        res += x
    return res

def lazy_sum(*args):
    def inner():
        res = 0
        for x in args:
            res += x
        return res
    return inner

print(mysum(1,2,3,4,5))

print(lazy_sum(1,2,3,4,5)())