#!/usr/bin/env python

import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def call_b1():
    os.system("sudo .~/rogauracore/rogauracore initialize_keyboard  && sudo .~/rogauracore/rogauracore brightness 1")


def call_b2():
    os.system("sudo .~/rogauracore/rogauracore initialize_keyboard  && sudo .~/rogauracore/rogauracore brightness 2")

def call_b3():
    os.system("sudo .~/rogauracore/rogauracore initialize_keyboard  && sudo .~/rogauracore/rogauracore brightness 3")


def call_f1():
    os.system("echo 2 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")

def call_f2():
    os.system("echo 0 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")

def call_f3():
    os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    
    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    #qp.setColor(QPalette.Window, Qt.black)
    qp.setColor(QPalette.Button, Qt.gray)
    #qp.setColor(QPalette.Label, Qt.gray)
    app.setPalette(qp)



    w = QWidget()
    
    w.setWindowTitle('G1k - Control Panel')

    label = QLabel(w)
    label.setText("Keyboard Backlight")
    label.move(250,150)
    label.show()

    label2 = QLabel(w)
    label2.setText("Fan Speed")
    label2.move(280,350)
    label2.show()

    # Images
    img1 = QLabel(w)
    pix1 = QPixmap('img1.jpg')
    img1.setPixmap(pix1)
    img1.setScaledContents(True)
    w.resize(pix1.width(), pix1.height())
    img1.show()

    #grid = QGridLayout(w)
    b1= QPushButton("Bright 1")
    b2= QPushButton("Bright 2")
    b3 = QPushButton("Bright 3")
    f1 = QPushButton("Silent")
    f2 = QPushButton("Performance")
    f3 = QPushButton("Turbo")

    b1.setStyleSheet("border-image: url('logo.png');")
    b2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                    "border:1px solid rgb(255, 170, 255);")

    # grid.addWidget(b1,0,0)
    # grid.addWidget(b2,0,1)
    # grid.addWidget(b3,0,2)
    # grid.addWidget(f1,1,0)
    # grid.addWidget(f2,1,1)
    # grid.addWidget(f3,1,2)

    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWidget(cancelButton)

    vbox = QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(hbox)

    # self.setLayout(vbox)

    # self.setGeometry(300, 300, 300, 150)
    

    b1.clicked.connect(call_b1)
    b2.clicked.connect(call_b2)
    b3.clicked.connect(call_b3)


    f1.clicked.connect(call_f1)
    f2.clicked.connect(call_f2)
    f3.clicked.connect(call_f3)

    w.show()
    sys.exit(app.exec_())