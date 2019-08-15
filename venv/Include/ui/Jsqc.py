from Include.ui.Jsq import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Jsqc (QMainWindow):
    ans = 0
    flag = "true"
    a = 0
    b = 0
    c = "?"
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.coonet()
    def coonet(self):
        self.ui.pushButton.clicked.connect(self.p1)
        self.ui.pushButton_2.clicked.connect(self.p2)
        self.ui.pushButton_3.clicked.connect(self.p3)
        self.ui.pushButton_4.clicked.connect(self.p4)
        self.ui.pushButton_5.clicked.connect(self.p5)
        self.ui.pushButton_6.clicked.connect(self.p6)
        self.ui.pushButton_7.clicked.connect(self.p7)
        self.ui.pushButton_8.clicked.connect(self.p8)
        self.ui.pushButton_9.clicked.connect(self.p9)
        self.ui.pushButton_10.clicked.connect(self.p0)
        self.ui.pushButton_11.clicked.connect(self.p11)
        self.ui.pushButton_12.clicked.connect(self.p12)
        self.ui.pushButton_13.clicked.connect(self.p13)
        self.ui.pushButton_14.clicked.connect(self.p14)
        self.ui.pushButton_15.clicked.connect(self.p15)
        self.ui.pushButton_16.clicked.connect(self.p16)

    def p1(self):
        if self.flag=="true":
          self.a=self.ui.lcdNumber.intValue()*10+1
          self.ui.lcdNumber.display(self.a)
        else:
            self.b=self.ui.lcdNumber.intValue()*10+1
            self.ui.lcdNumber.display(self.b)
    def p2(self):
        if self.flag=="true":
          self.a=self.ui.lcdNumber.intValue()*10+2
          self.ui.lcdNumber.display(self.a)
        else:
            self.b=self.ui.lcdNumber.intValue()*10+2
            self.ui.lcdNumber.display(self.b)
    def p3(self):
        if self.flag=="true":
          self.a=self.ui.lcdNumber.intValue()*10+3
          self.ui.lcdNumber.display(self.a)
        else:
            self.b=self.ui.lcdNumber.intValue()*10+3
            self.ui.lcdNumber.display(self.b)
    def p4(self):
        if self.flag=="true":
          self.a=self.ui.lcdNumber.intValue()*10+4
          self.ui.lcdNumber.display(self.a)
        else:
            self.b=self.ui.lcdNumber.intValue()*10+4
            self.ui.lcdNumber.display(self.b)
    def p5(self):
        if self.flag=="true":
          self.a=self.ui.lcdNumber.intValue()*10+5
          self.ui.lcdNumber.display(self.a)
        else:
            self.b=self.ui.lcdNumber.intValue()*10+5
            self.ui.lcdNumber.display(self.b)
    def p6(self):
        if self.flag=="true":
          self.a=self.ui.lcdNumber.intValue()*10+6
          self.ui.lcdNumber.display(self.a)
        else:
            self.b=self.ui.lcdNumber.intValue()*10+6
            self.ui.lcdNumber.display(self.b)
    def p7(self):
        if self.flag == "true":
            self.a = self.ui.lcdNumber.intValue() * 10 + 7
            self.ui.lcdNumber.display(self.a)
        else:
            self.b = self.ui.lcdNumber.intValue() * 10 + 7
            self.ui.lcdNumber.display(self.b)
    def p8(self):
        if self.flag == "true":
            self.a = self.ui.lcdNumber.intValue() * 10 + 8
            self.ui.lcdNumber.display(self.a)
        else:
            self.b = self.ui.lcdNumber.intValue() * 10 + 8
            self.ui.lcdNumber.display(self.b)
    def p9(self):
        if self.flag == "true":
            self.a = self.ui.lcdNumber.intValue() * 10 + 9
            self.ui.lcdNumber.display(self.a)
        else:
            self.b = self.ui.lcdNumber.intValue() * 10 + 9
            self.ui.lcdNumber.display(self.b)
    def p0(self):
        if self.flag == "true":
            self.a = self.ui.lcdNumber.intValue() * 10
            self.ui.lcdNumber.display(self.a)
        else:
            self.b = self.ui.lcdNumber.intValue() * 10
            self.ui.lcdNumber.display(self.b)
    def p11(self):
        self.ui.lcdNumber.display(0)
        if self.c=="?":
            self.c="+"
            self.flag="false"
    def p12(self):
        self.ui.lcdNumber.display(0)
        if self.c == "?":
            self.c = "-"
            self.flag = "false"
    def p13(self):
        self.ui.lcdNumber.display(0)
        if self.c == "?":
            self.c = "*"
            self.flag = "false"
    def p14(self):
        self.ui.lcdNumber.display(0)
        if self.c == "?":
            self.c = "/"
            self.flag = "false"

    def p15(self):
        if self.c=="+":
            self.ans=self.a+self.b
            self.ui.lcdNumber.display(self.ans)
        elif self.c=="-":
            self.ans=self.a-self.b
            self.ui.lcdNumber.display(self.ans)
        elif self.c == "*":
            self.ans = self.a * self.b
            self.ui.lcdNumber.display(self.ans)
        elif self.c == "/"and self.b!=0:
            self.ans = self.a / self.b
            self.ui.lcdNumber.display(self.ans)
        elif self.c=="/"and self.b==0:
            self.ui.Label.setText("除数不应为0,请按清空键恢复")
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.pushButton_13.setEnabled(False)
            self.ui.pushButton_14.setEnabled(False)
            self.ui.pushButton_15.setEnabled(False)
        self.flag="false"
        self.c="?"
        self.a=self.ans
        self.b=0

    def p16(self):
        self.ans = 0
        self.a=0
        self.b=0
        self.c="?"
        self.flag="true"
        self.ui.lcdNumber.display(0)

        if self.ui.pushButton_15.isChecked():
              print(1)
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.pushButton_13.setEnabled(True)
            self.ui.pushButton_14.setEnabled(True)
            self.ui.pushButton_15.setEnabled(True)
            self.ui.Label.setText("提示框                    ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui=Jsqc()
    ui.show()
    sys.exit(app.exec_())