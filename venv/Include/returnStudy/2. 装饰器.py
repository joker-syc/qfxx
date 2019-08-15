#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-

# def A(func):
#     print("-->1")
#     def wrapper(*args,**kwargs):
#         func()
#         print("-->hello")
#     return wrapper
#
# @A
# def show():
#     print("-->python")
#
#
# show()

# def A(func):
#     print('-->1')
#     dd=lambda x:x*x
#     return dd
# @A
# def B():
#     print('dd')
#
# B(1)          #这里只会执行print('-->1')  因为加装装饰器后,首先运行的是装饰器的函数8
# print(B(1))
# print(B(3))


#一定要注意lambda函数形成的闭包
# def testFun():
#     temp = [lambda x: i*x for i in range(4)]
#     return temp
#
# for everyLambda in testFun():
#     print(everyLambda(2))

# temp = [lambda x: i*x for i in range(4)]
# print(temp[0](2))

