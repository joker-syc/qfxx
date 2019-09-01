#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 14:30
# @Author  : joker-syc
# @Site    : 
# @File    : 5.数组的高级索引---整数数组索引.py
# @Software: PyCharm

import numpy as np

#数组的高级索引---整数数组索引
# x = np.array([[1,  2],  [3,  4],  [5,  6]])
# y = x[[0,1,2],                   #这个是行索引
#       [0,1,0]]                  # 这个是列索引
# print (y)                       #取出(0,0)(1,1)(2,0)位置上的数

# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print ('我们的数组是：' )
# print (x)
# print ('\n')
# rows = np.array([[0,0],[3,3]])            #这个作为行索引
# cols = np.array([[0,2],[0,2]])            #这个作为列索引
# y = x[rows,cols]                          #在前的为行,在后的为列
# print  ('这个数组的四个角元素是：')
# print (y)                                 #取出(0,0)(0,2)(3,0)(3,2)

# a = np.array([[1,2,3], [4,5,6],[7,8,[1,2]]])
# b = a[1:3, 1:3]                            #取出行下标在1~2,列下标在1~3之间的元素
# c = a[1:3,[1,2]]                           #同上
# d = a[...,1:]                              #取出除第一列以外的元素
#
# print(b)
# print(c)
# print(d)
# print(a[...,1:])
