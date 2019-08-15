#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
字典的遍历：
若直接使用for循环遍历字典，默认遍历key值

字典名.values() 获取所有的value值
字典名.keys() 获取所有的key
字典名.items() 获取字典的key与value
'''
d1 = {"haha":123,"heihie":234,"hehe":444,"wuwu":5555}
for x in d1:
    print(x)

for v in d1.values():
    print(v)

print(type(d1.values()))

for k,v in d1.items():
    print(k,v)

for k in d1.keys():
    print(k)