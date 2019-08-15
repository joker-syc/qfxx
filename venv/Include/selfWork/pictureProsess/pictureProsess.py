#/usr/bin/env python
#-*- coding: utf-8 -*-
# Editer:jokersyc
from PIL import Image
# 图片显示时使用的是当前操作系统自带的图片显示软件来显示
# img=Image.open("C:\\Users\\Administrator\\Desktop\\day02知识回顾.png")
# img.show()

# import matplotlib.pyplot as plt
# # 使用一个matplotlib的库来绘制图片进行显示
# img=Image.open("C:\\Users\\Administrator\\Desktop\\dd.jpg")

# plt.figure("dog")
# plt.imshow(img)                   #将图片装载进去
# plt.show()
# figure默认是带axis的，如果没有需要，我们可以关掉()
# plt.axis("off")(图片坐标)


# gray=img.convert('L')
# plt.imshow(gray,cmap='gray')
# plt.show()
'''
现在大部分的彩色图像都是采用RGB颜色模式，处理图像的时候，要分别对RGB三种分量进行处理，实际上RGB并不能反映图像的形态特征，只是从光学的原理上进行颜色的调配。
现在有很多其他的颜色模式，例如HSI模式，HSI是由色调，饱和度，亮度三个分量来表示颜色。HSI比RGB更符合人的视觉特性。
但是HSI也是三通道，真正反映图像特征的变量是I，其他都是色彩的反映。
所以我们经常要把图像弄成8位的灰度值图像直接进行处理，可以通过直方图，灰度变化，还有正交变换之类的进行处理。甚至经常把图像分割之后变成二值图像处理。


使用函数convert()来进行转换，它是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式，mode 的取值可以是如下几种：

.1（1位像素，黑白，每字节存储一个像素）
·L（8位像素，黑白）
·P（8位像素，使用调色板映射到任何其他模式）
·RGB（3x8位像素，真彩色）
·rgba（4x8位像素，带透明蒙版的真彩色）
·CMYK（4x8位像素，分色）
·YCBCR（3x8位像素，彩色视频格式）
·I（32位有符号整数像素）
·F（32位浮点像素）
'''
# gray=img.convert('L')   #转换成灰度
# r,g,b=img.split()   #分离三通道
# pic=Image.merge('RGB',(r,g,b)) #合并三通道
# plt.figure("beauty")
# plt.subplot(2,3,1), plt.title('origin')
# plt.imshow(img),plt.axis('off')
# plt.subplot(2,3,2), plt.title('gray')
# plt.imshow(gray,cmap='gray'),plt.axis('off')
# plt.subplot(2,3,3), plt.title('merge')
# plt.imshow(pic),plt.axis('off')
# plt.subplot(2,3,4), plt.title('r')
# plt.imshow(r,cmap='gray'),plt.axis('off')
# plt.subplot(2,3,5), plt.title('g')
# plt.imshow(g,cmap='gray'),plt.axis('off')
# plt.subplot(2,3,6), plt.title('b')
# plt.imshow(b,cmap='gray'),plt.axis('off')
# plt.show()

# plt.subplot(1,2,1)
# plt.imshow(img)
#
# dd=(100,200,300,400)    #left, upper, right, lower(左上右下)
# roi=img.crop(dd)
# plt.subplot(1,2,2)
# plt.imshow(roi)
# plt.show()

# plt.subplot(1,2,1)
# plt.imshow(img)
#
# box=(80,100,260,300)
# roi=img.crop(box)
# plt.subplot(1,2,2)
# plt.imshow(roi)
# plt.show()