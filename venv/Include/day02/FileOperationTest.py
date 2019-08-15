#文件操作之递归复制
import os
# # file中的路径不能是文件夹的路径，必须是文件的路径。不然会报无此权限的错误，目前没找到解决办法
# file=open(file='C:\\Users\\Administrator\\Desktop\\被复制的目录\\笔记.txt',encoding="gb2312")
# print(file)
# h=file.read()
# print(h)
# # 此时的file是_io.TextIOWrapper对象，该对象不是序列。输出的是对象的所有已赋值的属性
# # 如果涉及到中文，还是别用utf-8，用gb2312.
# text=file.read(1024)
# # print(text)
# file.close()



# 如果要给指定的文件夹写入文件,须指定文件名.不然会报错(就是报权限问题的错)
dd=input("请输入文件名:")
file1=open(file="C:\\Users\\Administrator\\Desktop\\目标文件夹\\"+str(dd)+".txt",mode="w+",encoding="gb2312")
file1.write(text)
text1=file1.read(1024)
print(text1)
file1.close()

# # 要复制的文件目录
# aimLink="aim"
# # 要存放的文件目录
# totoLink="toto"

# def ddCopy(aimLink,totoLink):
#     # 递归复制aimLink目录下的文件
#     # 如果aimLink不是目录而是文件,则直接复制
#     if not os.path.isdir(aimLink):
