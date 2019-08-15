#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 0023 17:17
# @Author  : joker-syc
# @Site    : 
# @File    : zuoye.py
# @Software: PyCharm

'''
将音乐播放器改写为面向对象
'''
#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
1.给歌词解析器添加音乐
2.写一个音乐播放器

'''
# import pygame
# import os
# import time
# import _thread
# class songPlay:
#     musicDir=r'D:\CloudMusic'
#     musicList=[]
#     nowMusic=''
#     value=0.5
#     def getMusic(self):
#         if not os.path.exists(self.musicDir):
#             print("指定播放目录不存在")
#         else:
#             musicName=os.listdir(self.musicDir)
#             for a in musicName:
#                 musicAddress=os.path.join(self.musicDir,a)
#                 self.musicList.append(musicAddress)
#             # print(musicList)
#     def playMusic(self,music):
#         mm = pygame.mixer.music.load(music)
#         pygame.mixer.music.set_volume(self.value)
#         pygame.mixer.music.play()
#         pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
#
#     def stopMusic(self):
#         pygame.mixer.music.stop()
#
#     # def backplay():
#
#
#     def nextMusic(self):
#         if self.musicList.index(self.nowMusic)==len(self.musicList)-1:
#             self.nowMusic=self.musicList[0]
#             self.playMusic(nowMusic)
#         else:
#             self.nowMusic=self.musicList[self.musicList.index(self.nowMusic)+1]
#             self.playMusic(self.nowMusic)
#
#     def lastMusic(self):
#         if self.musicList.index(self.nowMusic)==0:
#             self.nowMusic=self.musicList[-1]
#             self.playMusic(self.nowMusic)
#         else:
#             self.nowMusic=self.musicList[self.musicList.index(self.nowMusic)-1]
#             self.playMusic(self.nowMusic)
#
#     def increase(self):
#         try:
#             self.value+=0.1
#             pygame.mixer.music.set_volume(self.value)
#         except:
#             print("已到达最大音量")
#
#     def reduce(self):
#         try:
#             self.value-=0.1
#             pygame.mixer.music.set_volume(self.value)
#         except:
#             print("已到达最小音量")
#
#     @staticmethod
#     def welcome():
#         print('''
#         *************************
#         * 欢迎来到酷我音乐播放器 *
#         *************************
#         ''')
#         pygame.mixer.init()
#
#     @staticmethod
#     def select():
#         print('''
#         **************************
#         * 1.播放       2.停止     *
#         * 3.下一曲     4.上一曲   *
#         * 5.增大音量   6.减少音量 *
#         *      0.退出             *
#         ***************************
#         ''')
#         return input("请选择您要操作的选项：")
#
#     def center(self):
#         self.nowMusic=self.musicList[0]
#         songPlay.welcome()
#         while 1:
#             a=songPlay.select()
#             if a=='0':
#                 return 0
#             elif a=='1':
#                 self.playMusic(self.nowMusic)
#                 continue
#             elif a=='2':
#                 self.stopMusic()
#                 continue
#             elif a=='3':
#                 self.nextMusic()
#                 continue
#             elif a=='4':
#                 self.lastMusic()
#                 continue
#             elif a=='5':
#                 self.increase()
#                 continue
#             elif a=="6":
#                 self.reduce()
#                 continue
#
#     @staticmethod
#     def manyThread(threadName):
#         print(threadName+"\n")
#         center()
# if __name__=="__main__":
#     playsong=songPlay()
#     playsong.getMusic()
#     playsong.center()
#     # 此时创建的是一个守护线程:会随着主线程的结束而结束
#     # 主线程执行的速度非常快，主线程执行结束，就直接退出了，因此我们的子线程根本不会被创建
#     # 多线程必须要在程序还处于"活"的状态时才能执行,这就是while 1 的作用,让程序不停下来,停留在cpu中.
#     # try:
#         # _thread.start_new_thread(manyThread,('thread1',))   #似乎这里当子线程执行这个后,主线程就去下一行了(子线程访问后,主线程就不管了),使得主线程过早结束,子线程还没发挥作用就被销毁了
#         # time.sleep(10)
#         # _thread.start_new_thread(manyThread,('thread2',))
#         # time.sleep(100)
#     # except:
#     #     print("实验多线程失败")
#
#     # while 1:
#     #     pass

'''
ATM系统
卡：卡号，密码，金额，锁
用户：name，iscard，phonenum，card
ATM系统：
属性：用户列表  登录状态
行为： 1.登陆   2.开户     3.查询   4.取款     5.存款   0.退出
6.转账   7.改密     8.锁卡   9.解锁

使用json进行持久化处理
'''
import random
import json

