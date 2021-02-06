# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UiFile.user.callTable import callData

class order(object):
    def setupUi(self, MainWindow, prewindow, username):
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
        self.orderdetail = QtWidgets.QLineEdit(self.centralwidget)
        self.orderdetail.setGeometry(QtCore.QRect(20, 350, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orderdetail.setFont(font)
        self.orderdetail.setReadOnly(True)
        self.orderdetail.setObjectName("orderdetail")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 601, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(298)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.checkDetail = QtWidgets.QPushButton(self.centralwidget)
        self.checkDetail.setGeometry(QtCore.QRect(480, 400, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkDetail.setFont(font)
        self.checkDetail.setObjectName("checkDetail")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #-------------------------------------------------
        self.username = username
        self.thiswindow = MainWindow
        self.prewindow = prewindow
        self.loadData()
        self.checkDetail.clicked.connect(self.showDetail)
        self.backBtn.clicked.connect(self.backClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Order Detail"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "Orders List"))
        self.orderdetail.setText(_translate("MainWindow", "Order Waiting for Payment : Total"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total Price"))
        self.checkDetail.setText(_translate("MainWindow", "Check detail"))

    def loadData(self):
        try:
            rs = callData(self.username)
            if rs[1] != 0:
                self.uselater = rs[2]
                data = rs[0]
                countitem = 0
                for rowdata in data:
                    self.tableWidget.insertRow(countitem)
                    countcol = 0
                    for data in rowdata:
                        self.tableWidget.setItem(countitem, countcol, QtWidgets.QTableWidgetItem((data)))
                        countcol = countcol + 1
                    countitem = countitem + 1
                self.totalPrice()
            else:
                print("No order")
        except Exception as e:
            print(e)

    def showDetail(self):
        orderID = self.getSelecedOrderName()
        if orderID is not None:
            infoToshow = ""
            for x in self.uselater:
                if x[0] == orderID:
                    infoToshow = x
            message = "Detail for order ID : [{0}]\n" \
                      "This order have {1} games\n" \
                      "--------------------------------------\n".format(orderID, len(infoToshow[2]))
            gamelist = []
            for x in infoToshow[2]:
                gamelist.append(x)
            count = 1
            for x in gamelist:
                message = message + "{0}) {1:10} for {2:15,.2f} Baht.\n".format(count, x[0], float(x[1]))
                count = count + 1
            message = message + "--------------------------------------\n"
            message = message + "Total price is : {0:,.2f} Baht.".format(float(infoToshow[1]))
            self.sucessShow("Show order detail", message)

    def sucessShow(self, title, message):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Information)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        WarBox.exec_()

    def totalPrice(self):
        totalprice = 0
        for x in self.uselater:
            totalprice = totalprice + float(x[1])
        self.orderdetail.setText("Order Waiting for Payment : Total {0:10} {1:20,.2f} Baht.".format("", totalprice))

    def getselectedRowID(self):
        return self.tableWidget.currentRow()

    def getSelecedOrderName(self):
        try:
            return self.tableWidget.item(self.getselectedRowID(), 0).text()
        except:
            pass

    def backClick(self):
        self.thiswindow.hide()
        self.prewindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = order()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
