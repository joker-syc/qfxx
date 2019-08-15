#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''

'''

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # def __repr__(self):
    #     return "%s-%d"%(self.name,self.age)

    # __str__ = __repr__

    def __add__(self, other):
        return Person(self.name+other.name,self.age+other.age)


if __name__ == '__main__':
    per1 = Person("lili",19)
    per2 = Person("yiyi",19)
    per3 = Person("yiyi",19)
    print(per1+per2+per3)
    # dict1 = {1:"1",2:"2",3:"3"}
    # dict2 = {1:"1",2:"2",3:"3"}
    # print(dict1-dict2)



