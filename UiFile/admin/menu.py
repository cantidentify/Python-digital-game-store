# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.admin.order_management import order_management
from UiFile.admin.store_managemnet import store_management


class Ui_adminmenu(object):
    def setupUi(self, adminmenu, prewindow, username):
        adminmenu.setObjectName("adminmenu")
        adminmenu.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(adminmenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.orderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orderBtn.setGeometry(QtCore.QRect(350, 180, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.orderBtn.setFont(font)
        self.orderBtn.setObjectName("orderBtn")
        adminmenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminmenu)
        self.statusbar.setObjectName("statusbar")
        adminmenu.setStatusBar(self.statusbar)

        self.retranslateUi(adminmenu)
        QtCore.QMetaObject.connectSlotsByName(adminmenu)
        #---------------------------------
        self.backBtn.clicked.connect(self.backClick)
        self.prewindow = prewindow
        self.thiswindow = adminmenu
        self.storeBtn.clicked.connect(self.store)
        self.orderBtn.clicked.connect(self.order)
        self.username = username

    def retranslateUi(self, adminmenu):
        _translate = QtCore.QCoreApplication.translate
        adminmenu.setWindowTitle(_translate("adminmenu", "MainWindow"))
        self.label.setText(_translate("adminmenu", "Menu (Admin)"))
        self.storeBtn.setText(_translate("adminmenu", "Store \n"
"Management"))
        self.backBtn.setText(_translate("adminmenu", "Back"))
        self.orderBtn.setText(_translate("adminmenu", "Order \n"
"Management"))

    def order(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = order_management()
        self.ui.setupUi(self.window, self.thiswindow, self.username)
        self.window.show()
        self.thiswindow.hide()

    def store(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = store_management()
        self.ui.setupUi(self.window, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def backClick(self):
        self.thiswindow.hide()
        self.prewindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminmenu = QtWidgets.QMainWindow()
    ui = Ui_adminmenu()
    ui.setupUi(adminmenu)
    adminmenu.show()
    sys.exit(app.exec_())
