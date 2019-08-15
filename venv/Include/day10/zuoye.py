#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
1.给歌词解析器添加音乐
2.写一个音乐播放器
'''
import pygame
import os
import time
musicDir=r'D:\CloudMusic'
musicList=[]
nowMusic=''
value=0.5
def getMusic():
    if not os.path.exists(musicDir):
        print("指定播放目录不存在")
    else:
        musicName=os.listdir(musicDir)
        for a in musicName:
            musicAddress=os.path.join(musicDir,a)
            musicList.append(musicAddress)
        # print(musicList)
def playMusic(music):
    mm = pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(value)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

def stopMusic():
    pygame.mixer.music.stop()

# def backplay():


def nextMusic():
    global nowMusic
    if musicList.index(nowMusic)==len(musicList)-1:
        nowMusic=musicList[0]
        playMusic(nowMusic)
    else:
        nowMusic=musicList[musicList.index(nowMusic)+1]
        playMusic(nowMusic)

def lastMusic():
    global nowMusic
    if musicList.index(nowMusic)==0:
        nowMusic=musicList[-1]
        playMusic(nowMusic)
    else:
        nowMusic=musicList[musicList.index(nowMusic)-1]
        playMusic(nowMusic)

def increase():
    global value
    try:
        value+=0.1
        pygame.mixer.music.set_volume(value)
    except:
        print("已到达最大音量")

def reduce():
    global value
    try:
        value-=0.1
        pygame.mixer.music.set_volume(value)
    except:
        print("已到达最小音量")

def welcome():
    print('''
    *************************
    * 欢迎来到酷我音乐播放器 *
    *************************
    ''')
    pygame.mixer.init()

def select():
    print('''
    **************************
    * 1.播放       2.停止     *
    * 3.下一曲     4.上一曲   *
    * 5.增大音量   6.减少音量 *
    *      0.退出             *
    ***************************
    ''')
    return input("请选择您要操作的选项：")

def center():
    global nowMusic
    nowMusic=musicList[0]
    welcome()
    while 1:
        a=select()
        if a=='0':
            return 0
        elif a=='1':
            playMusic(nowMusic)
            continue
        elif a=='2':
            stopMusic()
            continue
        elif a=='3':
            nextMusic()
            continue
        elif a=='4':
            lastMusic()
            continue
        elif a=='5':
            increase()
            continue
        elif a=="6":
            reduce()
            continue

if __name__=="__main__":
    getMusic()
    center()
    # 此时创建的是一个守护线程:会随着主线程的结束而结束
    # 主线程执行的速度非常快，主线程执行结束，就直接退出了，因此我们的子线程根本不会被创建
    # 多线程必须要在程序还处于"活"的状态时才能执行,这就是while 1 的作用,让程序不停下来,停留在cpu中.
    # try:
        # _thread.start_new_thread(manyThread,('thread1',))   #似乎这里当子线程执行这个后,主线程就去下一行了(子线程访问后,主线程就不管了),使得主线程过早结束,子线程还没发挥作用就被销毁了
        # time.sleep(10)
        # _thread.start_new_thread(manyThread,('thread2',))
        # time.sleep(100)
    # except:
    #     print("实验多线程失败")

    # while 1:
    #     pass


