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

        #------------------------------------------------------------------
        # инициализация потока для GroupBox2
        self.t2 = GBThread2()
        # self.t1.signal1.connect(lambda: print('signal '))
        self.t2.signal2.connect(self.BStLineEditURL)

        # нажатие кнопки Начать отсчет
        self.ui.BStart.clicked.connect(self.BStartCounterProcessingURL)

    # обработка событий в GroupBox2
    # обработка нажатия кнопки Начать отсчет
    def BStartCounterProcessingURL(self):
        self.t2.SetLEURL(self.ui.LEURL.text())
        self.t2.start()

    def BStLineEditURL(self, value_):
        self.ui.TELog.appendPlainText((f"Запрос прошёл со статусом: {str(value_)}"))


    # обработка событий в GroupBox1
    # обработка нажатия кнопки Начать отсчет
    def BStartCounterProcessing(self):
        self.t1.setStartCounter(self.ui.SBSetTime.value())
        self.t1.start()

    def BStLineEdit(self, value_):
        self.ui.LEAuditTime.setText(str(value_))


class GBThread1(QtCore.QThread):

    signal1 = QtCore.Signal(int)

    def setStartCounter(self, SBSetTime: int ):
        self.SBSetTime = SBSetTime
        # self.LEAuditTime.text = SBSetTime

    def run(self)->None:
        self.status = True

        while self.status:
            self.signal1.emit(self.SBSetTime)
            self.SBSetTime -= 1
            time.sleep(1)
            if self.SBSetTime == -1:
                break


class GBThread2(QtCore.QThread):

    signal2 = QtCore.Signal(int)

    # def SetSPBox2(self, SPBox2 ):
    #     self.SPBox2 = SPBox2

    def SetLEURL(self, LEURL: str ):
        self.LEURL = LEURL

    def run(self) -> None:
        self.status = True

        while self.status:
            print("Делаем запрос")

            r = requests.get(self.LEURL)
            # r.status_code
            self.signal2.emit(r.status_code)
            print(str(r.status_code))
            print("Прошли запрос запрос")

            self.status = False

        print("Вышли из цикла")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()


    app.exec_()