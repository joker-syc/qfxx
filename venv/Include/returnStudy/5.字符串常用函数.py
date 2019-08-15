#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
eval(str1)
功能:将字符串转为有效的表达式并且将表达式的结果返回
str(obj)
功能：将其它类型的转为字符串

string.lower()
功能：将大写字母转为小写字母

string.upper()
功能：将小写转为大写字母

string.swapcase()
功能：将大写字母转为小写，将小写字母转为大写

string.title()
功能：将每个单词的首字母大写【标题化的字符串】

string.capitalize()
功能：将开头的首字母大写，其他都小写

string.center(width,fillchar)
功能：返回一个以指定字符串居中长度width使用fillchar来进行填充的字符串

string.ljust(width,fillchar)
功能：返回一个以指定字符串居左长度width使用fillchar来进行填充的字符串

string.rjust(width,fillchar)
功能：返回一个以指定字符串居右长度width使用fillchar来进行填充的字符串

string.zfill(width)
功能：返回一个以指定字符串居右长度width使用0来进行填充的字符串


string.count(x,start,end)
功能：统计x在string中出现的次数，若不指定start与end，默认统计整个字符串
若指定start与end则取值范围[start,end)


string.find(sub,start,end)
功能：从左往右在string中查找sub，若找得到则返回第一个匹配的下标值，若找不到
则返回-1.
若不指定start与end则默认查找整个字符串，若指定start与end则查询范围
为[start,end)


string.rfind(sub,start,end)
功能：从右往左在string中查找sub，若找得到则返回第一个匹配的下标值，若找不到
则返回-1.
若不指定start与end则默认查找整个字符串，若指定start与end则查询范围
为[start,end)


string.index(sub,start,end)
功能：从左往右在string中查找sub，若找得到则返回第一个匹配的下标值，若找不到
则报错.
若不指定start与end则默认查找整个字符串，若指定start与end则查询范围
为[start,end)

string.rindex(sub,start,end)
功能：从右往左在string中查找sub，若找得到则返回第一个匹配的下标值，若找不到
则报错.
若不指定start与end则默认查找整个字符串，若指定start与end则查询范围
为[start,end)

string.lstrip(chars)
功能：去掉sting左边指定的chars。若不指定chars，则默认去除空白符
空白符：【 \t\r\n\f】

string.rstrip(chars)
功能：去掉sting右边指定的chars。若不指定chars，则默认去除空白符
空白符：【 \t\r\n\f】

string.strip(chars)
功能：去掉sting左右两边指定的chars。若不指定chars，则默认去除空白符
空白符：【 \t\r\n\f】


string.split(seq,maxsplit)
功能：从左往右以指定的seq对string进行切片，并且将切片后的结果以列表的形式返回。
若不指定seq默认情况下使用空白符来进行切片
若不指定maxsplit则默认全部切片，若指定则切指定的次数


string.rsplit(seq,maxsplit)
功能：从右往左以指定的seq对string进行切片，并且将切片后的结果以列表的形式返回。
若不指定seq默认情况下使用空白符来进行切片
若不指定maxsplit则默认全部切片，若指定则切指定的次数

string.splitlines(keepends=True)
功能：对string按行进行切片，切片的结果以列表返回，keepends默认为False
不保留换行符，当keepends为True的时候保留换行符
'''
path = "/Users/zhangjiao/PycharmProjects/szpython1905/day04/1.作业.py"
# l1 = eval("(1,2,3,4)")
# print(l1)
# print(type(l1))
string = "You Are\n very\n good！！！"
string3 = "You Are very good！！！"
string2 = "*******You Are **very** good！！！**********"

# print(string2.lstrip("*"))
# print(string2.rstrip("*"))
# print(string2.strip("*"))
# print(string2.lstrip("*").rstrip("*"))
# print(string2.split("*"))
# print(string.split(maxsplit=10))
# print(string.rsplit(maxsplit=2))
print(string.splitlines(keepends=True))
# print(string.count("o",0,14))

# print(string.find("o",3,14))
# print(string.index("o",3,14))
# print(string.rfind("o",3,14))
# print(string.rindex("o",3,14))

# print(string.center(50,"&"))
# print(string.ljust(50,"&"))
# print(string.rjust(50,"&"))
# print(string.zfill(50))

# print(string.lower())
# print(string.upper())
# print(string.swapcase())
# print(string.title())
# print(string.capitalize())
