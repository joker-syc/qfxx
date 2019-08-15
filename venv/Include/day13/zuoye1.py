#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
自己定义一个字典，完成字典相加的功能与相减的功能，
相加：求并集［若key出现重复就覆盖］
相减：求交集
__sub__
'''
class dict():

    def __init__(self,value):
        self.value=value

    def __add__(self, other):
        print(self.value)
        print(other.value)
        self.value.update(other.value)         #字典的update函数是没有返回值的
        return self.value
        # return "dd"

    def __sub__(self, other):
        print(self.value)
        print(other.value)
        c={}
        for a in self.value:
            for b in other.value:
                if a==b:
                    c[a]=other.value[b]
        return c



        return self.value

a=dict({1:2,3:4})
b=dict({1:3,4:5})
c=a+b
print(c)
print()
c=a-b
print(c)