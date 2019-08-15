#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
map(fuc,iter1)
fuc函数:有且只有一个参数，并且此函数有返回值。
iter1:可迭代对象
功能：将可迭代对象中的元素依次取出，作用于func函数，
并且将作用的结果以迭代器的方式返回

reduce(fuc,iter1)
参数一：函数，有且只有两个参数
参数二：可迭代对象
功能：将可迭代对象中的元素依次取出，并作用fuc函数，把作用的结果作为下一次的参数
继续运算。
'''
from functools import reduce
from operator import add

print(reduce(lambda x,y:x+y,range(1,10001)))
print(reduce(lambda x,y:x*y,range(1,5)))
# print(reduce(lambda x,y:x*y,range(1,6)))
# print(reduce(lambda x,y:x*y,range(1,7)))


list1 = [13,445,6,65,'887','234',34,'3455','234']

print(reduce(add,map(int,list1)))

def func(l):
    l1 = []
    for x in l:
        l1.append(int(x))
    return l1

# print(func(list1))
print(list(map(int,list1)))
print(list(map(str,list1)))

'''
使用map函数，求n的序列[1,4,9,..,n^2]
'''
print(list(map(lambda x:x*x,range(1,101))))

