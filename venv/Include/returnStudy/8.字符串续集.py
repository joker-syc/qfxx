#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
max(str1)
功能：返回str1中ASCII最大的那个
min(str1)
功能：返回str1中ASCII值最小的那个

str1.replace(old,new,count)
参数一：旧字符串
参数二：新字符串
参数三：替换的次数
功能：将str1中指定旧串替换成新串，并且将替换的新的字符串返回。
若指定count则替换count次，若不指定，则默认全部替换。

字符串的映射替换
1.生成一个映射表
table = str3.maketrans("god","123")
2.根据映射表进行替换
str1.translate(table)

str1.startswith(sub)
功能：判断str1是否以sub开头

str1.endswith(sub)
功能：判断str1是否以sub结束

str1.encode("utf-8")
功能：将普通字符串转为二进制字符串
utf-8：编码格式
注意：编码与解码使用相同的编码格式

bstr.decode("utf-8")
功能：将二进制字符串转为普通字符串

str1.isalpha()
功能：判断str1中的字符是否为为字母，若是则返回True，否则返回False
注意：中文没有考虑【若出现中文也为True】

str1.isalnum()
功能：判断str1中的字符是否为为字母或者数字，若是则返回True，否则返回False
注意：中文没有考虑【若出现中文也为True】

str1.isupper()
功能：判断str1中的所有字符是否全部都大写，若是则返回True，否则返回False

str1.islower()
功能：判断str1中的所有字符是否全部都小写，若是则返回True，否则返回False

str1.istitle()
功能：判断str1是否为标题化的字符串，若是返回True，否则返回False

str1.isspace()
功能：判断str1是否只包含空白符，若是则返回True，否则返回False

ord(char)
功能：返回char的ASCII码值

chr(code)
功能：返回code对应的ASCII的字符
'''
# print("".isspace())
# print(" ".isspace())
# print("\n".isspace())
# print("\r".isspace())
# print("\f".isspace())
# print("\t".isspace())
print(ord('A'))
print(chr(65))


str4 = 'hello中国'
str5 = 'Hello World'
str6 = 'Hello2World'
str7 = 'GOO D'
# print(str4.isalpha())
# print(str5.isalpha())
# print(str6.isalpha())

# print(str4.isalnum())
# print(str5.isalnum())
# print(str6.isalnum())
#
# print(str4.istitle())
# print(str5.istitle())
# print(str6.istitle())
# print(str7.istitle())

# print(str4.islower())
# print(str5.islower())
# print(str6.islower())
# print(str7.islower())

# print(str4.isupper())
# print(str5.isupper())
# print(str6.isupper())
# print(str7.isupper())

# str1 = "hello world, hello"
# str2 = str1.replace("hello","hi",1)
# print(str2)
#
# str3 = "good"
# table = str3.maketrans("god","123")
# print(str1.translate(table))
#
# phonenum = "12478880233"
# print(phonenum.startswith("123"))
# print(phonenum.startswith("124"))
# print(phonenum.endswith("244"))
# print(phonenum.endswith("233"))
#
# print(phonenum.encode("utf-8"))
# bstr = "你好啊".encode("utf-8")
# print(bstr)
# print(bstr.decode("utf-8"))

