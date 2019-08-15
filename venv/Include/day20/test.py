#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 0002 8:35
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm

# for a in range(5.5):
#     print(a)

# str1='2dadadad1\n'
# print(str1.startswith('1'))
# print(str1.endswith('\n'))

# dict1={1:2,3:[12,232,23,[232,3]],4:"12"}
# print(type(dict1.values()))
# print(list(dict1.values()))              #结论:<class 'dict_values'>的行为模式就是list
# dict2=set(dict1)
# print(dict2)
# print(dict1)
# dict3=set(dict1.values())
# print(dict3)                         #这个会报错 ,显示list为不可哈希类型

'''
对于 Python 的内建类型来说，只要是创建之后无法修改的(immutable)类型都是 hashable 如字符串，
可变动的都是 unhashable的比如：列表、字典、集合，他们在改变值的同时却没有改变id，
无法由地址定位值的唯一性，因而无法哈希。我们自定义的类的实例对象默认也是可哈希的（hashable），而hash值也就是它们的id()。
'''
# str1='wqweweq122'                 #因为str类型是不可变类型,因此其的库函数并不会改变其原有的值
# str1.replace('2','1')
# print(str1)
# str1.upper()
# print(str1)

# list1=[1,2,12,3,4,43,21,2,3,2,4]            #因为list类型是可变类型,因此其的库函数会改变其原有的值
# list1.sort()
# print(list1)

# import functools
#
# def a(c,b=0):
#     return c+b
#
# print(functools.partial(a,b=1)(1))

class A:
    __slots__=('name','age')
    pass

a=A()
a.dd='dd'
print(a.dd)