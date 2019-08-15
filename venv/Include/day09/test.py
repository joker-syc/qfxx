#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc
# def add_(num1,num2):
#     print(num1+num2)
# import functools,operator
# add1=functools.partial(add_,num2=100)
# add1(1)

# 如果要对系统的内置函数
# add2=functools.partial(operator.add,100) #这个100是给a的
# print(add2(10))

# a=1
# def dd():
#     global a
#     a+=1
#     print(a)
#     def dd1():
#         #nonlocal a        #此时nonlocal 就无法访问a的地址(此时如果还要用a,则须用global(相当于解释器分不清global a 与nonlocal a 的区别))
#         a+=1
#         print(a)
#     return dd1()
# dd()

# def func():
#     list1=[]
#     for x in range(10):
#         def inner():
#             return x
#         list1.append(inner)
#     return list1
# print(func())
# list2=func()
# for x in list2:
#     print(x())

# def dd(n):
#     if n==1:
#         return 1
#     else:
#         return dd(n-1)+n
#
# print(dd(998))

# def feibo(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         fei=feibo(n-1)+feibo(n-2)
#         n-=1
#         return fei
# for x in range(10):
#     print(feibo(x))


# a:总人数 b:第一个人的岁数 c:与下一个人相差的岁数
# b=5
# def age (a):
#     if a<=1:
#         return b
#     else:
#         return age(a-1)+2
#
# print(age(5))

# 2.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# def mi(a,b,sun):
#   #初始高度 a
#   #反弹次数 b
#     if b==11:
#         return sun
#     else:
#         b+=1
#         sun+=a+0.5*a
#         return mi(0.5*a,b,sun),0.5*a,b,sun

# def mi(a,b,sun):
#     if b==11:
#         return sun
#     else:
#         b+=1
#         sun+=a+0.5*a
#         return mi(0.5*a,b,sun),0.5*a,b,sun
#
# # print(mi(100,0,0))
# import turtle    #本来想用小海龟模拟的,感觉好麻烦,就算了
# for a in range(11):
#     b=mi(100,0,0)
#     print(b)

# 3.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少
#nun 第十天桃子的数目
# def taozi(nun,day):
#     if day==1:
#         return nun
#     else:
#         day-=1
#         nun=2*(nun+1)
#         return taozi(nun,day)
# print(taozi(1,10))




