from PySide2 import QtWidgets, QtCore, QtGui
from MainForm import Ui_MainWindow


class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setPlaceholderText("Ля-ля-ля!!!")

        self.ui.toolBox.setCurrentIndex(0)
        self.ui.pushButton.clicked.connect(self.onPushButtonClick)


    def onPushButtonClick(self):
        # print("Hello")
        self.ui.lineEdit.setText("Иванов")

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()