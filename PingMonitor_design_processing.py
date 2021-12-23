from PySide2 import QtWidgets, QtCore, QtGui
from PingMonitor_design import Ui_Form
import time
import requests

class PingMonitortWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PingMonitortWindow, self).__init__(parent)

        # Для отображения формы нужно добавить две строки
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.tableWidget.insertRow(0)
        self.ui.tableWidget.insertRow(1)
        self.ui.tableWidget.insertRow(2)

        self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('8.8.8.8'))
        self.ui.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem('7.7.7.7'))
        self.ui.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem('5.5.5.5'))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = PingMonitortWindow()
    window.show()


    app.exec_()
