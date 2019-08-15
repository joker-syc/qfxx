#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
list1.append(obj)
功能：将obj追加到列表的末尾

list1.extend(iterable)
功能:将序列打碎插入到list1中

list1.insert(index,object)
功能：在指定的index处插入object，原本位置上元素，向后依次顺延。

list1.pop(index)
功能：将指定下标处的元素删除并且返回，若不指定index，则默认删除最后
一个。

list1.remove(objcet)
功能：将第一个匹配到的object移除。

list1.clear()
功能：清空列表

del list1
功能：删除列表

list1.index(object,start,stop)
功能：在指定的范围内[start,stop)查找指定的object
若找得到则返回第一次匹配的下标值，若找不到则报错
注意：当不指定范围的时候，默认是整个列表。

list1.count(object)
功能：统计obejct在list1中出现的次数


max(list2)
功能：返回列表中最大值

min(list2)
功能：返回列表中最小值

list2.reverse()
功能：将列表倒叙

list2.sort(reverse=True)
功能：对列表中的元素进行排序，默认升序，
若reverse=True，则为降序

'''
import random


'''
需求：去除list1中重复字符
list1 = [1,2,3,1,2,1,2,3,"hah","good",True,False,True,None]
'''
list1 = []
list1.append("hello")
list1.append(True)
print(list1)
list2 = ["good","nice","haha"]
# list1.append(list2)
# print(list1)

list1.extend(list2)
print(list1)
list1.extend("112233")
print(list1)

# list1.insert(0,3)
# print(list1)
print("*"*50)
print(list1.pop(0))
print(list1)

print(list1.remove("1"))
print(list1)

# list1.clear()
# print(list1)

# del list1[0]
# print(list1)

# print(list1.index("0"))
# print(list1.index(True))

print(list1.count("22"))

list2 = list(range(10))
random.shuffle(list2)
print(list2)
print(list2[::-1])
# print(max(list2))
# print(min(list2))
list2.reverse()
print(list2)

list2.sort(reverse=True)
print(list2)
