# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'store_managemnet.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.admin.callTable import callData
from UiFile.admin.addform import Ui_addform
from UiFile.admin.managementProgram import deleteProgram
from UiFile.admin.modifyform import Ui_modifyform
from PyQt5.QtWidgets import QMessageBox

class store_management(object):
    def setupUi(self, MainWindow, prewindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
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
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(40, 400, 111, 51))
        self.backBtn.setObjectName("backBtn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 60, 120, 31))
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

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 361, 291))
        self.tableWidget.setMinimumSize(QtCore.QSize(361, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(7)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(117)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(46)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(460, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.modifyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.modifyBtn.setGeometry(QtCore.QRect(460, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.modifyBtn.setFont(font)
        self.modifyBtn.setObjectName("modifyBtn")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(460, 300, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName("delBtn")
        self.refreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.refreshBtn.setGeometry(QtCore.QRect(330, 390, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.refreshBtn.setFont(font)
        self.refreshBtn.setObjectName("refreshBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #------------------------------------------------
        self.loaddata()
        self.addBtn.clicked.connect(self.add)
        self.refreshBtn.clicked.connect(self.refresh)
        self.modifyBtn.clicked.connect(self.modify)
        self.delBtn.clicked.connect(self.delete)
        self.prewindow = prewindow
        self.thiswindow = MainWindow
        self.backBtn.clicked.connect(self.backClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Store Management"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "List of Games"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.modifyBtn.setText(_translate("MainWindow", "Modify"))
        self.delBtn.setText(_translate("MainWindow", "Delete"))
        self.refreshBtn.setText(_translate("MainWindow", "Refresh"))

    def loaddata(self):
        try:
            rs = callData()
            if rs[1] != 0:
                data = rs[0]
                countitem = 0
                for rowdata in data:
                    self.tableWidget.insertRow(countitem)
                    countcol = 0
                    for data in rowdata:
                        self.tableWidget.setItem(countitem, countcol, QtWidgets.QTableWidgetItem((data)))
                        countcol = countcol + 1
                    countitem = countitem + 1
            else:
                print("No game in store")
        except Exception as e:
            print(e)

    def add(self):
        self.windows = QtWidgets.QMainWindow()
        self.ui = Ui_addform()
        self.ui.setupUi(self.windows)
        self.windows.show()

    def modify(self):
        nameToModify = self.getSelecedGameName()
        if nameToModify is not None:
            self.windows = QtWidgets.QMainWindow()
            self.ui = Ui_modifyform()
            self.ui.setupUi(self.windows, nameToModify)
            self.windows.show()
        else:
            pass


    def delete(self):
        nameTodelete = self.getSelecedGameName()
        if (self.WarConShow("Confirm Deletion", "Are you sure to delete game [{0}]?".format(nameTodelete))) == 1024:
            if deleteProgram(nameTodelete):
                print("{0} is deleted".format(nameTodelete))
                self.refresh()

    def WarConShow(self, title, message):
        #4194304
        #1024
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Information)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        WarBox.setDefaultButton(QMessageBox.Cancel)
        ans = WarBox.exec_()
        return ans

    def getselectedRowID(self):
        return self.tableWidget.currentRow()

    def getSelecedGameName(self):
        try:
            return self.tableWidget.item(self.getselectedRowID(), 0).text()
        except:
            pass

    def refresh(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.loaddata()

    def backClick(self):
        self.thiswindow.hide()
        self.prewindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = store_management()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
