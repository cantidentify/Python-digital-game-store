# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu(admin).ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Menu (Admin)"))
        self.storeBtn.setText(_translate("MainWindow", "Store \n"
"Management"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.orderBtn.setText(_translate("MainWindow", "Order \n"
"Management"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
