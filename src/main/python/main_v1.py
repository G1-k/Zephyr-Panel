import sys
import os
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        #self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('OK', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        #layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        # if (self.textName.text() == 'foo' and
        #     self.textPass.text() == 'bar'):
        #     self.accept()
        global passw
        passw = self.textPass.text()
        print(passw)
        self.accept()
        

        # else:
        #     QtWidgets.QMessageBox.warning(
        #         self, 'Error', 'Bad user or password')


 
qtCreatorFile = "/home/g1k/zephyr-panel/zephyr.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow, Login):
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
        #os.system("gnome-terminal -- bash -c 'cd && sudo ./rogauracore/rogauracore initialize_keyboard  && sudo ./rogauracore/rogauracore brightness 1'".format(p=passw))
        #os.system("sudo ./rogauracore/rogauracore initialize_keyboard  && sudo ./rogauracore/rogauracore brightness 1")

    # def call_b2(self):
    #     os.system("sudo ./rogauracore/rogauracore initialize_keyboard  && sudo ./rogauracore/rogauracore brightness 2")

    # def call_b3(self):
    #     os.system("sudo ./rogauracore/rogauracore initialize_keyboard  && sudo ./rogauracore/rogauracore brightness 3")

    # def call_b4(self):
    #     os.system("sudo ./rogauracore/rogauracore initialize_keyboard  && sudo ./rogauracore/rogauracore brightness 0")

    def call_f1(self,val):
        os.system("gnome-terminal -- bash -c 'cd && echo {p} | sudo -S -v && echo {v} | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy'".format(p=passw , v=val))
        #os.system("gnome-terminal -- bash -c 'cd && echo 2 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy; read'")

    # def call_f2(self):
    #     os.system("gnome-terminal -- bash -c 'cd && echo {p} | sudo -S -v && echo 0 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy'".format(p=passw))

    # def call_f3(self):
    #     os.system("gnome-terminal -- bash -c 'cd && echo {p} | sudo -S -v && echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy'".format(p=passw))

    


if __name__ == "__main__":


    # #app = QtWidgets.QApplication(sys.argv)
    # appctxt = ApplicationContext()   
    # window = MyApp()
    # window.show()
    # exit_code = appctxt.app.exec_()
    # sys.exit(exit_code)
    # #sys.exit(app.exec_())

    #app = QtWidgets.QApplication(sys.argv)
    appctxt = ApplicationContext()
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MyApp()
        window.show()
        sys.exit(appctxt.app.exec_())