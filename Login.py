# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Register import Ui_Register
from loginProgram import login
from UiFile.user.menu import Ui_usermenu
from UiFile.admin.menu import Ui_adminmenu

class Ui_MainWindow(object):
    def setupUiLogin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 350, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 229, 261, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 170, 261, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ---------------------------------------------------
        self.pushButton.clicked.connect(self.loginBtn)
        self.pushButton_2.clicked.connect(self.registerBtn)

        self.thiswindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Digital Game Store"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Username"))

    def loginBtn(self):
        user = self.lineEdit_3.text()
        passwor = self.lineEdit_2.text()
        ans = login(user, passwor)
        if ans[0]:
            if ans[1] == "1":
                self.clearLine()
                print("Login to admin")
                self.windows = QtWidgets.QMainWindow()
                self.ui = Ui_adminmenu()
                self.ui.setupUi(self.windows, self.thiswindow, user)
                self.windows.show()
                self.thiswindow.hide()
            else:
                self.clearLine()
                print("Login to user")
                self.windows = QtWidgets.QMainWindow()
                self.ui = Ui_usermenu()
                self.ui.setupUi(self.windows, self.thiswindow, user)
                self.windows.show()
                self.thiswindow.hide()
        else:
            print("Login Fail")

    def registerBtn(self):
        self.windows = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.windows, self.thiswindow)
        self.windows.show()
        self.thiswindow.hide()

    def openLoginWindow(self):
        self.windows = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.windows, self.thiswindow)
        self.windows.show()
        self.thiswindow.hide()

    def clearLine(self):
        self.lineEdit_3.clear()
        self.lineEdit_2.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiLogin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
