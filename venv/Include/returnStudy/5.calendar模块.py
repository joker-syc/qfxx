#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import calendar

'''
calendar.month(year,mon)
功能：返回月日历
calendar.calendar(year)
功能：返回年日历

calendar.isleap(year)
功能：判断某年是否为闰年，闰年返回True，平年返回False

calendar.leapdays(year1,year2)
功能：返回［year1，year2）之间闰年的个数


calendar.monthrange(year,mon)
功能：返回本月第一天的星期码与本月的天数


calendar.monthcalendar(year,mon)
返回以每周每天为元素的序列

calendar.weekday(year,mon,day)
功能：返回指定日期的星期码
'''
print(calendar.month(2019,7))
print(calendar.month(2019,8))
# print(calendar.calendar(2020))
print(calendar.isleap(200))
print(calendar.leapdays(2000, 2019))

print(calendar.monthrange(2019,7))
print(calendar.monthrange(2019,8))

print(calendar.monthcalendar(2019,7))
print(calendar.weekday(2019,7,22))