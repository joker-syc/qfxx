#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import urllib.request
import ssl
def getData():
    # if a==1:
    #     a=""
    context = ssl._create_unverified_context()
    # url = "https://www.qiushibaike.com/text/page/"+str(a)
    url = "https://www.baidu.com/"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    requset = urllib.request.Request(url,headers=header)

    response = urllib.request.urlopen(requset,context=context)

    data = response.read()

    return data.decode()

if __name__ == '__main__':
    getData()
