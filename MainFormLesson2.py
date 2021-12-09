# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFormLesson2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BLeftTop = QPushButton(self.centralwidget)
        self.BLeftTop.setObjectName(u"BLeftTop")

        self.gridLayout.addWidget(self.BLeftTop, 0, 0, 1, 1)

        self.BRightTop = QPushButton(self.centralwidget)
        self.BRightTop.setObjectName(u"BRightTop")

        self.gridLayout.addWidget(self.BRightTop, 0, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 0, 2, 7, 1)

        self.BCenter = QPushButton(self.centralwidget)
        self.BCenter.setObjectName(u"BCenter")

        self.gridLayout.addWidget(self.BCenter, 1, 0, 1, 2)

        self.BLeftDown = QPushButton(self.centralwidget)
        self.BLeftDown.setObjectName(u"BLeftDown")

        self.gridLayout.addWidget(self.BLeftDown, 2, 0, 1, 1)

        self.BRightDown = QPushButton(self.centralwidget)
        self.BRightDown.setObjectName(u"BRightDown")

        self.gridLayout.addWidget(self.BRightDown, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)

        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")

        self.gridLayout.addWidget(self.dial, 5, 0, 1, 1)

        self.plainTextEditDigit = QPlainTextEdit(self.centralwidget)
        self.plainTextEditDigit.setObjectName(u"plainTextEditDigit")

        self.gridLayout.addWidget(self.plainTextEditDigit, 5, 1, 1, 1)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 6, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BLeftTop.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.BRightTop.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.BCenter.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.BLeftDown.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.BRightDown.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


