#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 19:52
# @Author  : joker-syc
# @Site    : 
# @File    : 蓄水池抽样算法.py
# @Software: PyCharm

'''
问题：如何随机从n个对象中选择一个对象，这n个对象是按序排列的，但是在此之前你是不知道n的值的。
'''

'''
解法：我们总是选择第一个对象，以1/2的概率选择第二个，以1/3的概率选择第三个，
以此类推，以1/m的概率选择第m个对象。当该过程结束时，每一个对象具有相同的选中概率
'''
#按照题目要求,我打算将需要抽样的数据假设为一个不知道其长度的列表(在抽样函数运行的过程中,不去查询列表的长度)
#先假定一个长列表作为测试数据
import random
a=[1,2,32,3,4,4,4,43,43,43,3,23,3,4,4,55,5,6,6,6,6,54,3,4,3,43,4,34,32,3,1,3,4,34,3,4,1,1,3]

def sampling(sample):
    c=0
    for b in sample:
        # 先给抽取到的值choice赋初值
        if c==0:
            choice=b
        #之后,每遇到一个新的值,就要进行判定
        z=random.randint(0,c+1)
        #这里实际上就是用random产生的随机数来判断    我发现产生随机数时是概率均等的,
        # 而题意要求的是"第二个是1/2的概率 第三个是1/3的概率..."所以就想到了用这个来模拟(应该是对的吧)
        if z!=(c+1):
            c+=1
            pass
        else:
            choice=sample[c+1]
            c+=1
        # print(choice)

    return choice

if __name__ == '__main__':
    for e in range(10):
        print('\n',str(sampling(a)))



