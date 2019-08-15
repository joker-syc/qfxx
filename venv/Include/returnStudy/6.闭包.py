#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
若在一个函数内部定义另外一个函数，外部函数我们称之为外函数，
里面的函数我们称之为内函数。

闭包：在外函数中定义一个内函数，内函数使用了外函数的临时变量，
外函数的返回值是内函数的引用，此时就构成了一个闭包。

装饰器一定是闭包，闭包不一定是装饰器。

一般情况下，如果一个函数结束，那么这个函数所占用的空间都会被释放，
还给内存，局部变量也会随之消失，但是闭包是一个特殊的存在，当外函数
在结束自己的时候，发现自己还有临时变量在内函数中还需要使用，这时候，
他会将自己的临时变量绑定给内函数，然后自己再结束。
'''
# def func():
#     list1 = []
#     for i in range(10):
#         def inner(x):
#             return x*i
#         list1.append(inner)
#     return list1

# for x in range(10):
#     pass
# print(x)

# list1 = func()
# for f in list1:
#     print(f(2))

# def outer(func):
#     def inner():
#         print("***************")
#         func()
#     return inner


# def lazy_sum(*args):
#     def inner(a):
#         res = 0
#         for x in args:
#             res += x
#             res += a
#         return res
#     return inner
#
# print(lazy_sum(1,2,3,4)(1))

