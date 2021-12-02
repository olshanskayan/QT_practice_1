from PySide2 import QtWidgets, QtCore, QtGui


class MainTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.lineEditSurname = QtWidgets.QLineEdit("Фамилия")
        self.lineEditSurname.setPlaceholderText("Фамилия")
        self.lineEditName = QtWidgets.QLineEdit("Имя")
        self.lineEditName.setPlaceholderText("Имя")
        self.lineEditTel = QtWidgets.QLineEdit("Телефон")
        self.lineEditTel.setPlaceholderText("Телефон")

        self.pushButtonOk = QtWidgets.QPushButton("Ok")

        #Для визуализации добавим поле вывода
        layout = QtWidgets.QVBoxLayout()

        #Добавим в него компоненты
        layout.addWidget(self.lineEditSurname)
        layout.addWidget(self.lineEditName)
        layout.addWidget(self.lineEditTel)
        layout.addWidget(self.pushButtonOk)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()