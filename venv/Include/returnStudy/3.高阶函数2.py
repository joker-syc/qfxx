#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
filter(fuc，iter)
参数一：函数 有且只有一个参数
参数二：可迭代对象
功能：将可迭代对象中的元素依次取出，并且作用于fuc函数，根据fuc返回的结果
决定是否保留该元素，返回真保留，返回假不保留,结果作为迭代器返回。

filter(None,iter)
过滤迭代器中为假的元素。

sorted(iter1,key,reverse)
 参数一：可迭代对象
 参数二：key，决定比较结果
 参数三：是否降序，默认升序［默认False］
'''
list1 = [1,2,3,12,34,21,23,12,3]
print(list(filter(lambda x: True if x%2 else False,list1)))


data = [["jerry",28,"吃"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]

print(list(filter(lambda x: False if x[-1]=="无" else True,data)))

list1 = [13,445,6,65,'887','234',34,'3455','234']

print(list(sorted(list1,key=int)))
list1.sort(key=lambda x:int(x)%10)
print(list1)

print(list(sorted(data,key=lambda x:x[1],reverse=True)))