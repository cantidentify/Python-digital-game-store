# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# ---------------------------------------------------
from bin.checkFormat import checkBlank


class Ui_Register(object):
    def setupUi(self, Register, prewindow):
        Register.setObjectName("Register")
        Register.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.day = QtWidgets.QLineEdit(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(230, 320, 41, 21))
        self.day.setObjectName("day")
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
        self.cancelBtn.setGeometry(QtCore.QRect(160, 400, 111, 51))
        self.cancelBtn.setObjectName("cancelBtn")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 200, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(460, 240, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.year = QtWidgets.QLineEdit(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(350, 320, 41, 21))
        self.year.setObjectName("year")
        self.month = QtWidgets.QLineEdit(self.centralwidget)
        self.month.setGeometry(QtCore.QRect(290, 320, 41, 21))
        self.month.setObjectName("month")
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
        self.regisBtn.setGeometry(QtCore.QRect(350, 400, 111, 51))
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
        self.password.setObjectName("password")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 300, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 340, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        Register.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)
        # ---------------------------------------------------
        self.regisBtn.clicked.connect(self.regisProgram)
        # self.cancelBtn.clicked.connect(self.cancelBtn)
        # self.thiswindow = Register
        # self.prewindow = prewindow

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.label.setText(_translate("Register", "Register"))
        self.label_3.setText(_translate("Register", "Password"))
        self.cancelBtn.setText(_translate("Register", "Cancel"))
        self.label_10.setText(_translate("Register", "More than \"4\" Character "))
        self.label_7.setText(_translate("Register", "Day"))
        self.label_12.setText(_translate("Register", "Example."))
        self.label_11.setText(_translate("Register", "xx@xx.xx"))
        self.label_2.setText(_translate("Register", "Username"))
        self.regisBtn.setText(_translate("Register", "Register"))
        self.label_4.setText(_translate("Register", "E-Mail"))
        self.label_9.setText(_translate("Register", "Year"))
        self.label_5.setText(_translate("Register", "Birth date"))
        self.label_8.setText(_translate("Register", "Month"))

    # ---------------------------------------------------
    def openLoginWindow(self):
        print()
        # self.thiswindow.hide()
        # self.prewindow.show()

    def regisProgram(self):
        user = self.username.text()
        passwor = self.password.text()
        email = self.email.text()
        day = self.day.text()
        month = self.month.text()
        year = self.year.text()
        if checkBlank(user, passwor, email, day, month, year):
            print()
        else:
            print("Please input data")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
