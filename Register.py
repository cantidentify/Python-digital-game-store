# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

# ---------------------------------------------------
from regisProgram import checkBlank, checkSameUser, checkPassword, checkEmail, saveToDB


class Ui_Register(object):
    def setupUi(self, Register, prewindow):
        Register.setObjectName("Register")
        Register.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(230, 150, 241, 21))
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(150, 350, 111, 51))
        self.cancelBtn.setObjectName("cancelBtn")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 200, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(460, 240, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 260, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(230, 270, 241, 21))
        self.email.setObjectName("email")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.regisBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regisBtn.setGeometry(QtCore.QRect(340, 350, 111, 51))
        self.regisBtn.setObjectName("regisBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 250, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(230, 210, 241, 21))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        Register.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        # ---------------------------------------------------
        self.regisBtn.clicked.connect(self.regisProgram)
        self.cancelBtn.clicked.connect(self.openLoginWindow)
        self.thiswindow = Register
        self.prewindow = prewindow

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.username.setPlaceholderText(_translate("Register", "Username"))
        self.label.setText(_translate("Register", "Register"))
        self.label_3.setText(_translate("Register", "Password"))
        self.cancelBtn.setText(_translate("Register", "Cancel"))
        self.label_10.setText(_translate("Register", "More than \"4\" Character "))
        self.label_12.setText(_translate("Register", "Example."))
        self.label_11.setText(_translate("Register", "xx@xx.xx"))
        self.label_2.setText(_translate("Register", "Username"))
        self.regisBtn.setText(_translate("Register", "Register"))
        self.label_4.setText(_translate("Register", "E-Mail"))
        self.email.setPlaceholderText(_translate("Register", "E-Mail"))
        self.password.setPlaceholderText(_translate("Register", "Password"))

    # ---------------------------------------------------
    def openLoginWindow(self):
        self.thiswindow.hide()
        self.prewindow.show()

    def regisProgram(self):
        user = self.username.text()
        passwor = self.password.text()
        email = self.email.text()
        if checkBlank(user, passwor, email):
            if checkPassword(passwor):
                if checkEmail(email):
                    if checkSameUser(user, email):
                        saveToDB(user, passwor, email)
                        print("Register Success")
                        self.openLoginWindow()
                    else:
                        print("Its same user")
                else:
                    print("Wrong Email Format.")
            else:
                print("Please fill password more than 4 char.")
        else:
            print("Please fill data.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
