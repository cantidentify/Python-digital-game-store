# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifyform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.admin.managementProgram import callFromName, updateGame

class Ui_modifyform(object):
    def setupUi(self, modifyform, nameToModify):
        modifyform.setObjectName("modifyform")
        modifyform.resize(416, 480)
        self.centralwidget = QtWidgets.QWidget(modifyform)
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
        self.nameform.setReadOnly(True)
        self.priceform = QtWidgets.QLineEdit(self.Detail)
        self.priceform.setGeometry(QtCore.QRect(10, 230, 311, 21))
        self.priceform.setObjectName("priceform")
        self.descripform = QtWidgets.QTextEdit(self.Detail)
        self.descripform.setGeometry(QtCore.QRect(10, 130, 301, 61))
        self.descripform.setObjectName("descripform")
        self.label_6 = QtWidgets.QLabel(self.Detail)
        self.label_6.setGeometry(QtCore.QRect(110, 10, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.gamenow = QtWidgets.QLineEdit(self.Detail)
        self.gamenow.setGeometry(QtCore.QRect(230, 20, 91, 21))
        self.gamenow.setReadOnly(True)
        self.gamenow.setPlaceholderText("")
        self.gamenow.setObjectName("gamenow")
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
        modifyform.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(modifyform)
        self.statusbar.setObjectName("statusbar")
        modifyform.setStatusBar(self.statusbar)

        self.retranslateUi(modifyform)
        QtCore.QMetaObject.connectSlotsByName(modifyform)
        #------------------------------------------------
        self.ConfirmBtn.clicked.connect(self.confirm)
        self.backBtn.clicked.connect(self.back)
        self.nameToModify = nameToModify
        self.settext()
        self.thiswindow = modifyform

    def retranslateUi(self, modifyform):
        _translate = QtCore.QCoreApplication.translate
        modifyform.setWindowTitle(_translate("modifyform", "MainWindow"))
        self.ConfirmBtn.setText(_translate("modifyform", "Confirm"))
        self.backBtn.setText(_translate("modifyform", "Back"))
        self.Detail.setTitle(_translate("modifyform", "Game Detail"))
        self.label_5.setText(_translate("modifyform", "Price"))
        self.label_4.setText(_translate("modifyform", "Description"))
        self.label_3.setText(_translate("modifyform", "Name"))
        self.nameform.setPlaceholderText(_translate("modifyform", "Name"))
        self.priceform.setPlaceholderText(_translate("modifyform", "Price"))
        self.descripform.setPlaceholderText(_translate("modifyform", "Description"))
        self.label_6.setText(_translate("modifyform", "Now modify :  "))
        self.label_2.setText(_translate("modifyform", "Modify Game"))

    def back(self):
        self.thiswindow.hide()

    def getData(self):
        name = self.nameToModify
        return callFromName(name)

    def settext(self):
        name = self.nameToModify
        self.gamenow.setText(name)
        data = self.getData()
        self.nameform.setText(data["name"])
        self.descripform.setText(data["des"])
        self.priceform.setText(data["price"])

    def confirm(self):
        nameid = self.nameToModify
        getdesc = self.descripform.toPlainText()
        getprice = self.priceform.text()
        count = updateGame(nameid, getdesc, getprice)
        if count > 0:
            print("Update game {0} complete".format(nameid))
            self.thiswindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modifyform = QtWidgets.QMainWindow()
    ui = Ui_modifyform()
    ui.setupUi(modifyform)
    modifyform.show()
    sys.exit(app.exec_())
