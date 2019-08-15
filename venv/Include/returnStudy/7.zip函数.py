#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
zip函数
打包函数

zip(iter1,iter2)
功能：将iter1与iter2对应位置上的元素进行打包，以迭代器方式返回
长度与最短的那个相同

zip(*zipobj)
功能：将zip对象进行解包
'''
list1 = [1,2,3,4]
list2 = ["1","2","3","4","5"]

zipobj = zip(list1,list2)
print(list(zipobj))

print(list(zip(*zipobj)))

dict1 = {1:"hello",2:"good",3:"nice"}
# dict2 = {"hello":1,"good":2,"nice":3}
dict3 = {"hello":3,"good":2,"nice":1}

# dict1.keys()
#
# dict1.values()

print(dict(zip(dict1.values(),list(dict1.keys())[::-1])))

print(dict(zip(dict1.values(),dict1)))




