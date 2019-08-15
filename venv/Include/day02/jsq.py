#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc


# a=int(input("请输入你的工资:"))
# h=int(input("请输入公积金:"))
# k=int(input("请输入起征额"))
# if a<=k :
#     print("无须缴纳个人所得税")
# elif a<=1500:
#     print("须缴纳个人所得税额为%d"%((a-h-k)*0.03))
# elif a<=4500:
#     print("须缴纳个人所得税额为%d" % ((a - h - k) * 0.1-105))
# elif a<=9000:
#     print("须缴纳个人所得税额为%d" % ((a - h - k) * 0.2-555))
# elif a<=35000:
#     print("须缴纳个人所得税额为%d" % ((a - h - k) * 0.25-1005))
# elif a<=55000:
#     print("须缴纳个人所得税额为%d" % ((a - h - k) * 0.3-2755))
# elif a<=80000:
#     print("须缴纳个人所得税额为%d"%((a-h-k)*0.35-5505))
# else:
#     print("须缴纳个人所得税额为%d" % ((a - h - k) * 0.4-13505))


# b=int(input("请输入年份:"))
# if b%400==0 or (b%100!=0 and b%4==0):
#     print("%d是闰年"%(b))
# else:print("%d不是闰年"%(b))


# c=int(input("请输入一个数字:"))
# if c<1000 and int(c/100)**3+int((c%100)/10)**3+(c%10)**3==c:
#     print("%d是一个水仙花数"%(c))
# else:print("%d不是一个水仙花数"%(c))


# d=int(input("请输入一个数字:"))
# if d<100000 and int(d/10000)==d%10 and int((d%10000)/1000)==int((d%100)/10):
#     print("%d是一个回文数"%(d))
# else:print("%d不是一个回文数"%(d))

import random
while 1:
    e=input("请选择压大还是小:")
    gg=random.randint(1,6)
    print(gg)
    zz=""
    if gg<=3:
        zz="小"
    else:zz="大"
    if e==zz:
        print("庄家喝酒")
    else:print("先干为敬")
    print("是否继续?")
    if input("Y//N")=="Y":
        pass
    else: break
print("再见")