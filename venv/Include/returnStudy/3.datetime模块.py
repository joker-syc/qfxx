#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
from datetime import datetime
'''
datetime.now()
功能：获取当前时间

datetime(year,mon,day,hour,min,sec)
功能：返回指定的时间

dt.strftime(format)
功能：将datetime对象转为指定的时间格式
timedelta = datetime1 - datetime2
功能：两个datetime相减得到一个时间间隔对象。
通过时间间隔对象可以获取间隔的天数.days
以及除间隔天数之外剩余的秒数  .seconds
'''
'''
认识多少天？输入认识的时间，写成函数的形式
如果一小时以内，显示一个小时以内
如果是一天以内，显示一天以内
若七天以内，显示一个星期以内
若超过了七天，就显示具体的秒数
'''
dt = datetime.now()
# print(dt)
# print(type(dt))
# strdt = str(dt)
# print(type(strdt))
# print(strdt)

dt2 = datetime(2019,7,8,9,0,0)
print(dt2)

# strf = dt.strftime("%x %X")
# print(strf)
dd = dt - dt2
print(dd)
print(type(dd))
print(dd.days)
print(dd.seconds)