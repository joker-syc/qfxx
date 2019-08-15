#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
def outer(func):
    def inner(参数列表):
        #添加动态添加的功能
        return func(参数列表)
    return inner

外函数：
1.接收被装饰的函数 func
2.将装饰好的函数返回

内函数：
1.接收被装饰函数的参数
2.添加动态添加的功能
3.执行被装饰的函数，并且将其结果返回

'''



def outerAge(func):
    def inner(age):
        if age>160 or age < 0:
            print("见鬼了...")
        else:
            func(age)
    return inner

@outerAge
def getAge(age):
    print("我今年%d岁"%age)

'''
年龄[0,160]
'''
getAge(200)
getAge(100)
'''
给登录函数添加一个装饰器，实现对用户名以及密码的过滤，要求
用户名的长度5~8，字母数字下划线组成，不能以数字开头，密码6位数字组成
'''
def  isalnum_(str1):
    for x in str1:
        if x.isalnum() or x == "_":
            pass
        else:
            return False
    else:
        return True


def outerlogin(func):
    def inner(user,psd):
        if len(user) >= 5 and len(user) <=8 and isalnum_(user) and (user[0]<"0" or user[0] >"9"):
            if len(psd) == 6 and psd.isdigit():
                return func(user,psd)
        print("用户名或者密码非法")
    return inner


@outerlogin
def login(user,psd):
    if user == "admin" and psd == "123456":
        return True
    else:
        return False

# print(login("1223sf","123344"))
# print(login("a1223sf","123344"))
# print(login("admin","123456"))
print(login("adm&in","123456"))