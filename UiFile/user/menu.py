# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.user.store import Ui_MainWindow as store
from UiFile.user.order import order

class Ui_usermenu(object):
    def setupUi(self, usermenu, prewindow, username):
        usermenu.setObjectName("usermenu")
        usermenu.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(usermenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.orderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orderBtn.setGeometry(QtCore.QRect(370, 180, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.orderBtn.setFont(font)
        self.orderBtn.setObjectName("orderBtn")
        self.storeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.storeBtn.setGeometry(QtCore.QRect(160, 180, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.storeBtn.setFont(font)
        self.storeBtn.setObjectName("storeBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(260, 340, 111, 51))
        self.backBtn.setObjectName("backBtn")
        usermenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(usermenu)
        self.statusbar.setObjectName("statusbar")
        usermenu.setStatusBar(self.statusbar)

        self.retranslateUi(usermenu)
        QtCore.QMetaObject.connectSlotsByName(usermenu)
        #--------------------------------------------
        self.username = username
        self.backBtn.clicked.connect(self.backClick)
        self.prewindow = prewindow
        self.thiswindow = usermenu
        self.storeBtn.clicked.connect(self.store)
        self.orderBtn.clicked.connect(self.order)


    def retranslateUi(self, usermenu):
        _translate = QtCore.QCoreApplication.translate
        usermenu.setWindowTitle(_translate("usermenu", "MainWindow"))
        self.label.setText(_translate("usermenu", "Menu (User)"))
        self.orderBtn.setText(_translate("usermenu", "Order"))
        self.storeBtn.setText(_translate("usermenu", "Store"))
        self.backBtn.setText(_translate("usermenu", "Back"))

    def backClick(self):
        self.thiswindow.hide()
        self.prewindow.show()

    def store(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = store()
        self.ui.setupUi(self.window, self.thiswindow, self.username)
        self.window.show()
        self.thiswindow.hide()

    def order(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = order()
        self.ui.setupUi(self.window, self.thiswindow, self.username)
        self.window.show()
        self.thiswindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usermenu = QtWidgets.QMainWindow()
    ui = Ui_usermenu()
    ui.setupUi(usermenu)
    usermenu.show()
    sys.exit(app.exec_())
