#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-

'''
1.同桌找了一个女朋友跟你炫耀
同桌类：
特征：name，sex，age，女朋友
行为：炫耀
女朋友类
特征：name，sex，age，facevalue
行为：做饭  卖萌  敲代码
'''
class classMate():
    def __init__(self,name,sex,age,hobby):
        self.name=name
        self.sex=sex
        self.age=age
        self.hobby=hobby

    def haveGirlFriend(self):
        self.girlFriend=girlFriend("二丫","女",18,60,'做饭  卖萌  敲代码')
        print("我有一个叫%s的女朋友,%d岁,颜值%d,喜欢%s"%(self.girlFriend.name,self.girlFriend.age,self.girlFriend.faceValue,self.girlFriend.hobby))

    def selfIntroduction(self):
        print("我是%s,%s岁,喜欢%s"%(self.name,self.age,self.hobby))

    def letGirlIntroduction(self):
        self.girlFriend.selfIntroduction()

class girlFriend():
    def __init__(self,name,sex,age,faceValue,hobby):
        self.name=name
        self.sex=sex
        self.age=age
        self.faceValue=faceValue
        self.hobby=hobby
    def selfIntroduction(self):
        print("我是%s,%s岁,喜欢%s"%(self.name,self.age,self.hobby))

classmate=classMate("二蛋",'男',20,"炫耀")
classmate.selfIntroduction()
classmate.haveGirlFriend()
classmate.letGirlIntroduction()

'''

2.人开枪射击子弹
人：
特征：name  枪
行为：射击  装子弹
枪：
特征：型号  射击范围  弹夹
行为：砰 开枪  上膛

弹夹：
特征：子弹个数
行为： 加弹  减弹
'''
class man():
    def __init__(self,name):
        self.name=name
        self.guns=gun()

    def shoot(self):
        if self.guns.clips.nun>=0:
            self.guns.loaded()
            self.guns.shooting()
        else:
            print("需要装子弹")
            self.loading()

    def loadingAll(self):
        print("正在换弹夹")
        self.guns.clips.__init__()

    def loadingOne(self):
        print("正在给弹夹上一颗子弹")
        self.guns.clips.addc()

class gun():
    def __init__(self):
        self.clips=clip()

    def  loaded(self):
        print("上膛中")
        print('预备')

    def shooting(self):
        print("砰")
        self.clips.reducec()


class clip():
    def __init__(self):
        self.nun=7

    def addc(self):
        if self.nun==7:
            print("弹夹已满")
        else:
            self.nun+=1
            print("正在加弹")

    def reducec(self):
        if self.nun==0:
            print("弹夹已空")
        else:
            self.nun-=1
            print("正在减弹")



if __name__=="__main__":
    man1=man(input("我是:"))
    while 1:
        a=int(input("你手里有一把枪,请选择操作:\n"+
                "1:开枪   2:换弹夹  3:给弹夹上一颗子弹\n"+
                "4:退出射击\n"))
        if a==1:
            man1.shoot()
        elif a==2:
            man1.loadingAll()
        elif a==3:
            man1.loadingOne()
        elif a==4:
            break
        print("你现在枪里还有%d颗子弹"%man1.guns.clips.nun)
    print("欢迎再来")



