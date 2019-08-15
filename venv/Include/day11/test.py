# class Student:
#     name='dd'
#     #当用Student创建新的对象时,会自动调用__init__()函数(如果有)
#     def __init__(self):
#         self.className='111'
#         self.name='gg'
# student=Student()
# print(student.name)
# #这个就不会出错
# print(student.className)
# print(Student.name)
# print(Student.className)

# student=Student
# print(student.name)
# #类变量直接定义在类中变量，成员变量是定义在方法绑定在self身上的变量
# #这个就会出错,因为student是一个类,并不会调用__init__()给Student类添加新的成员变量,
# #以类来调用时,优先使用类变量,而不是在函数中创建的成员变量
# #类变量随着类的加载而出现，成员变量随着对象的创建而出现
# print(student.className)

# stu=Student()
# stu.dd=1
# stu.name="沙雕"
# print(stu.dd)
# print(stu.name)

# stu=Student
# stu.name="zz"
# #注意这里原本是没有叫className的类变量的,实际上这里相当于是给Student添加了新的类变量
# stu.className="bc"
# print(stu.name)
# print(stu.className)

# from datetime import datetime
# timeNow=str(datetime.now())
# print("%s百度热点事件"%timeNow+"\t\t指数")
#假设输入时间格式为2099-01-01
# def suanTime(times):
#     dd=datetime.now()
#     print(int(times[0:4]),int(times[5:7]),int(times[8:10]))
#     times=datetime(int(times[0:4]),int(times[5:7]),int(times[8:10]))
#     print(dd-times)
#
# suanTime(input("请输入一个时间"))

# class classMate():
#     name='沙雕'
#     age=0
#     hobby="唱跳rap篮球"
#     def selfIntroduction(self):
#         print("我是%s,%s岁,喜欢%s"%(self.name,self.age,self.hobby))
#
#
# classmatee=classMat()
# classmate.selfIntroduction()

# print('�')   遇到无法解析的字符时就会用这个代替