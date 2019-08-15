#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
匿名函数
概念：指的是一类无需定义标识符的函数或者子程序
优点：没有名字，所以不会引起函数名冲突

语法：
lambda 参数列表: 表达式

1.lambda只是一个表达式，函数体非常简单
2.lambda 匿名函数
参数与参数之间使用逗号隔开，冒号不能省略
3.表达式只能有一条语句，此函数无需return，表达式的结果就是函数的返回值

调用匿名函数：
将lambda表达式赋值给一个变量，通过调用这个变量来进行调用此匿名函数。

匿名函数适用于比较简单一些运算。
'''

'''
需求：设计一个函数，两个数较大的那个
'''

# def func(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
#
# f = lambda a,b: a if a>b else b
# print(f(12,34))

# print(sum([1,2,3,4,5]))
# print(sum(range(1,101)))
'''
1^2+2^2+...+100^2
'''
# print(sum([x*x for x in range(1,101)]))

# print(sum([x**2 for x in range(1,int(input("请输入一个数字")))]))

# print(sum(list(map(lambda x:x**2 ,[x for x in range(1,int(input("请输入一个数字"))+1)]))))

# print(sum({1:2,2:3,3:4}))
#
# print(sum((1,2,4,5)))

# print(sum('1,2,3,4,5'))   #会报错

# z=lambda s:s+1
# y=lambda s:s+z(s)
# print(y(1))