#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 0026 8:44
# @Author  : joker-syc
# @Site    : 
# @File    : test.py
# @Software: PyCharm

# import json
#
# class Person :
#
#     def __init__(self,name,sex):
#         self.name=name
#         self.sex=sex
#
#
# def person2dict(per):
#     return {'name':per.name,'sex':per.sex}
#
# if __name__ == '__main__':
#     per=Person('沙雕','女')
#     with open('dd.txt','w',encoding='GBK') as f:
#         json.dump(per,f,default=person2dict)
#
#     with open('dd.txt', 'w', encoding='GBK') as f:
#         pass
#         # json.load(f,)

# import csv
#
# def readCsv(path,n):
#     with open(path,mode='r',encoding='GBK') as f:
#         list1=[]
#         for a in range(n):
#             list1.append(next(csv.reader(f)))
#         return list1
#
#
# def writeCsv(path,list1,n):
#     with open(path,'w',encoding='GBK') as f:
#         for a in range(n):
#             csv.writer(f).writerow(list1[a])
#
# filelist=readCsv(r'C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day15\002.csv',10)
# writeCsv('0023.csv',filelist,5)

# print(list(lambda x:x*x,[1,2,3,4]))     #这个用法是错误的

# print(list(map(lambda x:x*x,[1,2,3,4])))    #这个才对

#
# class A:
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def run2(self,run):
#         print(run)
#
# class B(A):
#
#     def __init__(self,name,age,run):
#         self.name=name
#         self.age=age
#         self.run=run
#
#     def run1(self):
#         print(self.run)
#
# a=A('猪',1,3)



