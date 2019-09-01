#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 14:32
# @Author  : joker-syc
# @Site    : 
# @File    : 6.数组的高级索引----布尔索引.py
# @Software: PyCharm

import numpy as np

#数组的高级索引----布尔索引
# # x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11],['1']])
# # x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11,[1,3]]])
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) #看来必须是纯数字才能索引
# print ('我们的数组是：')
# print (x)
# print ('\n')
#
# # print (x[x !=  5 and x <10])
# # print (x[x !=  5 , x <3])
# print (x[x ==  100])
# print (x[x ==  1])             #只要是合理的单个布尔运算符都可以   (就算索引不到也不会报错)