#用户的一切操作都需要通过ATM类
class ATM:
    # userMessage={}             #key: name='' value: [phonenum=''，cardId=[]]
    # cardMessage={}             #key: carId='' value: [password='',money=0,freeze=True,userName='']

    nowUser=''                 #当前系统用户
    nowCard=''
    lock=[False,3]

    def __init__(self):
        ATM.nowUser=''
        ATM.nowCard = ''
        Card.nowCardId=''
        ATM.lock=[False,3]

    def login(self):
        cardId = input("请输入你的卡号\n")
        if Card.isExist(cardId) and Card.ifLock(cardId):
            if Card.isRight(cardId):
                ATM.nowUser=Card.cardMessage[cardId][-1]
                ATM.nowCard=cardId
                Card.nowCardId=cardId
                print('你已经成功登入ATM')
            else:
                if ATM.lock[1]<=0:
                    ATM.lock[1]-=1
                    print('密码错误,当前可继续输入密码次数为%d'%self.lock[1])
                    self.login()
                else:
                    Card.cardMessage[cardId][-2]=False
                    print('此卡已冻结')
        else:
            print('卡号不存在')

    def loginOut(self):
        print(ATM.nowCard)
        print(ATM.nowUser)
        print(Card.nowCardId)
        print(Card.cardMessage)
        print(Men.userMessage)
        ATM.nowUser = ''
        ATM.nowCard = ''
        Card.nowCardId = ''
        ATM.lock = [False, 3]
        try:
            with open('cardMessage.txt', 'a+', encoding='GBK') as card:
                json.dump(Card.cardMessage,card,ensure_ascii=False)
            with open('userMessage.txt', 'a+', encoding='GBK') as user:
                json.dump(Men.userMessage,user,ensure_ascii=False)
        except:
            print("持久化失败")
        print("结束")

    def creatNewUser(self):
        userName=input("请输入新开户的用户名\n")
        if Men.ifNewUser(userName):
            phoneNumber=input("请输入电话号码\n")
            men=Men()
            men.addUser(userName,phoneNumber)
        else:
            print("用户名重复,请重新输入")
            self.creatNewUser()

    def selectUser(self):
        print(Men.select(ATM.nowUser))

    def getMoney(self):
        money=int(input("请输入取钱数\n"))
        if money>Card.cardMessage[ATM.nowCard][1]:
            print("取的数目大于当前用户的存款金额,请重新输入")
            self.getMoney()
        else:
            card=Card()
            card.getMoney(money)

    def inMoney(self):
        money=int(input("请输入存钱数\n"))
        card=Card()
        card.inMoney(money)

    def Transfer_accounts(self):
        cardId=input("请输入转账的账户\n")
        if cardId in Card.cardMessage:
            money=int(input('请输入转账的钱数\n'))
            if money<Card.cardMessage[ATM.nowCard][1]:
                card=Card.Transfer_accounts(money,cardId)
            else:
                print("当前账户的余额不足\n")
        else:
            print('不存在此卡号,请重新输入')
            self.Transfer_accounts()

    def changePasswd(self):
        if ATM.nowUser=='' and ATM.nowCard=='':
            print('当前未登录')
        else:
            card=Card()
            card.changePasswd()

    def lockCard(self):
        if ATM.nowUser == '' and ATM.nowCard == '':
            print('当前未登录')
        else:
            card=Card()
            card.lockCard()

    def unlock(self):
        if ATM.nowUser == '' and ATM.nowCard == '':
            print('当前未登录')
        else:
            card=Card()
            card.unlockCard()

    @staticmethod
    def welcome():
        print('''
           **********************
           *                    *
           *  welcome to bank   *
           *                    *
           **********************
           ''')

    @staticmethod
    def select():
        print('''
           **********************
           *  1.登陆   2.开户    *
           *  3.查询   4.取款    *
           *  5.存款   0.退出    *
           *  6.转账   7.改密    *
           *  8.锁卡   9.解锁    *
           **********************
           ''')
        num = input("请选择服务项目：")
        return num

