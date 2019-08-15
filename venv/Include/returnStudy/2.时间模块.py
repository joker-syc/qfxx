#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
时间戳：1970年1月1日午夜到现在所有的时间换算秒表示
UTC：格林尼治时间，国际标准时间，在中国时间 UTC＋8
DST：夏令时

year:年
mon：月
mday：日
hour：时
min ：分
sec ：秒
wday：星期码 0～6 周一～周日
yday：本年过了的天数
isdst：是否是夏令时
'''
import time

'''
time.time():
功能：获取时间戳
time.gmtime(sec)
功能：将时间戳转为时间元组utc时间
time.localtime(sec)
功能：将时间戳转为时间元组当地时间

time.ctime(sec)
功能：将指定的时间戳转为时间字符串，若时间戳没给，则默认为当前时间

time.asctime(tuple)
功能：将时间元组转为时间字符串

time.strftime(format,t)
功能：将时间元组格式化成指定的时间字符串

time.strptime(strt,format)
功能：将时间字符串使用指定的格式转为时间元组

time.mktime(strp)
功能：将时间元组转为时间戳

time.sleep(sec)
功能：休眠

time.clock()
功能：以浮点数的形式计算的秒数返回当前的cpu执行的时间

时间戳 －》 转为时间元组 －》转为时间字符串 －》转为时间元组 －》时间戳
'''
time.clock()
t1 = time.time()
print(t1)
# print(60*365*24*60*60)
gt = time.gmtime(t1)
print(gt)

lt = time.localtime(t1)
print(lt)

ct = time.ctime(t1)
print(ct)

asct = time.asctime(lt)
print(asct)

strft = time.strftime("%Y/%m/%d %H:%M:%S",lt)
strft2 = time.strftime("%x %X",lt)
print(strft)
print(strft2)

strp = time.strptime(strft,"%Y/%m/%d %H:%M:%S")
print(strp)
t2 = time.mktime(strp)
print(t2)

# time.sleep()
print(time.clock())















