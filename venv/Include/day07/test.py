#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc

# t1=(1,)
# t2=(2,)
# t3=t1+t2
# print(id(t1[0]))
# print(id(t3[0]))
# print(id(t2[0]))
# print(id(t3[1]))

# import os
# print(os.getcwd())

# 列表生成式
# 强制让for循环写在同一行

# print([x*x for x in range(1,100,2)])
# print([x for x in range(1,101) if x%3!=0])

#生成器:可以一边循环一边计算的机制
# 生成器只能使用一次(对生成器做的操作,遍历之类的)
#
#迭代器,生成器是典型的迭代器,
'''
迭代器不但能作用于for循环,还能被next函数不断调用并且返回下一个值,
直到出现StoIteration错误,表示遍历完毕

'''

# li=[(1,2),(1,3)]  #这里只会保留后面的
# print(dict(li))

# def quhe(n):
#     sun=0
#     for i in range(n+1):
#         sun+=i
#     return sun
#
# print(quhe(2))

# def fa(n):
#     sun=1
#     for i in range(1,n+1):
#         sun*=i
#     return sun
#
# print(fa(4))


# def sun(n):
#     sun=0
#     for i in range(1,n+1):
#         sun+=fa(i)
#     return sun
# print(sun(10))


# 1.设计一个函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def length(ob):
#     if len(ob)<5:
#         print("传入的",type(ob),"对象长度不大于5")
#     else:
#         print("传入的",type(ob),"对象长度大于5")
# length(["sdsd",334,44,[3,34,5,6]])    #同时也说明len()函数只能统计第一层的数目

# 2.设计一个函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容【字符串中含有空格，列表与元组中函数有空串】。
#
# 若含有则返回True，否则返回False
#
# ”hello world“ [12,34,"",23]

# def ifNull(dd):
#     for a in dd:
#         if type(dd)==str:
#             if a==" ":
#                 return True
#             else:
#                 print(a)
#                 continue
#         elif type(dd)==list:
#             if type(a)!=list:
#                 if a=="":
#                     return True
#                 else:continue
#             else:
#                 print(a)
#                 ifNull(a)
#                 continue
#         elif type(dd)==tuple:
#             if type(a)!=tuple:
#                 if a=="":
#                     return True
#                 else:continue
#             else:
#                 print(a)
#                 ifNull(a)
#                 continue
#     return False
# print(ifNull((1,23,"")))


# 3.设计一个函数，从控制台输入一个整数，计算整数绝对值的阶乘，n！=1 x 2 x … x n【写成函数】

# def Factorial(nun):
#     if nun<0:
#         nun=-nun
#     sun=1
#     for i in range(1,nun+1):
#         sun*=i
#     return sun
# print(Factorial(int(input("请输入一个整数"))))


# 4.从控制台输入两个正数，求这两个正数的最大公约数，与最小公倍数
#
# 注意：最大公约数的公式：
#
# m % n = r ，m = n  n = r  ，r == 0  输出m ，若不为0则继续循环
#
# 最小公倍数的公式：
#
# 最小公倍数 = 两个正数的乘积/最大公约数

# a=int(input("请输入一个正数"))
# b=int(input("请输入另一个正数"))
#
# def maxyue(m,n):
#     r = 1
#     while r!=0:
#         r=0
#         r=m%n
#         m=n
#         n=r
#     return m
#
# def minbei(m,n):
#     return m*n/maxyue(m,n)
# print(maxyue(a,b))
# print(minbei(a,b))

# 1.歌词解析器

# musicLrc = '''
# [00:03.50]传奇
# [00:19.10]作词：刘兵 作曲：李健
# [00:20.60]演唱：王菲
# [00:26.60]
# [04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
# [04:49.00]
# [02:47.44][00:43.69]再也没能忘掉你容颜
# [02:54.83][00:51.24]梦想着偶然能有一天再相见
# [03:02.32][00:58.75]从此我开始孤单思念
# [03:08.15][01:04.30]
# [03:09.35][01:05.50]想你时你在天边
# [03:16.90][01:13.13]想你时你在眼前
# [03:24.42][01:20.92]想你时你在脑海
# [03:31.85][01:28.44]想你时你在心田
# [03:38.67][01:35.05]
# [04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
# [04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
# [04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
# [04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
# [04:39.55][04:09.00][02:07.85]
# '''
import  time
import pygame
list1={}
timeorder=[]
def song(music):
    songList=music.splitlines()
    for songLine in songList:
        # 依据]分割时间戳与歌词
        if songLine:
            songLineLine=songLine.split("]")
            for end in songLineLine:
                endLine=end.split("[")
                for endLineLine in endLine:
                    #此时这里还是一行歌词
                    if endLineLine:
                        if 48<=ord(endLineLine[0])<=57:
                            list1[int(endLineLine[1:2])*60+float(endLineLine[-5:-1])]=songLineLine[-1]
                            timeorder.append(int(endLineLine[1:2])*60+float(endLineLine[-5:-1]))
    timeorder.append(0)
    timeorder.sort()
    print("歌词解析完成")
def start(multiple=1):
    print("开始播放")
    music=r"C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day07\chuanqi.mp3"
    pygame.mixer.init()
    mm=pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    a=1
    for song1 in timeorder:
        if song1 in list1:
            if list1[song1]:
                if a<=len(timeorder)-1:
                    time.sleep((timeorder[a]-song1)/multiple)
                    print(list1[song1])
                else:
                    print(list1[song1])
            else:
                if a<=len(timeorder)-1:
                    time.sleep((timeorder[a]-song1)/multiple)
        a+=1

# song(musicLrc)
# # print(timeorder)
# # print(list1)
#
# start(int(input("请选择以几倍速播放")))


# music = r"C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day07\chuanqi.mp3"
# pygame.mixer.init()
# mm = pygame.mixer.music.load(music)
# pygame.mixer.music.play()
# time.sleep(10)
