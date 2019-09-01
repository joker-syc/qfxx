#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 14:29
# @Author  : joker-syc
# @Site    : 
# @File    : 4.数组的切片及索引.py
# @Software: PyCharm

import numpy as np

#数组的切片和索引
# #切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。
# b=slice(1,5,2)
# print(a[b])

# print(a[::-1])

# a = np.array([[1,2,3],[3,4,5],[4,5,6],[1,2,3]])
# print(a)
# print (a[...,1])   # 第2列元素
# print (a[1,...])   # 第2行元素
# print (a[...,1:])  # 第2列及剩下的所有元素

# a = np.array([[1,2],[3,4,5],[4],[1,2]])      #当数组中的元素是不等长的时候,就没有列和行之分
# print(a)
# print (a[...,1])   # 第2列元素
# print (a[1,...])   # 第2行元素
# print (a[...,1:])  # 第2列及剩下的所有元素
