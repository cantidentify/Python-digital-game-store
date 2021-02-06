# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_management.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UiFile.admin.callTable import callDataForOrder
from UiFile.admin.approveOrder import approveProcess

class order_management(object):
    def setupUi(self, MainWindow, prewindow , username):
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
        self.ConfirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmBtn.setGeometry(QtCore.QRect(460, 400, 111, 51))
        self.ConfirmBtn.setObjectName("ConfirmBtn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 571, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(141)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(52)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(31)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 60, 97, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #------------------------------------------------
        self.loaddata()
        self.comboBox.currentTextChanged.connect(self.changeChoice)
        uselater = []
        self.ConfirmBtn.clicked.connect(self.approveOrder)
        self.prewindow = prewindow
        self.thiswindow = MainWindow
        self.backBtn.clicked.connect(self.backClick)
        self.username = username

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Order Management"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "Orders List"))
        self.ConfirmBtn.setText(_translate("MainWindow", "Approve"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total balance"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.comboBox.setItemText(0, _translate("MainWindow", "All Order"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Approved"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Waiting"))

    def loaddata(self):
        curr = self.comboBox.currentIndex()
        rs = callDataForOrder(str(curr))
        self.uselater = rs[2]
        try:
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
                print("Have no order right now")
        except Exception as e:
            print(e)

    def changeChoice(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.loaddata()

    def approveOrder(self):
        orderID = self.getSelecedOrderName()
        if orderID is not None and self.getSelecedOrderStatus() != "Approved":
            infoToshow = ""
            for x in self.uselater:
                if x[0] == orderID:
                    infoToshow = x
            message = "Are you sure to approve order ID [{0}]\n" \
                      "Username of order : {1}\n" \
                      "Game list : Have {2} games\n" \
                      "--------------------------------------\n".format(infoToshow[0], infoToshow[1], len(infoToshow[4]))
            gamelist = []
            for x in infoToshow[4]:
                gamelist.append(x)

            for x in gamelist:
                message = message + "" + "{0:15}".format(x[0]) + "" + "{0:10,.2f} Baht.".format(float(x[1])) + "\n"
            message = message + "--------------------------------------\n"
            message = message + "Total price is : {0:,.2f} Baht.".format(float(infoToshow[2]))
            self.WarConShow("Approve confirm", message, orderID, infoToshow, gamelist)
        else:
            print("Please select waiting order!")

    def WarConShow(self, title, message, orderID, infoTosend, gamelist):
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
            print("Approve order {0}".format(orderID))
            if approveProcess(orderID, infoTosend, gamelist, self.username):
                self.refresh()
                self.sucessShow("Order approved", "Order ID : {0}\n"
                                                  "By User   : {1}\n"
                                                  "Approved successfully".format(orderID, infoTosend[1]))

    def sucessShow(self, title, message):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Information)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        WarBox.exec_()

    def getselectedRowID(self):
        return self.tableWidget.currentRow()

    def getSelecedOrderStatus(self):
        try:
            return self.tableWidget.item(self.getselectedRowID(), 3).text()
        except:
            pass

    def getSelecedOrderName(self):
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
    ui = order_management()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
