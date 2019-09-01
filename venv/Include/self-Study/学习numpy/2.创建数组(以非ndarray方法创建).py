#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 14:27
# @Author  : joker-syc
# @Site    : 
# @File    : 2.创建数组(以非ndarray方法创建).py
# @Software: PyCharm

import numpy as np
#创建数组(不是用底层的ndarray方法来创建)
# import time
# # while 1:
# time.sleep(1)
# # a=np.empty([3,3])     #此方法创建的是一个未初始化数组    里面的数据在未初始化之前是随机的
# # a=np.zeros([4,4])     #此方法创建的是一个数组元素全是0 的数组
# a=np.ones([5,5])       #此方法创建的是一个数组元素全是1 的数组
#
# print(a)
# # print(id(a))          #每次调用np.empty()都会开辟新的内存空间
#
# z=1
# for x in range(0,3):
#     for y in range(0,3):
#         a[x][y]=z
#         z+=1
# print(a)               #可以通过下标给数组内存储的值进行初始化