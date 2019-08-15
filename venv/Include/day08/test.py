#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc
from Include.day07.test import song,start

musicLrc = '''
[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:36.75][02:35.90][00:32.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:43.44][00:39.69]再也没能忘掉你容颜
[02:50.83][00:47.24]梦想着偶然能有一天再相见
[02:58.32][00:54.75]从此我开始孤单思念
[03:04.15][01:00.30]
[03:05.35][01:01.50]想你时你在天边
[03:12.90][01:09.13]想你时你在眼前
[03:20.42][01:16.92]想你时你在脑海
[03:27.85][01:24.44]想你时你在心田
[03:34.67][01:31.05]
[04:05.46][03:35.37][01:31.75]宁愿相信我们前世有约
[04:12.37][03:42.38][01:38.47]今生的爱情故事 不会再改变
[04:20.82][03:50.83][01:47.18]宁愿用这一生等你发现
[04:27.38][03:57.40][01:53.43]我一直在你身旁 从未走远
[04:35.55][04:05.00][02:03.85]
'''
song(musicLrc)
start()



# from Include.day05.zuoye import maopao
# def sortt(list1,re=False):
#     a=maopao(list1,re)
#     print(a)
# sortt([9,8,7,6,5,4,56,78,43,21,1])
# sortt([9,8,7,6,5,4,56,78,43,21,1],True)
#
# def max1(*numb):
#     maxnum=numb[0]
#     for a in numb:
#         if a>=maxnum:
#             maxnum=a
#         else:
#             continue
#     return maxnum
# print(max1(2,34,5,67,896,34213,45,55656,44,4,34,34,34,3445,55,5))
#
# from collections.abc import Iterable
# def sun(*args):
#     if len(args)==1:
#         if isinstance(args,Iterable):
#             maxnum=args[0][0]
#             for a in args[0]:
#                 if a>maxnum:
#                     maxnum=a
#             return maxnum
#         else:
#             print("请输入一个可迭代对象")
#     else:
#         maxnum=args[0]
#         for a in args:
#             if a > maxnum:
#                 maxnum = a
#         return maxnum
#     # print(args)
#
# print(sun([1,23,4,5,4,5,6,6,7]))
#
# dic1={1:"h",2:"b",3:"w"}
# list1=["h","b","w"]
#
# print(dict(zip(dic1.values(),dic1)))
#
# print(dict(zip(dic1.values(),list(dic1)[::-1])))
#
# from collections.abc import Iterable
# if isinstance(list(dic1).reverse(),Iterable):
#     print("dd")
# else:print("gg")                          #由此可以发现list.reverse()返回不是一个可迭代对象
#
# def agec(func):
#     def inner(age):
#         if age >160 or age<0:
#             print("见鬼了")
#         else:
#             print("我今年%d"%age)
#     return inner
#
# @agec
# def age (age):
#     print("我今年%d"%age)
#
# age(200)
#
#
# def loginc(func):
#     def inner(name,passwd):
#         if 5<=len(name)<=8 and len(passwd)==6 and name[0].isalpha():
#             a=func(name,passwd)
#             return a
#         else:
#             print("用户名或密码错误")
#     return inner
#
# @loginc
# def login(name,passwd):
#     if name=="admin" and passwd=="123456":
#         return True
#     else:
#         return False
#
# print(login("h(*dmin","123456"))
#
# import functools
# def addnum(a,b):
#     sun=0
#     sun=a+b
#     return sun
# addnum1=functools.partial(addnum,b=10)
# print(addnum1(1))