#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 0029 9:11
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm

#为什么函数名字可以当做参数用？
#在python中万物皆对象,函数名也不过代表了在内存中的空间,也是一个对象

'''
map()函数
功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator(迭代器)返回
语法：map(func, lsd)
参数1是函数，参数2是序列
'''

# # map函数
# import doctest
# def double(nun):
#     '''
#     :param nun:
#     :return:
#     example:
#     >>> double(10)
#     10
#     '''
#     return nun**2
#
# l=map(double,[x for x in range(1,int(input('输入x'))+1)])
# print(l)           #不然返回的是一个map对象
# print(list(l))    #这个实际上是强制让迭代器运算完再添加到列表中

# print(list([x*x for x in range(1,int(input("请输入一个数字\n"))+1)]))     #用列表生成式

# print(list(map(lambda x:x**2,range(1,int(input("请输入一个数字\n"))+1))))  #用匿名函数



'''
reduce()函数
功能：一个函数作用在序列上，这个函数必须接受**两个参数**，reduce把结果继续和序列的下一个元素累计运算
语法：reduce(func，lsd)
参数1为函数，参数2为列表
reduce(f，[1，2，3，4])等价于f(f(f(1，2)，3)，4)，类似于递归           返回的是一个值
'''
# from functools import reduce
#
# list1=[1,2,3,23,23]
# print(reduce(lambda x,y:int(x)+int(y),list1))
# # l=map(int,list1)
# # print(list(l))
# # print(int('1'))
'''

'''

# import itertools
# myList = list(itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm",repeat=6))
# #可以尝试，有可能电脑会卡住
# #多线程也不行，电脑内存不够，咋处理都白搭
# print(len(myList))

# import time
# import itertools
#
# password = ("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm",repeat=6))
# #print(len(myList))
# while True:
#     try:
#         str1 = next(password)
#         time.sleep(0.00001)
#         print(str1)
#     except StopIteration as e:
#         break

# list1=[122,3,'1232',3,4,34,45]
# print(sorted(list1,key=int))    #不会改变列表内的值
#
# print(sorted(list1,key=lambda x:int(x)%10))


# import unittest
#
# class Test(unittest.TestCase):
#     def setUp(self):
#         print("开始测试")
#
#     def tearDown(self):
#         print('结束测试')
#
#     def test_double(self):
#         self.assertEqual(double(10),10,"测试有误")
#
#
# if __name__ == '__main__':
#     unittest.main()

import  re

# print(re.findall(r'[a-z]{5}','sjdsdjuuuu29129832983e83eu48rur8ru884u84ur84ur84ru84ur84ur84ur84r'))
# print(re.findall('a.*?z','asdsidjzawewdeezeefkkmdzaewiesmfzwmdksmaxz'))
# print(re.findall('a.*z','asdsidjzawewdeezeefkkmdzaewiesmfzwmdksmaxz'))
# print(re.findall(r'fist','dsdsdjsjfist'))

print(re.findall('dd[1-2]',r'ddq2ddd43dd12ddawwdw1dd1ddd3dd2'))

print(re.findall('[\u4e00-\u9fa5]',"nis你好野啊近段时间大家,sd,sdsdsdsdsds"))   #检索中文字符

print(re.findall('[^12323333wwewddsxc]','wdwdwdd123e3r4rr'))

print(re.findall('\d','dsds12edweew12ed'))

print(re.findall('\D','dkhd2ue3je3hej3j3eh3uehu'))
