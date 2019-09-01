#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 15:51
# @Author  : joker-syc
# @Site    : 
# @File    : 9.数组迭代.py
# @Software: PyCharm

'''
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。

迭代器最基本的任务的可以完成对数组元素的访问。

接下来我们使用 arange() 函数创建一个 2X3 数组，并使用 nditer 对它进行迭代。
'''

import numpy as np

# a = np.arange(6).reshape(2, 3)
# print('原始数组是：')
# print(a)
# # print('\n')
# print('迭代输出元素：')
# for x in np.nditer(a):
#     print(x, end=", ")
# print('\n')
# print(a.T)          #输出转置矩阵

a = np.arange(6).reshape(2, 3)
print(a)
for x in np.nditer(a.T):
    print(x, end=", ")
    print(id(x))
print('\n')

print(a.T)
for x in np.nditer(a.T.copy(order='C')):

    print(x, end=", ")
    print(id(x))
print('\n')

'''
迭代的时候修改数组中元素的值

nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），
为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。

'''
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# print ('原始数组是：')
# print (a)
# print ('\n')
# # for x in np.nditer(a):
# #     x[...]=2*x
# # print ('修改后的数组是：')
# # print (a)                            #嗯,只读的确不能修改里面的值,会报ValueError: assignment destination is read-only
#
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...]=2*x
# print ('修改后的数组是：')
# print (a)
#
# for x in np.nditer(a, op_flags=['writeonly']):
#     x[...]=2*x
#     # print(x)
#     # if x <3:
#     #     print(a[x])            #不是只写吗....怎么可读呢????
# print ('修改后的数组是：')
# print (a)

'''
使用外部循环 

nditer类的构造器拥有flags参数，它可以接受下列值：
c_index       可以跟踪 C 顺序的索引 
f_index       可以跟踪 Fortran 顺序的索引 
multi-index   每次迭代可以跟踪一种索引类型 
external_loop 给出的值是具有多个值的一维数组，而不是零维数组 

在下面的实例中，迭代器遍历对应于每列，并组合为一维数组。
'''

a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('修改后的数组是：')
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
    print(x, end=", " )
    print(id(x))
# a = np.arange(0,60,5)
# a = a.reshape(3,4).T                   #为什么
# print ('原始数组是：')
# print (a)
# print ('\n')
# print ('修改后的数组是：')
# for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):      #
#     print (x, end=", " )