# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'store.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UiFile.admin.callTable import callData
from UiFile.user.saveOrder import saveOrder

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, prewindow, username):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 482)
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
        self.ConfirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmBtn.setGeometry(QtCore.QRect(460, 400, 111, 51))
        self.ConfirmBtn.setObjectName("ConfirmBtn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 361, 251))
        self.tableWidget.setMinimumSize(QtCore.QSize(361, 20))
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
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(117)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(46)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(290, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(420, 100, 191, 221))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(94)

        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 330, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.totalprice = QtWidgets.QLineEdit(self.centralwidget)
        self.totalprice.setGeometry(QtCore.QRect(420, 359, 191, 21))
        self.totalprice.setReadOnly(True)
        self.totalprice.setObjectName("totalprice")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(290, 400, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #-----------------------------------------------------
        self.loaddata()
        self.prewindow = prewindow
        self.thiswindow = MainWindow
        self.addBtn.clicked.connect(self.addgame)
        self.cancelBtn.clicked.connect(self.cancelSelected)
        self.totalPriceShow()
        self.ConfirmBtn.clicked.connect(self.buyConfirm)
        self.username =username
        self.backBtn.clicked.connect(self.backToMenu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Game Store"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "List of Games"))
        self.ConfirmBtn.setText(_translate("MainWindow", "Confirm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        self.label_3.setText(_translate("MainWindow", "All selected"))
        self.label_4.setText(_translate("MainWindow", "Total price"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))

    def backToMenu(self):
        self.thiswindow.hide()
        self.prewindow.show()

    def buyConfirm(self):
        count = self.tableWidget_2.rowCount()
        if count > 0:
            self.WarConShow("Order confirm", "Do you wan't to confirm order?")

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
        if ans == 1024:
            gamelist = self.getalldataincart()
            username = self.username
            if saveOrder(gamelist, username):
                while self.tableWidget_2.rowCount() > 0:
                    self.tableWidget_2.removeRow(0)
                print("Success save program")
                self.totalPriceShow()

    def getalldataincart(self):
        numallrow = int(self.tableWidget_2.rowCount())
        numrow = 0
        listdataincart = []
        for rowdata in range(numallrow):
            numcol = 0
            listdemo = []
            for coldata in range(2):
                listdemo.append(self.tableWidget_2.item(numrow, numcol).text())
                numcol = numcol + 1
            listdataincart.append(listdemo)
            numrow = numrow + 1

        return listdataincart

    def totalPriceShow(self):
        rowCount = self.tableWidget_2.rowCount()
        totalPrice = 0
        for row in range(rowCount):
            item = self.tableWidget_2.item(row, 1)
            itemText = item.text()
            totalPrice = totalPrice + int(itemText)
        show = "Total price : {0:,.2f} Baht.".format(totalPrice)
        self.totalprice.setText(show)

    def addgame(self):
        name = self.getSelecedGameName()
        price = self.getSelecedGamePrice()
        if (name is None):
            print("No game selected")
        else:
            selected = [name, price]
            self.selectedGame(selected)
            self.totalPriceShow()

    def cancelSelected(self):
        row = self.getselectedRowIDTable2()
        if row < 0:
            print("No selected game")
        else:
            self.tableWidget_2.removeRow(row)
            self.totalPriceShow()

    def selectedGame(self, game):
        countitem = 0
        self.tableWidget_2.insertRow(countitem)
        countcol = 0
        for data in game:
            self.tableWidget_2.setItem(countitem, countcol, QtWidgets.QTableWidgetItem((data)))
            countcol = countcol + 1

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

    def getselectedRowID(self):
        return self.tableWidget.currentRow()

    def getselectedRowIDTable2(self):
        return self.tableWidget_2.currentRow()

    def getSelecedGameName(self):
        try:
            return self.tableWidget.item(self.getselectedRowID(), 0).text()
        except:
            pass

    def getSelecedGamePrice(self):
        try:
            return self.tableWidget.item(self.getselectedRowID(), 2).text()
        except:
            pass

    def getSelecedGamePriceTable2(self):
        try:
            return self.tableWidget_2.item(self.getselectedRowIDTable2(), 2).text()
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
