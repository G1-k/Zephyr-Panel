import sys
import os
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtLogin = "/home/g1k/zephyr-panel/permission.ui"

Ui_Window, QtBaseClass = uic.loadUiType(qtLogin)

class Login(QtWidgets.QDialog , Ui_Window):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        Ui_Window.__init__(self)
        self.setupUi(self)
        self.buttonLogin.clicked.connect(self.handleLogin)

    def handleLogin(self):
        global passw
        passw = self.textPass.text()
        self.accept()

    
 
qtCreatorFile = "/home/g1k/zephyr-panel/zephyr.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.b4.clicked.connect(lambda: self.call_k(0))
        self.b1.clicked.connect(lambda: self.call_k(1))
        self.b2.clicked.connect(lambda: self.call_k(2))
        self.b3.clicked.connect(lambda: self.call_k(3))
        

        self.f1.clicked.connect(lambda: self.call_f1(2))
        self.f2.clicked.connect(lambda: self.call_f1(0))
        self.f3.clicked.connect(lambda: self.call_f1(1))


    def call_k(self,val):
        os.system("gnome-terminal -- bash -c 'cd && echo {p} | sudo -S -v && sudo ./rogauracore/rogauracore initialize_keyboard  && sudo ./rogauracore/rogauracore brightness {v}'".format(p=passw , v=val))
    

    def call_f1(self,val):
        os.system("gnome-terminal -- bash -c 'cd && echo {p} | sudo -S -v && echo {v} | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy'".format(p=passw , v=val))
        


if __name__ == "__main__":



    appctxt = ApplicationContext()
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MyApp()
        window.show()
        sys.exit(appctxt.app.exec_())