#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc

# 1.对一个列表进行冒泡排序【升序】
# list1=[9,8,7,6,5,4,56,78,43,21,1]
# b=0
def maopao(list1,flag):
    b=0
    if not flag:
        for c in range(len(list1)):
            for a in range(len(list1)-1):
                b=a+1
                if list1[a]>list1[b]:
                    list1[a],list1[b]=list1[b],list1[a]
    else:
        for c in range(len(list1)):
            for a in range(len(list1)-1):
                b=a+1
                if list1[a]<list1[b]:
                    list1[a],list1[b]=list1[b],list1[a]
    return  list1
# print(list1)



# 2.从控制输入一串字符串，要求字符串只能数字字母下划线，并且长度大于等于20，
# 若不符合条件重新输入，输入完毕之后，要求从控制台输入一个字符，使用自己输入的字符，
# 来对字符串进行切片，切片完毕之后，并且去掉空串，删除列表中的重复元素。
# def input1():
#     a=""
#     a=input("请输入一串字符串，只能包含数字字母下划线，并且长度大于等于20,否则将重新输入\n")
#     for c in a:
#         if  not (len(a) >= 20 and ord(c) == 95 or 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90 or 87 <= ord(c) <= 122):
#             print("输入的字符串有误,请重新输入")
#             input1()
#     change(a)
# def change(a):
#     d=""
#     d=list(set(a.split(input("请输入一个字符"))))
#     for e in d:
#         if e=="":
#             d.pop(d.index(e))
#     print(d)
# input1()


# 3.从控制台输入一串字符串，实现字符串翻转比如:hello => olleh 使用三种以上的方法实现

# a=""
# a=input("请输入一行字符串:\n")
#
# a=list(a)
# print(a)
# a.reverse()
# print(a)
#
# a=list(a)
# c=[]
# for b in range(len(a)):
#     c.append(a.pop())
# print(c)
#
#
# reduce(lambda x,y : y+x, a_string)


# 4.写一个双色球彩票系统，系统可以随机产生一组数据，一组彩票数据有六位数，这六位数的的取值范围是0和1。
#
# 一张彩票是两块钱，用户可以选择购买彩票的张数，若余额充足，用户可以开始游戏，要求从控制台输入6位的0或者1
#
# 若用户输入的不对，要求用户重新输入，直到输入成功为止。若中奖的话，中奖金额为购买彩票金额的50倍，
#
# 若没中奖则打印继续努力！用户可以选择继续买票或者是退出。买票和退出的时候要求打印剩余金额。
#
# 余额不足的时候提示用户充值。
# 以下代码已作废!!!
# import random
# global code #中奖彩票号码
# code=""
# global money#玩家的金额数
# money=0
# global zhu #玩家买的数
# zhu=0
# global cus #玩家的彩票号码
# cus=""
# # 生成中奖彩票号码
# def codec(b): #b用来判断是生成中奖彩票号码还是玩家的彩票号码
#     codes = []
#     for i in range(6):
#         a = ""
#         a = random.randint(1, 6)
#         codes.append(str(a))
#     print(codes)
#     print("".join(codes))
#     if b == 1:  # 生成中奖彩票号码
#         global code
#         code=codes
#         return code
#     else:       #生成玩家的彩票号码
#         global cus
#         cus=codes
#         return cus
#
# # 判断用户的金额是否够买彩票，如果不够就让他充值，充值足够后返回能够购买几注的注数，如果不愿充值则返回0
# def moneyd(c):
#     global money
#     if c==2:
#         if money<=2:
#             print("余额不足请充值:\n")
#             if input("是否充值?\n")=="是":
#                 money+=int(input("请输入充值金额:\n"))
#                 moneyd(2)
#             else:
#                 return 0
#         else:
#             return money//2
#     else:
#         bay()
#         return -1

#
#
# 主程序，用户购买彩票的入口,
# def bay():
#     global money
#     money=0
#     while 1:
#         a=0
#         a=moneyd(2)
#         if a>0:
#             b = input("请问你打算购买多少注？\n")
#             if b<=a:
#                 money-=2*b
#                 print("你的剩余金额为%d"%money)
#             else:
#                 print("你的余额不足以购买注数为%d的彩票"%b)
#                 c=input("请问你选择1:重新输入购买的注数  2:充值")
#                 moneyd(c)
#                 continue
#         else:
#             print("玩彩票不够钱还不充值,滚蛋")
#         d=codec(1)
#         e=codec(0)
#         if d==e:
#             print("恭喜你中奖了")
#             money+=(100*b)
#             print("你目前金额为%d"%money)
#         else:
#             print("抱歉你未中奖")
#         if input("是否继续?是/否")=="是":
#             continue
#         else:
#             break
#
# bay()

