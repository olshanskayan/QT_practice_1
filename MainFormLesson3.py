# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFormLesson3.ui'
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
        MainWindow.resize(921, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(10, 10, 283, 114))
        self.gridLayout = QGridLayout(self.groupBox1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.BStartCounter = QPushButton(self.groupBox1)
        self.BStartCounter.setObjectName(u"BStartCounter")

        self.gridLayout.addWidget(self.BStartCounter, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.SBSetTime = QSpinBox(self.groupBox1)
        self.SBSetTime.setObjectName(u"SBSetTime")
        self.SBSetTime.setValue(0)

        self.gridLayout.addWidget(self.SBSetTime, 1, 1, 1, 1)

        self.LEAuditTime = QLineEdit(self.groupBox1)
        self.LEAuditTime.setObjectName(u"LEAuditTime")

        self.gridLayout.addWidget(self.LEAuditTime, 3, 1, 1, 2)

        self.label_4 = QLabel(self.groupBox1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)

        self.groupBox2 = QGroupBox(self.centralwidget)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setGeometry(QRect(300, 10, 276, 431))
        self.gridLayout_2 = QGridLayout(self.groupBox2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)

        self.label_7 = QLabel(self.groupBox2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.LEURL = QLineEdit(self.groupBox2)
        self.LEURL.setObjectName(u"LEURL")

        self.gridLayout_2.addWidget(self.LEURL, 1, 1, 1, 2)

        self.label_8 = QLabel(self.groupBox2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 2)

        self.SPBox2 = QSpinBox(self.groupBox2)
        self.SPBox2.setObjectName(u"SPBox2")

        self.gridLayout_2.addWidget(self.SPBox2, 2, 2, 1, 1)

        self.BStart = QPushButton(self.groupBox2)
        self.BStart.setObjectName(u"BStart")

        self.gridLayout_2.addWidget(self.BStart, 3, 0, 1, 1)

        self.BStop = QPushButton(self.groupBox2)
        self.BStop.setObjectName(u"BStop")

        self.gridLayout_2.addWidget(self.BStop, 4, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)

        self.TELog = QPlainTextEdit(self.groupBox2)
        self.TELog.setObjectName(u"TELog")

        self.gridLayout_2.addWidget(self.TELog, 6, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(590, 10, 321, 431))
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 171, 16))
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 50, 111, 16))
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(190, 50, 47, 13))
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 90, 47, 13))
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(170, 90, 47, 13))
        self.SBUpdate = QSpinBox(self.groupBox_3)
        self.SBUpdate.setObjectName(u"SBUpdate")
        self.SBUpdate.setGeometry(QRect(130, 50, 42, 22))
        self.PGCPU = QProgressBar(self.groupBox_3)
        self.PGCPU.setObjectName(u"PGCPU")
        self.PGCPU.setGeometry(QRect(10, 120, 141, 301))
        self.PGCPU.setValue(24)
        self.PGCPU.setOrientation(Qt.Vertical)
        self.PBRAM = QProgressBar(self.groupBox_3)
        self.PBRAM.setObjectName(u"PBRAM")
        self.PBRAM.setGeometry(QRect(170, 120, 141, 301))
        self.PBRAM.setValue(24)
        self.PBRAM.setOrientation(Qt.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 921, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox1.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0435\u043a.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f:", None))
        self.BStartCounter.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0442\u0441\u0447\u0435\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438:", None))
        self.LEAuditTime.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0435\u043a.", None))
        self.groupBox2.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0441\u0430\u0439\u0442\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.LEURL.setText(QCoreApplication.translate("MainWindow", u"https://google.com", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c \u043a\u0430\u0436\u0434\u044b\u0435:", None))
        self.BStart.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.BStop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433:", None))
        self.groupBox_3.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u044b:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u044f\u0442\u044c \u043a\u0430\u0436\u0434\u044b\u0435:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0435\u043a.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
    # retranslateUi

