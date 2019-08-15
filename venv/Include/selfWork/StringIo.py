#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc
# 2019/7/13/15:00
'''
StringIO
很多时候,数据读写不一定是文件,也可以在内存中读写.
StringIO就是在内存中读写str
要把str写入StringIO,我们需要先创建一个StringIO,然后像文件一样写入即可
'''
from io import StringIO
# f=StringIO()
# f.write("hello")  #该语句会返回输入的字符个数
# print(f.getvalue()) #.getvalue()用于获取写入内存的值

# f=StringIO("努力就会有回报!!!") #此时可以用文件读取的函数读取数据 与open()类似（open()是与具体的文件打交道）
# while 1:
#     a=f.readline()
#     if a
