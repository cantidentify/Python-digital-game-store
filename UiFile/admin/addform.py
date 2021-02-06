# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.admin.addGame import checkSameName, addGame, checkPrice
from regisProgram import checkBlank


class Ui_addform(object):
    def setupUi(self, addform):
        addform.setObjectName("addform")
        addform.resize(416, 480)
        self.centralwidget = QtWidgets.QWidget(addform)
        self.centralwidget.setObjectName("centralwidget")
        self.ConfirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmBtn.setGeometry(QtCore.QRect(270, 400, 111, 51))
        self.ConfirmBtn.setObjectName("ConfirmBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(40, 400, 111, 51))
        self.backBtn.setObjectName("backBtn")
        self.Detail = QtWidgets.QGroupBox(self.centralwidget)
        self.Detail.setGeometry(QtCore.QRect(40, 60, 331, 291))
        self.Detail.setObjectName("Detail")
        self.label_5 = QtWidgets.QLabel(self.Detail)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.Detail)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.Detail)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.nameform = QtWidgets.QLineEdit(self.Detail)
        self.nameform.setGeometry(QtCore.QRect(10, 60, 311, 21))
        self.nameform.setObjectName("nameform")
        self.priceform = QtWidgets.QLineEdit(self.Detail)
        self.priceform.setGeometry(QtCore.QRect(10, 230, 311, 21))
        self.priceform.setObjectName("priceform")
        self.descripform = QtWidgets.QTextEdit(self.Detail)
        self.descripform.setGeometry(QtCore.QRect(10, 130, 301, 61))
        self.descripform.setObjectName("descripform")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 10, 120, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        addform.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addform)
        self.statusbar.setObjectName("statusbar")
        addform.setStatusBar(self.statusbar)

        self.retranslateUi(addform)
        QtCore.QMetaObject.connectSlotsByName(addform)

        #--------------------------------------------------
        self.ConfirmBtn.clicked.connect(self.addGame)
        self.thiswindow = addform

    def retranslateUi(self, addform):
        _translate = QtCore.QCoreApplication.translate
        addform.setWindowTitle(_translate("addform", "MainWindow"))
        self.ConfirmBtn.setText(_translate("addform", "Confirm"))
        self.backBtn.setText(_translate("addform", "Back"))
        self.Detail.setTitle(_translate("addform", "Game Detail"))
        self.label_5.setText(_translate("addform", "Price"))
        self.label_4.setText(_translate("addform", "Description"))
        self.label_3.setText(_translate("addform", "Name"))
        self.nameform.setPlaceholderText(_translate("addform", "Name"))
        self.priceform.setPlaceholderText(_translate("addform", "Price"))
        self.descripform.setPlaceholderText(_translate("addform", "Description"))
        self.label_2.setText(_translate("addform", "Add game"))

    def addGame(self):
        name = self.nameform.text()
        des = self.descripform.toPlainText()
        price = self.priceform.text()
        try:
            if checkBlank(name, des, price):
                if checkSameName(name):
                    if checkPrice(price):
                        if addGame(name, des, price):
                            print("Add game successfully. Please click refresh button")
                    else:
                        print("Please fill the price correctly")
                else:
                    print("Same game name")
            else:
                print("Blank input")
        except Exception as e:
            print(e)
        self.nameform.clear()
        self.descripform.clear()
        self.priceform.clear()
        self.thiswindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addform = QtWidgets.QMainWindow()
    ui = Ui_addform()
    ui.setupUi(addform)
    addform.show()
    sys.exit(app.exec_())
