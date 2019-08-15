#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
进程＋协程＋正则
主页： https://sz.lianjia.com/ershoufang
区域：一个区域对应一个进程
分区爬取：拿到页码分页爬取［协程］
将数据写到csv文件中，按区域写［标题与价格］
'''
from gevent import monkey;monkey.patch_all()#导入猴子补丁#可以实现协程的自动切换
import gevent
import multiprocessing
import time
import ssl
import urllib.request
import os
import threading
import re
import csv


def getdata(url):
    context = ssl._create_unverified_context()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    requset = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(requset, context=context)
    data = response.read()

    return data.decode()

def getPageNun(url):
    data=getdata(url)
    # print(data)
    maxPagenun=re.findall('"totalPage"[:](\d*)',data)
    # print(maxPagenun)
    return maxPagenun

def func(url,saveFile):
    if os.path.exists(saveFile):
        pass
    else:
        os.mkdir(saveFile)
    gList=[]
    for a in range(1,int(getPageNun(url)[0])):
        pageURL=url+'/pg'+str(a)
        g = gevent.spawn(save,pageURL,saveFile,a)
        gList.append(g)
    gevent.joinall(gList)

def save(url,saveFlie,nun):
    data=getdata(url)
    with open(file=saveFlie+'/'+str(nun)+'.csv',mode='w',encoding='utf-8') as f:
        message = re.findall(r'</div><div class="price"><span>(.*?)</span>(.*?)</div>.*?data-is_focus=""  data-el="ershoufang">(.*?)</a><div class="info">',data, flags=re.S)
        # print(jggg)
        # f.write(data)
        csv_writer = csv.writer(f)
        for row in message:
            csv_writer.writerow(row)


def areaGet(url):
    data=getdata(url)
    # print(data)
    Area=re.findall(r'区在售二手房 ">(.*?)</a>',data,re.S)
    location=re.findall(r'<a href="/ershoufang/([a-z]*?)/"  title="深圳.*?区在售二手房 ">.*?</a>',data,re.S)
    # location=re.findall(r'<a href="/ershoufang/(.*?)/"  title="深圳.*?区在售二手房 ">.*?</a>',data,re.S)
    # print(Area)
    # print(location)
    #创建多进程
    pList=[]
    z=0
    for saveFile in Area:
        path=url+location[z]
        p = multiprocessing.Process(target=func, args=(path,saveFile))
        p.start()
        pList.append(p)
        z+=1
    for p in pList:
        p.join()



if __name__ == '__main__':
    t1 = time.time()
    path = "https://sz.lianjia.com/ershoufang/"
    if os.path.exists('file'):
        os.chdir("file")
    else:
        os.mkdir("file")
        os.chdir("file")
    areaGet(path)
    print(time.time()-t1)

    # save(path,'dd',1)

