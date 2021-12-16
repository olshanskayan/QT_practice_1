from PySide2 import QtWidgets, QtCore, QtGui
from MainFormLesson3 import Ui_MainWindow
import time
import requests

class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        # Для отображения формы нужно добавить две строки
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # инициализация потока для GroupBox1
        self.t1 = GBThread1()
        # self.t1.signal1.connect(lambda: print('signal '))
        self.t1.signal1.connect(self.BStLineEdit)

        # нажатие кнопки Начать отсчет
        self.ui.BStartCounter.clicked.connect(self.BStartCounterProcessing)

        # инициализация потока для GroupBox2
        self.t2= GBThread2()
        # self.t1.signal1.connect(lambda: print('signal '))
        self.t2.signal2.connect(self.LEURL)

        # нажатие кнопки Начать отсчет
        self.ui.BStartCounter.clicked.connect(self.BStaptProcessing)


    # обработка событий в GroupBox1
    # обработка нажатия кнопки Начать отсчет
    def BStartCounterProcessing(self):
        self.t1.setStartCounter(self.ui.SBSetTime.value())
        self.t1.start()

    def BStLineEdit(self, value_):
        self.ui.LEAuditTime.setText(str(value_))

    # обработка событий в GroupBox2
    # def BStartProcessing(self):
    #     self.t2.


class GBThread1(QtCore.QThread):

    signal1 = QtCore.Signal(int)

    def setStartCounter(self, SBSetTime: int ):
        self.SBSetTime = SBSetTime
        # self.LEAuditTime.text = SBSetTime

    def run(self)->None:
        self.status = True

        while self.status:
            self.signal1.emit(self.SBSetTime)
            self.SBSetTime -=1
            time.sleep(1)
            if self.SBSetTime == -1:
                break


class GBThread2(QtCore.QThread):

    signal2 = QtCore.Signal(int)

    def getURL(self, LEURL: str ):
        print("Проверили доступность")

    def SetSPBox2(self, SPBox2):
        self.SPBox2 = SPBox2

    def SetLEURL(self, LEURL):
        self.LEURL = LEURL

    def run(self)->None:
        self.status = True

        while self.status:
            self.signal2.emit(self.LEUR)

            r = requests.get(self.LEUR)
            r.status_code

            time.sleep(1)
            if mycount == 20:
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()


    app.exec_()