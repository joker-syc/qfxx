#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
装饰器：在代码运行的期间动态增加功能的方式，我们称之为装饰器。
'''

'''
最简单的装饰器
def outer(func):
    def inner():
        #增加的功能
        func()
    return inner

外函数：
1.接收被装饰的函数，func ：被装饰的函数，
2.将装饰好的替代版的函数返回
内函数：
1.添加动态增加的功能
2.执行被装饰的函数

在内函数中，若被装饰的函数有返回值的时候，我们必须使用return，把被装饰函数的值返回
若被装饰的函数没有返回值，我们无需使用return。

'''
def outer(func):
    def inner():
        print("***********")
        res = func()
        print(res)
        print("***********")
        return res
    return inner



@outer
def now():
    return "2019-7-17"


# @outer
# def f():
#     print("hello world")

# def now2():
#     print("***********")
#     now()

print(now())
# f()


'''
****************
2019-7-17

'''

