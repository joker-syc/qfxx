#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 0026 19:50
# @Author  : joker-syc
# @Site    : 
# @File    : zuoye.py
# @Software: PyCharm


#....又没有更好,改成json进行持久化太麻烦,要改好多地方
#算了,就不在系统运行的时候持久化,等系统退出的时候持久化把
#搞定了
'''
将ATM系统补全，并且将数据使用json模块进行持久化。
'''
'''
有两个磁盘文件A和B,各存放一行字母,
要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''

# with open(file='A.txt',mode='r',encoding='utf-8') as a:
#     # print(d)
#     A=[]
#     for c in a.read():
#         A.append(c)
#
# with open(file='B.txt',mode='r',encoding='utf-8') as b:
#     B=[]
#     for d in b.read():
#         B.append(d)
#
# with open(file='C.txt',mode='w',encoding='utf-8') as c:
#     C=A+B
#     C.sort()
#     print(C)
#     c.write(str(C))

'''
从键盘输入一个字符串，将小写字母全部转换成大写字母，
然后输出到一个磁盘文件"test"中保存。
'''
# a=input('请输入一行字符串\n')
# a=a.upper()
# print(a)
# with open(file='test.txt',mode='w',encoding='utf-8') as b:
#     b.write(a)

'''
检验__doc__内置变量的作用
'''
# class ss:
#     def dd(a):
#         '''
#         sha
#         :return:
#         '''
#         print(__doc__)       #这个输出的是当前的模块的从上往下第一个包含在'''   '''中的内容
#
# s=ss()
# s.dd()

# print(__file__)    #获取当前模块的.py文件的绝对路径

