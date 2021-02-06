# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.admin.addGame import checkBlank, checkSameName, addGame


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 480)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(130, 10, 120, 31))
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
        self.Detail = QtWidgets.QGroupBox(Dialog)
        self.Detail.setGeometry(QtCore.QRect(30, 60, 331, 291))
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
        self.name = QtWidgets.QLineEdit(self.Detail)
        self.name.setGeometry(QtCore.QRect(10, 60, 311, 21))
        self.name.setObjectName("name")
        self.price = QtWidgets.QLineEdit(self.Detail)
        self.price.setGeometry(QtCore.QRect(10, 230, 311, 21))
        self.price.setObjectName("price")
        self.descrip = QtWidgets.QTextEdit(self.Detail)
        self.descrip.setGeometry(QtCore.QRect(10, 130, 301, 61))
        self.descrip.setObjectName("descrip")
        self.backBtn = QtWidgets.QPushButton(Dialog)
        self.backBtn.setGeometry(QtCore.QRect(30, 410, 111, 51))
        self.backBtn.setObjectName("backBtn")
        self.ConfirmBtn = QtWidgets.QPushButton(Dialog)
        self.ConfirmBtn.setGeometry(QtCore.QRect(260, 410, 111, 51))
        self.ConfirmBtn.setObjectName("ConfirmBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #-----------------------------------------------
        self.backBtn.clicked.connect()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Add game"))
        self.Detail.setTitle(_translate("Dialog", "Game Detail"))
        self.label_5.setText(_translate("Dialog", "Price"))
        self.label_4.setText(_translate("Dialog", "Description"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.name.setPlaceholderText(_translate("Dialog", "Name"))
        self.price.setPlaceholderText(_translate("Dialog", "Price"))
        self.descrip.setPlaceholderText(_translate("Dialog", "Description"))
        self.backBtn.setText(_translate("Dialog", "Back"))
        self.ConfirmBtn.setText(_translate("Dialog", "Confirm"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
