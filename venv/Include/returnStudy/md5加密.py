#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
文件注释

'''
import hashlib

# # 待加密信息
# str1 = '1234565678'
# # 创建md5对象
# hl = hashlib.md5()
# #更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
# #md5_obj=hashlib.md5("123456".encode("utf-8")) 效果一样
# hl.update(str1.encode("utf-8"))
# print('MD5加密前为 ：' + str1)
# print('MD5加密后为 ：' + hl.hexdigest())

# print(vars())
class Animal(object):
    pass

class Ani2(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    pass

class Peron(Animal,Ani2):
    pass

per = Peron("lili",19)
print(dir(per))
print(Peron.__name__)
print(Peron.__module__)
print(__name__)

print(Peron.__bases__)
print(per.__dict__)
print(Peron.__dict__)