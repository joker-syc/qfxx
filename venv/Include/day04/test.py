#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc

#上课时敲的代码,,,,,,还有作业
''''
# d=int(input("请输入一个数字:"))
# i=1
# z=1
# while i<=d:
#     z*=i
#     i+=1
#
# print(z)


# a=1
# while a<20:
#     a+=1
#     if a==10:
#         pass
#         print("dd")
#     print(a)

# a=1
# c=int(input("请输入一个数字:"))
# sum=0
# while a<=c:
#     b=1
#     z=1
#     while z<=a:
#         b*=z
#         z+=1
#     sum+=b
#     a+=1
# print("前%d项阶乘和的为%d"%(c,sum))
#
# a=int(input("请输入一个数字:"))
# b=1
# c=1
# d=0
# while b<=a:
#     c*=b
#     d+=c
#     b+=1
# print(d)

# 控制循环的变量要与循环体的式子分离
# i=int(input("请输入一个数字:"))
# z = 0
# b = 1
# for n in range(1,i+1):
#     z+=n
#     b*=n
# print(z)
# print(b)



# for n in range(1,i+1):
#     dd=1
#     for b in range(1,n+1):
#         dd*=b
#     z+=dd
# print(z)



# 9*9乘法表
# a=int(input("请输入数字:"))
# 正常
# for b in range(1,a+1):
#     for c in range(1,b+1):
#         print("%d*%d=%d"%(b,c,b*c),end="  ")
#     print()

# 镜像
# z=0
# for b in range(1,a+1):
#     zz=1
#     for c in range(b,0,-1):
#         z=a-b
#         if zz==1:
#             for d in range(1,z+1):
#                 print(end="\t \t")
#         zz-=1
#         print("%d*%d=%d"%(b,c,b*c),end="\t")
#     print()

# 上下逆
# for b in range(a,0,-1):
#     for c in range(1,b+1):
#         print("%d*%d=%d"%(b,c,b*c),end="  ")
#     print()

# 左右逆
# for b in range(a,0,-1):
#     for c in range(1,b+1):
#         print("%d*%d=%d"%(b,c,b*c),end="  ")
#     print()

# 上下左右逆
# z=0
# for b in range(a,0,-1):
#     zz=1
#     for c in range(b,0,-1):
#         z=a-b
#         if zz==1:
#             for d in range(1,z+1):
#                 print(end="\t \t")
#         zz-=1
#         print("%d*%d=%d"%(b,c,b*c),end="\t")
#     print()

# 用while实现
# 正常
# b=1
# while b<=a:
#     c=1
#     while c<=b:
#         print("%d*%d=%d"%(b,c,b*c),end="\t")
#         c+=1
#     b+=1
#     print("")


# 镜像
# b=1
# while b<=a:
#     c=b
#     d=0
#     zz=1
#     while c>=1:
#         if zz==1:
#             while d<=a-b:
#                 print('',end="\t\t")
#                 d+=1
#         print("%d*%d=%d"%(b,c,b*c),end="\t")
#         c-=1
#         zz-=1
#     b+=1
#     print("")

# 上下翻转
# b=a
# z=0
# while b>=1:
#     c=1
#     z=b
#     while z>=1:
#         print("%d*%d=%d"%(b,c,b*c),end="\t")
#         c+=1
#         z-=1
#     b-=1
#     print("")



# 上下左右逆
# b=a
# z=0
# while b>=1:
#     c=1
#     z=b
#     zz=1
#     d=a-b
#     while z>=1:
#         if zz == 1:
#             while d>0:
#                 print(end="\t\t")
#                 d-=1
#         print("%d*%d=%d"%(b,c,b*c),end="\t")
#         c+=1
#         z-=1
#         zz=-1
#     b-=1
#     print("")


# 计算1~100以内所有能被3或者17整除的数的和
# sum=0
# for a in range(1,101):
#     if a%3==0 or a%17==0:
#         print(a)
#         sum+=a
#     else:pass
# print(sum)


# 计算100~999的水仙花数的个数，并且打印水仙花数
# sun=0
# g=0
# for a in range(100,1000):
#     if int(a/100)**3+int((a%100)/10)**3+(a%10)**3==a:
#         print("水仙花数有:%d"%(a))
#         sun+=a
#         g+=1
#     else:pass
# print("总和为%d,总个数为%d"%(sun,g))


# 计算10000~99999回文数的个数，并且打印回文数
# sun=0
# g=0
# for a in range(10000,100000):
#     if int(a / 10000) == a % 10 and int((a % 10000) / 1000) == int((a % 100) / 10):
#         print("回文数有:%d"%(a))
#         sun+=a
#         g+=1
#     else:pass
# print("总和为%d,个数有%d"%(sun,g))


# 计算200~500以内能被7整除但不是偶数的数的个数
# g=0
# for a in range(200,501):
#     if a%7==0 and a%2!=0:
#         print("%d"%(a))
#         g+=1
#     else:pass
# print("个数有:%d"%(g))


# 押宝游戏：
# 开始游戏 -> 投入赌金 ->
# 循环  ：
# 押宝【5块钱一次】 -> 开奖  --》中奖/未中奖 中奖奖励的金额【1~10】--》
# 用户输入是否继续 【当余额不足请充值，若不充值则退出游戏】


# import random
# k=0
# dd=""
# k=int(input("请输入投入赌金额数"))
# while 1:
#     if k<5 :
#         print("余额不足请充值")
#         dd=input("是否充值")
#         if dd=="是":
#             while k<5:
#                 f=0
#                 f=int(input("请输入充值数,充值数必须大于5,否则须再次充值"))
#                 k += f
#                 if k<5:
#                     print("总额仍然不大于5,须再次充值")
#         else:
#             print("穷B再见")
#             break
#     else:
#         e = input("请选择压大还是小:")
#         k-=5
#         gg = random.randint(1, 6)
#         print(gg)
#         zz = ""
#         if gg <= 3:
#             zz = "小"
#         else:
#             zz = "大"
#         if e == zz:
#             award=random.randint(1,10)
#             print("恭喜你中奖了,奖金为%d"%(award))
#             k+=award
#         else:
#             print("抱歉你未中奖")
#         print("是否继续?")
#         if input("是//否") == "是":
#             pass
#         else:
#             break
# print("再见")



# 百钱买百鸡，现有100文钱，公鸡5文钱一只，母鸡3文钱一只，小鸡一文钱3只，
# 要求：公鸡，母鸡，小鸡都要有，把100文钱买100只鸡，买的鸡是整数。多少只公鸡，
# 多少只母鸡多少只小鸡？
# dd算法
# a=0
# b=0
# c=0
# dd=0
# for a in range(1,14):
#     for b in range(1,25):
#         for c in range(3,90):
#             if c%3==0:
#                 if 5*a+3*b+(1/3)*c<=100 and a+b+c==100:
#                     print(a,b,c)
#                     dd+=1
#                 else:pass
#             else:continue
# print(dd)

# 树算法 深度优先
# class Tree :
#     a = 0
#     b = 0
#     c = 0
#     s = 0
#     com=0
#     def ca(self):
#         self.a+=1
#     def da(self):
#         self.a-=1
#     def cb(self):
#         self.b+=1
#     def db(self):
#         self.b-=1
#     def cc(self):
#         self.c+=1
#     def dc(self):
#         self.c-=1
#     def sum(self):
#         self.s=self.a*5+self.b*3+self.c*1/3
#         return self.s
#     def com(self):
#         self.com=self.a+self.b+self.c
#         return self.com
#
# tree=Tree()
# while tree.s<=100 and tree.com<=100:
#     tree.ca()
# else :
#     while tree.s<=100 and tree.com<=100:






# 今有雉（鸡）兔同笼，上有三十五头，下有九十四足。问雉兔各几何
# a=0
# b=0
# for a in range(1,35):
#     for b in range(1,35):
#         if a+b==35 and 2*a+4*b==94:
#             print("鸡有%d只,兔有%d只"%(a,b))
#         else:pass
'''

#复习时敲的代码
#eval函数 会将字符串转换为有效的表达式,并返回计算的结果
# a="1+2"
# print(eval(a))
# a="{'a':1,'b':3}"
# print(eval(a))
# print(type(a))          #并不会改变a的值

a='sddsasdasdCCaAACCdsa1说道说道'
print(a.upper())
# a='ASDCCeee1信息查询'
# print(a.lower())

# a='adsdsdASWQEDD'
# print(a.swapcase())

# a='asds ass Assd wewe wsdW'
# print(a.capitalize())

# a='asds ass Assd wewe wsdW'
# print(a.title())