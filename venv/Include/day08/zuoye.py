#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc

#1.设计一个函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5,
# 若是则返回True，否则返回False

def lenc(*args):
    if len(args)==1:
        if type(args[0])==str:
            return False
        else:
            if len(args[0])<=5:
                return False
    else:
        if len(args)<= 5:
            return False
    return True

print(lenc([1,23,4,55,5,3]))

# 2.设计一个函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
# 【字符串中含有空格，列表与元组中函数有空串】。若含有则返回True，否则返回False
# "hello world" [12,34,"",23]

def judge(*args):
    if len(args)==1:
        if type(args[0])==str:
            if args[0]=="" or " ":
                return False
        else:
            for a in args[0]:
                if a=="":
                    return False
        return True

print(judge("sdsd"))

# max()函数的功能补全
# 传递1个，必须可迭代对象，返回可迭代对象中的最大值
# 若传递多个，必须number或str ，返回最大值

from collections.abc import Iterable     #判断对象是否为可迭代对象的库函数
def sun(*args):
    if len(args)==1:
        if isinstance(args,Iterable):
            maxnum=args[0][0]
            for a in args[0]:
                if a>maxnum:
                    maxnum=a
            return maxnum
        else:
            print("请输入一个可迭代对象")
    else:
        maxnum=args[0]
        for a in args:
            if a > maxnum:
                maxnum = a
        return maxnum
    # print(args)

print(sun([1,23,4,5,4,5,6,6,7]))

