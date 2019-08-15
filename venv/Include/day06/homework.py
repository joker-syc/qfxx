#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc


# 1.画中国国旗
# import turtle
# import math
# length=500
# turtle.begin_fill()
# turtle.fillcolor("red")
# turtle.forward(length)
# turtle.right(90)
# turtle.forward(0.66*length)
# turtle.right(90)
# turtle.forward(length)
# turtle.right(90)
# turtle.forward(0.66*length)
# turtle.right(90)
# turtle.end_fill()
#
# turtle.up()
# turtle.forward(0.15*length)
# turtle.right(90)
# turtle.forward(0.15*length)
# turtle.left(90)
# turtle.down()
# turtle.begin_fill()
# turtle.fillcolor("yellow")
# for _ in range(5):
#     turtle.forward(0.12*length)
#     turtle.right(144)
# turtle.end_fill()
#
# turtle.up()
# turtle.forward(0.06*length)
# turtle.right(90)
# turtle.forward(0.12*(math.sin(math.radians(54))* (0.5*math.tan(math.radians(36))) / (1+math.sin(math.radians(54))))*length)
#
# turtle.left(144)
# turtle.forward(0.1*length)
# turtle.right(18)
# turtle.down()
#
# turtle.begin_fill()
# turtle.fillcolor("yellow")
# for i in range(5):
#     turtle.forward(0.08*length)
#     turtle.left(144)
# turtle.end_fill()
#
# turtle.up()
# turtle.left(198)
# turtle.forward(0.1*length)
# turtle.right(216)
# turtle.forward(0.1*length)
# turtle.right(18)
# turtle.down()
#
# turtle.begin_fill()
# turtle.fillcolor("yellow")
# for i in range(5):
#     turtle.forward(0.08*length)
#     turtle.left(144)
# turtle.end_fill()
#
# turtle.up()
# turtle.left(198)
# turtle.forward(0.1*length)
# turtle.right(216)
# turtle.forward(0.1*length)
# turtle.right(18)
# turtle.down()
#
# turtle.begin_fill()
# turtle.fillcolor("yellow")
# for i in range(5):
#     turtle.forward(0.08*length)
#     turtle.left(144)
# turtle.end_fill()
#
# turtle.up()
# turtle.left(198)
# turtle.forward(0.1*length)
# turtle.right(216)
# turtle.forward(0.1*length)
# turtle.right(18)
# turtle.down()
#
# turtle.begin_fill()
# turtle.fillcolor("yellow")
# for i in range(5):
#     turtle.forward(0.08*length)
#     turtle.left(144)
# turtle.end_fill()
#
# turtle.done()

# 2.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
# 各是多少？【存到list中】
# num="1234"
# out=[]
# for a in num:
#     for b in num:
#         for c in num:
#             dd=a+b+c
#             if dd.count("1")>1 or dd.count("2")>1 or dd.count("3")>1 or dd.count("4")>1:
#                 continue
#             else:
#                 print(dd)
#                 out.append(dd)
# print(set(out))


# 3.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
# 可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，
# 超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# a=int(input("请输入利润总数\n"))
# if a<=100000:
#     print("奖金总额为:%d"%(a*0.1))
# elif a<=200000:
#     print("奖金总额为:%d" % (10000+(a-100000)*0.075))
# elif a<=400000:
#     print("奖金总额为:%d" % (17500+(a-200000)*0.05))
# elif a<=600000:
#     print("奖金总额为:%d" % (27500+(a-400000)*0.03))
# elif a<=1000000:
#     print("奖金总额为:%d" % (33500+(a-600000)*0.015))
# else:
#     print("奖金总额为:%d" % (39500+(a-1000000)*0.075))


# 4.将一个列表的数据复制到另一个列表中。使用三种以上的方法
# copy.copy()
# copy.deepcopy()
# list1=[[1,2,3,4,[1,2,[[3,3],3]]],3,3,[233,3]]


# 5.从控制台输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# text=input("请输入一行字符")
# L=0
# Letter={}
# s=0
# n=0
# num={}
# o=0
# other={}
# for aim in text:
#     if 65<=ord(aim)<=90 or 97<=ord(aim)<=122:
#         if aim in Letter:
#             L+=1
#             Letter[aim]+=1
#             continue
#         else:
#             L+=1
#             Letter[aim]=1
#             continue
#     elif 48<=ord(aim)<=57:
#         if aim in num:
#             n+=1
#             num[aim]+=1
#             continue
#         else:
#             n+=1
#             num[aim]=1
#             continue
#     elif ord(aim)==32:
#         s+=1
#     else:
#         if aim in other:
#             o+=1
#             other[aim]+=1
#             continue
#         else:
#             o+=1
#             other[aim]=1
#             continue
#
# print("字母统计",Letter,"总个数为%d"%L)
# print("数字统计",num,"总个数为%d"%n)
# print("空格统计",s,"总个数为%d"%s)
# print("其他字符统计",other,"总个数为%d"%o)


# 6.写代码，有如下列表，请按照功能要求实现每一个功能
# li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# a.请输出"Kelly"
# b.找到 'all'元素并将其修改为"ALL"
# import copy
# li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# print(li[2][1][1].title())
# b=[]
# def inList(list1):
#     for a in list1:
#         if type(a)==list:
#             print(a)
#             inList(a)
#         elif a=="all":
#             dd=list1.index(a)
#             list1[dd]="All"
#             break
#         else:
#             continue
# inList(li)
# print(li)


# 7.猜数字
# 很多人在聚餐时都玩过猜数字游戏，由某人随机出一个指定范围内的数，
# 然后其他人一个一个猜，猜的过程中区间不断缩小，直到猜中为止。
# 这里的猜数字游戏就是用程序来代替那个出数字的人，程序算法设计为：
#
# 1.输入数字区间--->2.系统产生区间内的随机数--->3.玩家输入自己猜的数字--->
# 4.比较玩家猜的与答案的高低并提示--->5.未猜中则回到3，猜中则提示猜次数
# import random
#
# space=input("请输入数字区间\n")   #格式为3,6
# def create(space):
#     if int(space[0])>=int(space[-1]):
#         print("输入错误的区间")
#         return "错误"
#     else:
#         x=random.randint(int(space[0]),int(space[-1]))
#         print(x)
#         return x
# key=create(space)
# while 1:
#     dd=int(input("请输入猜的数字\n"))
#     if dd=="错误":
#         continue
#     if dd==key:
#         print("恭喜你猜中了")
#         break
#     elif dd>key:
#         print("大了")
#         continue
#     else:
#         print("小了")
#         continue


