#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-

def func():
    list1 = []
    for x in range(10):
        def inner():
            return x
        list1.append(inner)
    return list1
# l1 = func()
# print(l1)
# for f in l1:
#     print(f())

for i in range(10):
    pass
print(i)
