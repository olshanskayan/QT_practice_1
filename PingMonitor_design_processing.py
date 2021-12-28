# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtCore, QtGui
from PingMonitor_design import Ui_Form
import sys
import os
import time
import requests

class PingMonitortWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PingMonitortWindow, self).__init__(parent)

        # Для отображения формы нужно добавить две строки
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #Добавляем строки в grid
        self.ui.tableWidget.insertRow(0)
        # self.ui.tableWidget.insertRow(1)
        # self.ui.tableWidget.insertRow(2)

        #Задаем значение строк, т.е. прописываем ip-адреса для наблюдения
        self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('8.8.8.8'))
        # self.ui.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem('7.7.7.7'))
        # self.ui.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem('5.5.5.5'))

        # инициализация потока для tableWidget
        self.t1 = GBThreadTWidget()
        # self.t1.signal1.connect()

        # нажатие кнопки Начать отсчет
        self.ui.pushButton.clicked.connect(self.pushButtonProcessing)

    def GetIpAdesses(self):
        _List = []
        for i in range(self.ui.tableWidget.rowCount()):
            _List.append(self.ui.tableWidget.item(i, 0).data(0))

        return(_List)

    # обработка нажатия кнопки Старт
    def pushButtonProcessing(self):
        self.t1.SetIpAdress(self.GetIpAdesses())
        self.t1.start()
        # print(self.GetIpAdesses())

class GBThreadTWidget(QtCore.QThread):

    signal1 = QtCore.Signal(int)

    def SetIpAdress(self, IpList: list):
        self.IpList = IpList

    def run(self) -> None:
        self.status = True

        while self.status:
            for i in self.IpList:
                PingResult = os.system(f"ping {i}")
                print(PingResult)

            self.status = False

        print("Вышли из цикла")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = PingMonitortWindow()
    window.show()


    app.exec_()
