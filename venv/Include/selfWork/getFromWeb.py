#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc
import re
import os

from bs4 import BeautifulSoup
# 先给定一个目录,抓取其下的网页
base="C:\\Users\\Administrator\\Desktop\\python_课件+实验指导书\\lab\\website"
saveFile=[]
saveDir=[]
# 以广度优先的方式,循环遍历的获取网页,要求能从网页超链接中跳转地获取.
# seedURL就是base,targetDir就是处理完爬取到的网页内容之后将文件保存的指定目录,maxDepth就是爬取时跳转的深度.
# crawler是爬取策略和执行的方法
haveGetFile=[]
haveGetDir=[]
maxDepth=0
# Dir下的所有文件找出来,放在file中
def crawler(file, Dir, max):
    while 1:
        if not Dir:
            break
        else:
            if max<=0:
                break
            else:
                for aDir in Dir:
                    max-=1
                    init(aDir,max)


def init(seedURL,max):
    if max>0:
        if not os.path.exists(seedURL):
            print("输入的基础目录不存在")
        else:
            if os.path.isdir(seedURL):
                fileAndDir=os.listdir(seedURL)
                for target in fileAndDir:
                    # 分别存放
                    targetLink=os.path.join(seedURL, target)
                    if os.path.isdir(targetLink):
                        if targetLink not in saveDir and targetLink not in haveGetFile:
                            saveDir.append(targetLink)
                        else:
                            pass
                    else:
                        if targetLink not in saveFile and targetLink not in haveGetDir:
                            saveFile.append(targetLink)
    else:
        print("已到达最大深度")



def htmlDataGet():
    for a in saveFile:
        if a.endswith(".html"):
            print(a)
            # print(dd)
            htmlFile=open(a,mode='r+',encoding='utf-8')
            haveGetFile.append(a)
            # print(htmlFile.name)
            h=htmlFile.read()
            # patter=re.compile(r'C:\\Users\\Administrator\\Desktop\\python_课件+实验指导书\\lab\\website\\(.*?).html')
            # h里面竟然是空的......(实际上目标地址的网页本身就是空的...)
            dd=BeautifulSoup(h,"html.parser")
            linkg=dd.find_all("a")
            for link in linkg:
                re1 = re.findall('href=".*?"', str(link))
                str1=htmlDataProcessing(re1[0])
            #   统计<p>.....</p>中字符出现的频次
            wordg=dd.find_all("p")
            print(wordg)
            for word in wordg:
                item=wordProsess(str(word).lstrip('<p>').rstrip('</p>'))
            print(item)
            htmlFile.close()
            # try:
            #     open('C:\\Users\\Administrator\\Desktop\\目标文件夹\\')
            # except:
            #     print("写入失败")
        else:
            pass
    haveGetDir=saveDir
    saveDir.clear()
    saveFile.clear()

# 统计文件中单个字母出现的频次
def wordProsess(file):
    item={}
    for a in file:
        if a not in item:
            file.count(a)
            item[a]=file.count(a)
        else:pass
    return item

def htmlDataProcessing(str1):
    str1=str1.lstrip('href="').rstrip('"')
    str1=str1.replace("/","\\")
    return str1





if __name__=="__main__":
    maxDepth = int(input("请设置抓取深度:"))
    init(base,maxDepth)
    crawler(saveFile, saveDir, maxDepth)
    htmlDataGet()
    print(saveFile)
    print(saveDir)
    print(haveGetFile)
    print(haveGetDir)


