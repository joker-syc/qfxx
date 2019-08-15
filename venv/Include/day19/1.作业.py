#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
'''
使用多线程爬取链家
https://sz.lianjia.com/zufang/
使用正则将区域提取出来
分区爬取，并且获取到页面中标题与金额，将其存储到csv文件中
'''
import urllib.request
import ssl
import threading
import os
import time
import re
import csv


def getdata(url):
    context = ssl._create_unverified_context()
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    requset = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(requset, context=context)
    data = response.read()

    return data.decode()


def getarea(url):
    data = getdata(url)
    quyuList = re.findall(r'data-type="district" class="filter__item--level2  ">.*?<a href="(.*?)"  >(.*?)</a>',data,re.S)
    # print(quyuList)
    return dict(quyuList)


def getareadata(path,area):
    data = getdata(path)
    resList = re.findall(r'<p class="content__list--item--title twoline">.*?<a.*?>(.*?)</a>.*?<em>(.*?)</em>',data,re.S)
    # print(resList)
    with open(area+".csv","w",encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(resList)


if __name__ == '__main__':
    url = "https://sz.lianjia.com/zufang/"
    url2 = "https://sz.lianjia.com"
    os.mkdir("file")
    os.chdir("file")
    areadict = getarea(url)
    # print(areadict)
    # path ="https://sz.lianjia.com/zufang/futianqu/"
    # t = threading.Thread(target=getareadata, args=(path, '福田'))
    # t.start()
    for areapath,area in areadict.items():
        path = url2+areapath
        t = threading.Thread(target=getareadata,args=(path,area))
        t.start()







