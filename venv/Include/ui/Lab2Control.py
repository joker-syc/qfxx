import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from Include.ui.LoginWindow import Ui_LoginWindow
from Include.ui.ManageWindow import Ui_ManageWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Lab2(QMainWindow):
    id=""
    username = ""
    pwd = ""
    gender=""
    isAdmin=""
    cur=""
    def __init__(self):
        super().__init__()
        # 连接数据库
        self.db = pymysql.connect("localhost", "root", "123456", "testdb", charset='utf8')
        # 获取游标、数据
        self.cur= self.db.cursor()
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self)
        self.loginConnect()


    def loginConnect(self):
        # 为按钮创建点击事件
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(QtCore.QCoreApplication.quit)
    def manageConnect(self):
        self.ui2.pushButton.clicked.connect(self.findU)
        self.ui2.pushButton_2.clicked.connect(self.deleteU)
        self.ui2.pushButton_3.clicked.connect(self.createU)
        self.ui2.pushButton_4.clicked.connect(self.out)

    def out(self):
        self.cur.close()
        QCoreApplication.quit()
    def findU(self):
        sql = "select * from tbuser  "
        self.cur.execute(sql)
        c=0
        b=0
        e=self.cur.execute(sql)
        g=self.cur.execute(sql)
        result = self.cur.fetchone()
        for f in range(e) :
            for a in result:
                print(result)
                if b>4:
                    b=0
                if f>0 and b>2:
                    c = c + 1
                    g=g-1
                newItem = QTableWidgetItem(str(a))
                print(newItem)
                self.ui2.tableWidget.setItem(c, b, newItem)
                b =b+1
            result = self.cur.fetchone()

    def deleteU(self):
        id = self.id
        name = self.username
        id2 = self.ui2.textEdit.toPlainText()
        username2 = self.ui2.textEdit_2.toPlainText()
        if self.isAdmin==1 or id==id2:
            sql="delete from tbuser where user_id=%s or user_name=%s"
            try:
                self.cur.execute(sql, [id2, username2])==1
                self.db.commit()
            except Exception as e:
                print("不存在此用户")
            else:print("删除成功")
        else:print("当前用户无此权限")

    def createU(self):
        id = self.id
        name = self.username
        id2 = self.ui2.textEdit.toPlainText()
        username2 = self.ui2.textEdit_2.toPlainText()
        passwd=self.ui2.textEdit_3.toPlainText()
        passwd2=self.ui2.textEdit_4.toPlainText()
        gender=self.ui2.comboBox.currentText()
        if self.ui2.checkBox.isChecked()==True:
           isAdmin=1
        else: isAdmin=0
        if self.isAdmin!=1 :
            print("当前用户无此权限")
        elif id2==id or id2==""or username2==""or passwd!=passwd2 or passwd==""or passwd2=="":
            print("输入的用户信息有误")
        else: sql="insert into tbuser(user_id,user_name,user_passwd,gender,isAdmin) values(%s,%s,%s,%s,%s) "
        try:
            self.cur.execute(sql,[id2,username2,passwd,gender,isAdmin])
            self.db.commit()
        except Exception as e:
            print("创建出现错误")
        else:print("创建成功")





    def login(self):
        self.id=self.ui.textEdit.toPlainText()
        self.pwd=self.ui.textEdit_2.toPlainText()
        sql="select * from tbuser where user_id=%s and user_passwd=%s"
        try:
            result=self.cur.execute(sql,[self.id,self.pwd])
        except Exception as e:
                print("用户ID或密码错误")
        else:
            if result==1:
              print("登陆成功")
              #登陆成功后记录登录用户是否为管理员，并按情况赋予相关的权限
              sql="select isAdmin from tbuser where user_id=%s and user_passwd=%s"
              self.cur.execute(sql, [self.id, self.pwd])
              result =  self.cur.fetchone()
              isAdmin=list(result)
              self.isAdmin=isAdmin[0]
              print(self.isAdmin)
              self.ui2=Ui_ManageWindow()
              self.ui2.setupUi(self)
              self.manageConnect()
            else:print("用户ID或密码错误")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui=Lab2()
    ui.show()
    sys.exit(app.exec_())
