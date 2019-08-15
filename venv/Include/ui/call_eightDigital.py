import sys
import time
from collections import deque
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Include.ui.eightDidital import *


class WorkThread(QThread):
    signal = pyqtSignal(int)
    def __init__(self):
        super(WorkThread, self).__init__()
        self.working = True
        self.x = 0
    def __del__(self):
        self.working = False
        self.wait()
    def run(self):
        while self.working:
            self.signal.emit(self.x)
            self.x = self.x + 1
            time.sleep(1)


class MyFrom(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.retCode = 0
        self.lst_steps = []
        self.workThread = WorkThread()

        self.ui.btn_calculate.clicked.connect(self.calculate_event)
        self.ui.btn_begin.clicked.connect(self.start_event)
        self.workThread.signal.connect(self.callback)
        self.ui.btn_stop.clicked.connect(self.stop_event)
        self.ui.btn_continue.clicked.connect(self.continue_event)

    def start_event(self):
        self.workThread.x = 0
        self.workThread.working = True
        self.workThread.start()

    def stop_event(self):
        self.workThread.working = False

    def continue_event(self):
        self.workThread.working = True
        self.workThread.start()

    def callback(self, x):
        if x <= len(self.lst_steps) - 1:
            lst = self.lst_steps[x]
            self.showImage(lst)
            self.ui.label_step_show.setText(str(x + 1) + "/"
                                 + str(len(self.lst_steps)))
        else:
            self.workThread.working = False

    def showImage(self, lst):
        for lst_len in range(len(lst)):
            path = "./image/" + lst[lst_len] + ".jpg"
            pix = QPixmap(path)
            if lst_len == 0:
                self.ui.label_step_0.setPixmap(pix)
            elif lst_len == 1:
                self.ui.label_step_1.setPixmap(pix)
            elif lst_len == 2:
                self.ui.label_step_2.setPixmap(pix)
            elif lst_len == 3:
                self.ui.label_step_3.setPixmap(pix)
            elif lst_len == 4:
                self.ui.label_step_4.setPixmap(pix)
            elif lst_len == 5:
                self.ui.label_step_5.setPixmap(pix)
            elif lst_len == 6:
                self.ui.label_step_6.setPixmap(pix)
            elif lst_len == 7:
                self.ui.label_step_7.setPixmap(pix)
            elif lst_len == 8:
                self.ui.label_step_8.setPixmap(pix)
            else:
                pass

    def calculate_event(self):
        srcLayout = ""
        destLayout = ""

        if self.ui.lineEdit_src_0.text() == "":
            srcLayout = "0" + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_1.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + "0" + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_2.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + "0" + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_3.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + "0" + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_4.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + "0" + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_5.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + "0" + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_6.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + "0" + self.ui.lineEdit_src_7.text() + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_7.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + "0" + self.ui.lineEdit_src_8.text()
        elif self.ui.lineEdit_src_8.text() == "":
            srcLayout = self.ui.lineEdit_src_0.text() + self.ui.lineEdit_src_1.text() + self.ui.lineEdit_src_2.text() + self.ui.lineEdit_src_3.text() + self.ui.lineEdit_src_4.text() + self.ui.lineEdit_src_5.text() + self.ui.lineEdit_src_6.text() + self.ui.lineEdit_src_7.text() + "0"
        else:
            pass

        if self.ui.lineEdit_dest_0.text() == "":
            destLayout = "0" + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_1.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + "0" + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_2.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + "0" + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_3.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + "0" + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_4.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + "0" + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_5.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + "0" + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_6.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + "0" + self.ui.lineEdit_dest_7.text() + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_7.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + "0" + self.ui.lineEdit_dest_8.text()
        elif self.ui.lineEdit_dest_8.text() == "":
            destLayout = self.ui.lineEdit_dest_0.text() + self.ui.lineEdit_dest_1.text() + self.ui.lineEdit_dest_2.text() + self.ui.lineEdit_dest_3.text() + self.ui.lineEdit_dest_4.text() + self.ui.lineEdit_dest_5.text() + self.ui.lineEdit_dest_6.text() + self.ui.lineEdit_dest_7.text() + "0"
        else:
            pass


        self.retCode, self.lst_steps = self.solvePuzzle_breadth(srcLayout, destLayout)
        print(self.retCode)
        print(self.lst_steps)
        if self.retCode == 0:
            self.ui.label_step_show.setText("0/" + str(len(self.lst_steps)))
        else:
            self.ui.label_step_show.setText("目标不可达")

    def swap_chr(self, a, i, j):
        if i > j:
            i, j = j, i
        b = a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
        return b

    def solvePuzzle_breadth(self, srcLayout, destLayout):
        g_dict_layouts = {}
        g_dict_shifts = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                         3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
                         6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
        g_dict_layouts[srcLayout] = -1
        queue_layouts = deque()
        queue_layouts.append(srcLayout)
        bfound = False
        while len(queue_layouts) > 0:
            curLayout = queue_layouts.popleft()
            if curLayout == destLayout:
                bfound = True
                break
                # 寻找0 的位置
            ind_slide = curLayout.index("0")
            lst_shifts = g_dict_shifts[ind_slide]
            for nShift in lst_shifts:
                newLayout = self.swap_chr(curLayout, nShift, ind_slide)
                if g_dict_layouts.get(newLayout) == None:
                    g_dict_layouts[newLayout] = curLayout
                    queue_layouts.append(newLayout)
        if bfound:
            self.lst_steps = []
            self.lst_steps.append(curLayout)
            while g_dict_layouts[curLayout] != -1:
                self.lst_steps.append(g_dict_layouts[curLayout])
                curLayout = g_dict_layouts[curLayout]
            self.lst_steps.reverse()
            return 0, self.lst_steps
        else:
            return -1, None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myFrom = MyFrom()
    myFrom.show()
    sys.exit(app.exec_())
