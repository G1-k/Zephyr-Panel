# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zephyr.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/rog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 631))
        self.label.setMouseTracking(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/g1k/zephyr-panel/img1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(30, 110, 81, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy)
        self.b2.setMouseTracking(True)
        self.b2.setTabletTracking(True)
        self.b2.setAutoFillBackground(False)
        self.b2.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/2.jpg\')")
        self.b2.setObjectName("b2")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(30, 50, 81, 51))
        self.b1.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/1.png\')")
        self.b1.setObjectName("b1")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(30, 170, 111, 51))
        self.b3.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/3.png\')")
        self.b3.setObjectName("b3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 211, 121))
        self.label_2.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/4.5.png\')")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.f3 = QtWidgets.QPushButton(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(620, 530, 241, 81))
        self.f3.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/f6.2.jpg\')")
        self.f3.setText("")
        self.f3.setObjectName("f3")
        self.f2 = QtWidgets.QPushButton(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(380, 530, 231, 81))
        self.f2.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/F4.png\')")
        self.f2.setText("")
        self.f2.setObjectName("f2")
        self.f1 = QtWidgets.QPushButton(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(130, 530, 241, 81))
        self.f1.setStyleSheet("border-image: url(\'/home/g1k/zephyr-panel/f5.5.png\')")
        self.f1.setText("")
        self.f1.setObjectName("f1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "G1k - Zephyr Panel"))
        self.b2.setText(_translate("MainWindow", "MED"))
        self.b1.setText(_translate("MainWindow", "    LOW"))
        self.b3.setText(_translate("MainWindow", "HIGH"))

