#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
4.写一个双色球彩票系统，系统可以随机产生一组数据，一组彩票数据有六位数，这六位数的的取值范围是0和1。

一张彩票是两块钱，用户可以选择购买彩票的张数，若余额充足，用户可以开始游戏，要求从控制台输入6位的0或者1

若用户输入的不对，要求用户重新输入，直到输入成功为止。若中奖的话，中奖金额为购买彩票金额的50倍，

若没中奖则打印继续努力！用户可以选择继续买票或者是退出。买票和退出的时候要求打印剩余金额。

余额不足的时候提示用户充值。
'''

import random


print("开始游戏".center(50,"*"))
money = int(input("请输入充值的金额："))
while True:
    count = int(input("请输入购买彩票的张数："))
    if money>= 2*count:
        money -= 2*count
        jiang = ""
        for x in range(6):
            jiang += random.choice(["0","1"])
        print(jiang)
        numlist = []
        for i in range(1,count+1):
            print("请输入第%d张号码："%i)
            while 1:
                number = input("请输入猜测的号码：")
                if len(number) == 6:
                    for n in number:
                        if n in ["0","1"]:
                            pass
                        else:
                            print("号码非法，请重新输入")
                            break
                    else:
                        print("号码合法")
                        break
                else:
                    print("长度非法请重新输入")
            numlist.append(number)
        jiangcount = numlist.count(jiang)
        if jiangcount>0:
            print("恭喜你中大奖了，中奖的金额为%d"%(jiangcount*2*50))
            money += jiangcount*2*50
        else:
            print("很遗憾，没中奖，继续努力！！！")

        print("您当前余额为%d"%money)
        jixu = input("是否继续游戏？ yes/no")
        if jixu == "yes":
            continue
        else:
            print("退出游戏")
            break
    else:
        print("余额不足，当前余额为%d"%money)
        cong = input("是否充值？yes/no")
        if cong == "yes":
            money += int(input("请输入充值的金额："))
            continue
        else:
            print("余额不足退出游戏")
            break

