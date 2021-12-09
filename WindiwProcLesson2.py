from PySide2 import QtWidgets, QtCore, QtGui
from MainFormLesson2 import  Ui_MainWindow
from functools import partial

class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        # Для отображения формы нужно добавить дые строки
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.move(450, 250)

        self.ui.BLeftTop.clicked.connect(partial(self.BMove, 0, 0))
        self.ui.BRightTop.clicked.connect(partial(self.BMove, 1000, 0))

    # Декорато для явного указания, что эта функция - слот
    @QtCore.Slot()
    def BMove(self, x, y,):

        screen_count = QtWidgets.QApplication.screens()


        for screens_count in screen_count:
            # self.ui.plainTextEdit.appendPlainText("Высота экрана")
            self.ui.plainTextEdit.appendPlainText(f"Разрешение экрана: {screens_count.size().width()} на {screens_count.size().height()}")
            self.ui.plainTextEdit.appendPlainText(f"Размер окна: {self.size().width()} на {self.size().height()}")

            # текущее положение
            self.pos().x()
            self.pos().y()
            self.move(x, y)

    def BChangePosition(self):
        self.move(100, 100)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()


    app.exec_()