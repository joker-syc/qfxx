#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
偏函数：就是将函数中的某些参数给固定住，然后返回一个新的函数，
调用新的函数会更加的方便。
作用：方便函数的调用。
偏函数是functools模块中提供的一个功能。

functools.partial(func,要固定参数)
参数一：被固定的函数的函数名
参数二：要固定的参数，可以以键值对的方式传参也可以以位置参数传参

功能：相等于给某个函数设置默认值，调用函数的时候会更加的方便。
'''
import functools
import operator

#
def ins(name,age,address):
    '''
    :param name:
    :param age:
    :param address:
    :return:
    '''
    print("我叫%s,我今年%d岁，我家在%s"%(name,age,address))


ins("李磊",20,"江西")
# ins("韩梅梅",21,"江西")
# ins("麻子",20)



ins2 = functools.partial(ins,address="江西",age=20)
ins2("马冬梅")

'''
求任意数与100相加之和。
'''
print(operator.add(100,20))

add2 = functools.partial(operator.add,100)
print(add2(20))

floordiv2 = functools.partial(operator.floordiv,20)
print(floordiv2(10))

int2 = functools.partial(int,base=2)
print(int2("10110"))







