#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 14:34
# @Author  : joker-syc
# @Site    : 
# @File    : 7.数组的高级索引----花式索引.py
# @Software: PyCharm

import numpy as np

#数组的高级索引----花式索引
# 传入顺序索引数组
x = np.arange(32).reshape((8, 4))
print(x)
print(x[[4, 2, 1, 7]])            #此时是以列轴为索引     取出的是对应的行的数组

# 传入倒序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[-4, -2, 1, -7]])       #可以倒序索引

# 传入多个索引数组（要使用np.ix_）
# x = np.arange(32).reshape((8, 4))
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11],[1]])
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2],[1])])
print(x)
print(x[np.ix_([1, 2, 1], [0, 2, 1])])
#以上的所有花式索引只对等长数组生效