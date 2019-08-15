#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
import threading
'''
通过继承的方式实现多线程
类一定要继承threading.Thread类
并且一定要重写run方法。
调用的时候我们无需手动调用run方法，调用start方法即可。
'''
import urllib.request
import ssl


class MyThread(threading.Thread):

    def __init__(self,url):
        self.url = url
        super().__init__()

    def getdata(self):
        context = ssl._create_unverified_context()
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
        requset = urllib.request.Request(self.url, headers=header)
        response = urllib.request.urlopen(requset, context=context)
        data = response.read()
        return data.decode()

    def run(self):
        print(threading.current_thread().name)
        print(self.url)
        data = self.getdata()
        with open("baidu.html","w",encoding="utf-8") as f:
            f.write(data)


if __name__ == '__main__':
    url = "https://www.baidu.com/"
    thread = MyThread(url)
    thread.start()
'''
使用这种方式爬取百度首页
'''

