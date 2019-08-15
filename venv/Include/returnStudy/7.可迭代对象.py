#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
能够直接作用于for循环的对象我们称之为可迭代对象
常见的可迭代对象：
集合类型：list，tuple，dict，set，str，range
生成器：在Python中可以一边循环一边计算的这种机制我们称之为生成器。
注意：使用生成器的时候，只能遍历一次。
'''
l1 = [x for x in range(1,11)]
g1 = (x for x in range(1,11))
print(g1)
print(l1)
for i in g1:
    print(i)
for i in g1:
    print(i)
