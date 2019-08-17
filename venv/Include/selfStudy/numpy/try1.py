#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 0027 17:07
# @Author  : joker-syc
# @Site    : 
# @File    : try1.py
# @Software: PyCharm

import numpy as np

# a=np.array(
#     (
#            (1,23,3,43,3,34,(1,2,33,3,23,2,32,3,232,32,32,3,2)),
#            (1,23,3,43,3,34,(1,2,33,3,23,2,32,3,232,32,32,3,2)),
#            (1,23,3,43,3,34,(1,2,33,3,23,2,32,3,232,32,32,3,2)),
#            (1,23,3,43,3,34,(1,2,33,3,23,2,32,3,232,32,32,3,2)),
#     )
#             )   #这样输入的数学意义是矢量,就是用元组输入(如果输入的元组的元素的数目不一致,就会报错)
# print(a)
# print(len(a))   #有7个元素
# print(a[0])
# print(a.shape[0])  #这个相当于len()函数,统计数组中的一维元素数目
# print(a.shape[1])  #统计数组中2维数组的元素数目
# # print(a.shape[2])  #这个会报错
#
# a=np.array([
#             [1,3,4,4,4,5,5,6,6],
#             [2,33,3,4,34,34,34,3433,4,34,3,4],
#             [2,2,32,32,32,32,32,23,23,2],
#             [2,3,2,32,3,23,3,3,[1,12,2,23,3,3,]]
#             ])
# #错误记录:多维数组千万不要少了外维的中括号
# print(a)
# print(len(a))
# print(a.shape)            #这个返回的是一个元组(好像与输入是元组的不太一样)
# print(a[0][0])
# print(a.size)             #相当于
# # print(a.shape[0])       #作用是与len()相同
# # print(a.shape[1])       #这个会报错,不知道啥原因

# a=np.array([
#             [1,3,4,4,4,5,5,6,6],
#             [1,3,4,4,4,5,5,6,6],
#             [1,3,4,4,4,5,5,6,6],
#             [1,3,4,4,4,5,5,6,'4']
#            ],int)
# #如果已经预先设置限定存储的类型,一级数组中出现了类型不一致的情况时,会在创建ndarray对象时报错
# # (实际上,只有当数组内的元素是无法通过相应得转化得到限定的存储类型时才会报错,其他时候会自动转换)
# print(a)
# print(len(a))
# print(a.shape)          #看来必须是非等长数组才能
# print(a[0][0])
# print(a.size)
# print(a.itemsize)     #数组中每个元素的大小 以字节为单位
# print(a.ndim)         #数组的维度
# print(a.flags)

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


# a=[[1,2,3,4],
#    [1,2,3,4],
#    [1,2,3,'4']]
# b=np.asarray(a,int)
# print(a)
# print(b)

# a=b'jsudjhiljieji'
# # b=np.frombuffer(a,dtype='S1')
# # b=np.frombuffer('skdjj2jkj23j',dtype='S1')          #看来只能处理同一类型的数据
# b=np.frombuffer(b'\1\2\3\4\5\6\7',dtype=np.uint8)    #搞不懂
#
# '''
# >> > s = 'hello world'
# >> > np.frombuffer(s, dtype='S1', count=5, offset=6)
# array(['w', 'o', 'r', 'l', 'd'],
#       dtype='|S1')                                      #可以看出来'S1'是用来处理字符型
#
# >> > np.frombuffer(b'\x01\x02', dtype=np.uint8)
# array([1, 2], dtype=uint8)
# >> > np.frombuffer(b'\x01\x02\x03\x04\x05', dtype=np.uint8, count=3)
# array([1, 2, 3], dtype=uint8)
# '''
# print(b)

# a=np.arange(5)
# a=np.arange(1,10,2,dtype=float)      #(start,stop,step)
# print(a)

a=np.linspace()
print(a)