#生成新的卡号    查询卡号是否存在
class Card:
    # cardMessage = {'123':['123',10,True,'沙雕']}  # key: carId='' value: [password='',money=0,freeze=True,userName='']
    cardMessage={}
    nowCardId=''
    addNewUser=''

    #申请新卡之前,必须有账户,userName
    # def creat(self,userName):
    #     newCard=self.creatNewCard()
    #     print("你的卡号为%S,请牢记"%newCard)
    #     self.cardMessage[newCard]=[self.setPasswd(),0,True,userName]
    #     return newCard

    def addCard(self):
        newCard=self.creatNewCard()
        print("你的卡号为%s,请牢记" % newCard)
        Card.cardMessage[newCard] = [self.setPasswd(), 0, True,self.addNewUser ]
        print(Card.cardMessage)
        return newCard


    def creatNewCard(self):
        newCard = ''
        for a in range(6):
            newCard += str(random.randint(1, 6))
        if self.isExist(newCard):
            self.creatNewCard()
        else:
            return newCard

    @classmethod
    def isExist(cla,cardId):
        if cardId in Card.cardMessage:
            return True
        else:
            return False

    @classmethod
    def isRight(cla,cardId):
        if input("请输入该卡的密码\n")==cla.cardMessage[cardId][0]:
            return True
        else:
            return False

    def setPasswd(self,*args):
        if args==():
            passwd=input("请输入密码\n")
            return passwd
        else:
            passwd = input("请输入重置的密码\n")
            Card.cardMessage[Card.nowCardId][0]=passwd

    def changePasswd(self):
        self.setPasswd(Card.nowCardId)

    @classmethod
    def ifLock(self,cardId):
        if Card.cardMessage[cardId][-2]:
            return True
        else:
            return False

    def lockCard(self):
        # if Card.cardMessage[cardId][-2]:
            Card.cardMessage[Card.nowCardId][-2]=False
            print("冻结成功\n")
        # else:
        #     print("该卡已冻结\n")

    def unlockCard(self):
        # if Card.cardMessage[cardId][-2]:
        #     print("该卡已解冻,无需再解冻\n")
        # else:
            Card.cardMessage[Card.nowCardId][-2]=True
            print("解冻成功\n")

    def getMoney(self,money):
        Card.cardMessage[Card.nowCardId][1]-=money
        print('取款成功')

    def inMoney(self,money):
        Card.cardMessage[Card.nowCardId][1]+=money
        print('存款成功')

    def Transfer_accounts(self,money,card2):
        #转账功能实现
        try:
            Card.cardMessage[Card.nowCardId][1]-=money
            Card.cardMessage[card2][1]+=money
            print("转账成功")
        except:
            print("转账失败")

class Men:
    # userMessage = {'沙雕': ["1", "123"]}  # key: name='' value: [phonenum=''，cardId=[]]
    userMessage = {}

    def addUser(self,newUserName,phonenum):
        card=Card()
        Card.addNewUser=newUserName
        Men.userMessage[newUserName]=[phonenum,card.addCard()]

    @classmethod
    def select(self,nowUserName):
        return Men.userMessage[nowUserName]

    @classmethod
    def ifNewUser(cla,userName):
        if userName in cla.userMessage:
            return False
        else:
            return True



if __name__ == '__main__':
    ATM.welcome()
    atm=ATM()
    #dumps和loads是在内存中转换（python对象和json字符串之间的转换），而dump和load则是对应于文件的处理。
    try:
        with open(file=r'C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day12\cardMessage.txt',mode='r',encoding='GBK') as card:
            # print(card)
            # print(type(card.read()))
            # print(type(card))
            cardmessage=card.read()
            cardmessage.replace("'",'''"''')
            print(cardmessage)
            Card.cardMessage=json.loads(cardmessage)
            print(Card.cardMessage)
        with open(file=r'C:\Users\Administrator\PycharmProjects\workhard\venv\Include\day12\userMessage.txt',mode='r',encoding='GBK') as user:
            usermessage=user.read()
            usermessage.replace("'",'''"''')
            print(usermessage)
            Men.userMessage=json.loads(usermessage)
            print(Men.userMessage)
    except:
        print("读取文件错误")
    while 1:
        nun=ATM.select()
        if nun=='1':
            atm.login()
        elif nun=='2':
            atm.creatNewUser()
        elif nun=='3':
            atm.selectUser()
        elif nun=='4':
            atm.getMoney()
        elif nun=='5':
            atm.inMoney()
        elif nun=='0':
            atm.loginOut()
        elif nun=='6':
            atm.Transfer_accounts()
        elif nun=='7':
            atm.changePasswd()
        elif nun=='8':
            atm.lockCard()
        elif nun=='9':
            atm.unlock()
        else:
            print("无效操作")