#这才是有效的
# import random
#  #中奖彩票号码
# code=""
# #玩家的金额数
# global money
# money=0
#  #玩家买的数
# zhu=0
#  #玩家的彩票号码
# cus=""
#
# def codec(b): #b用来判断是生成中奖彩票号码还是玩家的彩票号码
#     codes = []
#     for i in range(6):
#         a = ""
#         a = random.randint(1, 6)
#         codes.append(str(a))
#     print(codes)
#     print("".join(codes))
#     if b == 1:  # 生成中奖彩票号码
#         code=""
#         code=codes
#         return code
#     else:       #生成玩家的彩票号码
#         cus=""
#         cus=codes
#         return cus
#
# def moneyd(c,d):
#     global money
#     a = 0
#     if c==2:
#         if d<2:
#             print("余额不足请充值:\n")
#             if input("是否充值?\n")=="是":
#                 d+=int(input("请输入充值金额:\n"))
#                 money+=d
#                 return moneyd(2,d),d
#             else:
#                 return 0,d
#         else:
#             a=d//2
#             return a,d
#     else:
#         return -1,d
#
# while 1:
#     a=0
#     f=0
#     g=0
#     g=moneyd(2,money)
#     if type(g[0])!=int:
#         a=g[0][0]
#     else:
#         a=g[0]
#     if a>0:
#         b=0
#         b = int(input("请问你打算购买多少注？\n"))
#         if b<=a:
#             money-=(2*b)
#             print("你的剩余金额为%d"%money)
#         else:
#             print("你的余额不足以购买注数为%d的彩票"%b)
#             c=input("请问你选择1:重新输入购买的注数  2:充值")
#             moneyd(c,money)
#             continue
#     else:
#         print("玩彩票不够钱还不充值,滚蛋")
#         break
#     d=codec(1)
#     e=codec(0)
#     if d==e:
#         print("恭喜你中奖了")
#         money+=(100*b)
#         print("你目前金额为%d"%money)
#     else:
#         print("抱歉你未中奖")
#     if input("是否继续?是/否")=="是":
#         continue
#     else:
#         break


# 5.从控制台输入一个时间，打印这个时间的下一秒[16:33:55]
# [23:59:59] 显示[00:00:00]
# a=input("请输入一个时间,格式为[23:59:59]:\n")
# d=a.lstrip("[").rstrip("]")
# print(d)
# b=d.split(":")
# print(b)
# if b[2]!="59" :
#     if b[1]!="59":
#         if b[0]!="23":
#             b[2]=str(int(b[2])+1)
# elif b[1]!="59":
#         if b[0]!="23":
#             b[2]="00"
#             b[1]=str(int(b[1])+1)
# elif b[0]!="23":
#     b[2]="00"
#     b[1]="00"
#     b[0]=str(int(b[0])+1)
# else:
#     b[2] = "00"
#     b[1] = "00"
#     b[0] = "00"
# c="["+":".join(b)+"]"
# print(c)



# 6.写一个学生管理系统
# ----------------------------------------------------------
# |                    欢迎进入学生管理系统                   |
# |                                                         |
# | 1.学生信息录入      2.学生成绩查询     3.查找学生信息      |
# | 4.录入学生成绩      5.课程平均值     6.所有学生信息        |
# ----------------------------------------------------------
#
# 学生信息：
# 学号：      姓名：      性别：     成绩：     电话
# 学生信息结构:       学号:[姓名,性别,成绩,电话]   用字典存储

# student={1:["沙雕0","男",50,136666],
#          2:["沙雕1","女",60,136667],
#          3:["沙雕2","男",70,136668],
#          4:["沙雕3","女",80,136669],
#          5:["沙雕4","男",90,136660]}
# b=[]
# while 1:
#     print(" ----------------------------------------------------------\n"+
#           "|                    欢迎进入学生管理系统                  |\n"+
#           "|                                                          |\n"+
#           "| 1.学生信息录入      2.学生成绩查询     3.查找学生信息    |\n"+
#           "| 4.录入学生成绩      5.课程平均值       6.所有学生信息    |\n"+
#           " ----------------------------------------------------------\n")
#     a=input("请选择使用的功能:")
#     if a=="1":
#         d=True
#         while 1:
#             if d==False:
#                 print("输入的学生信息有误,请重新输入\n")
#             a=input("请输入学生的信息,以 姓名,性别,成绩,电话的方式\n")
#             a.lstrip("[").rstrip("]")
#             b=a.split(",")
#             if b[1]!="男"and b[1]!="女":
#                 d=False
#             else:
#                 for c in b[2]:
#                     if 48<=ord(c)<=57:
#                         continue
#                     else:
#                         d=False
#                 for e in b[3]:
#                     if 48 <= ord(c) <= 57:
#                         continue
#                     else:
#                         d = False
#                 if d==True:
#                     break
#         student[len(student)+1] =[b[0],b[1],int(b[2]),int(b[3])]
#         print("录入成功")
#         continue
#     elif a=="2":
#         serch=int(input("请输入学生学号\n"))
#         print("该学生的成绩为:"+str(student[serch][2]))
#         continue
#     elif a=="3":
#         serch = int(input("请输入学生学号\n"))
#         print("该学生的信息为:" + str(student[serch]))
#         continue
#     elif a=="4":
#         serch = int(input("请输入学生学号\n"))
#         achievement=int(input("请输入该学生的成绩\n"))
#         student[serch][2]=achievement
#         print("该学生的当前信息为:" + str(student[serch]))
#         continue
#     elif a=="5":
#         sun=0
#         for a in range(1,len(student)+1):
#             sun+=student[a][2]
#         print("平均成绩为:"+str(sun/len(student)))
#         continue
#     elif a=="6":
#         print(student)
#         continue





