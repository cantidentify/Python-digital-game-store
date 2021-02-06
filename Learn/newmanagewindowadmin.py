# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newmanagewindowadmin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime,date

from getdataformanage import getallveget
from savedatatodb import deletevegetableselect,insertvegetable,updatevegetable
from checkforinsertandaddveget import checkNoBlank,checknoduplicate,checklessorzeroprice,checklessorzeroquan,checkNoBlankInUpdate,datanotsameolddata

class Ui_MainWindowManageVeget(object):
    def setupUiManageVeget(self, MainWindow,prewindow,dataadmininput):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 10, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.showinfolist = QtWidgets.QLabel(self.centralwidget)
        self.showinfolist.setGeometry(QtCore.QRect(170, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.showinfolist.setFont(font)
        self.showinfolist.setObjectName("showinfolist")
        self.tablevegetable = QtWidgets.QTableWidget(self.centralwidget)
        self.tablevegetable.setGeometry(QtCore.QRect(30, 120, 418, 441))
        self.tablevegetable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablevegetable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablevegetable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablevegetable.setObjectName("tablevegetable")
        self.tablevegetable.setColumnCount(4)
        self.tablevegetable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablevegetable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablevegetable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablevegetable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablevegetable.setHorizontalHeaderItem(3, item)
        self.deletebtn = QtWidgets.QPushButton(self.centralwidget)
        self.deletebtn.setGeometry(QtCore.QRect(570, 510, 114, 32))
        self.deletebtn.setObjectName("deletebtn")
        self.showselect = QtWidgets.QLabel(self.centralwidget)
        self.showselect.setGeometry(QtCore.QRect(510, 150, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.showselect.setFont(font)
        self.showselect.setObjectName("showselect")
        self.showdelete = QtWidgets.QLabel(self.centralwidget)
        self.showdelete.setGeometry(QtCore.QRect(540, 480, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.showdelete.setFont(font)
        self.showdelete.setObjectName("showdelete")
        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(670, 560, 114, 32))
        self.backbutton.setObjectName("backbutton")
        self.inputname = QtWidgets.QLineEdit(self.centralwidget)
        self.inputname.setGeometry(QtCore.QRect(600, 270, 141, 21))
        self.inputname.setObjectName("inputname")
        self.dateinput = QtWidgets.QDateEdit(self.centralwidget)
        self.dateinput.setGeometry(QtCore.QRect(600, 390, 141, 22))
        self.dateinput.setObjectName("dateinput")
        self.inputprice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.inputprice.setGeometry(QtCore.QRect(600, 310, 141, 22))
        self.inputprice.setObjectName("inputprice")
        self.inputstock = QtWidgets.QSpinBox(self.centralwidget)
        self.inputstock.setGeometry(QtCore.QRect(600, 350, 141, 22))
        self.inputstock.setObjectName("inputstock")
        self.showname = QtWidgets.QLabel(self.centralwidget)
        self.showname.setGeometry(QtCore.QRect(470, 270, 131, 16))
        self.showname.setObjectName("showname")
        self.showprice = QtWidgets.QLabel(self.centralwidget)
        self.showprice.setGeometry(QtCore.QRect(470, 310, 131, 16))
        self.showprice.setObjectName("showprice")
        self.showstock = QtWidgets.QLabel(self.centralwidget)
        self.showstock.setGeometry(QtCore.QRect(470, 350, 131, 16))
        self.showstock.setObjectName("showstock")
        self.showdate = QtWidgets.QLabel(self.centralwidget)
        self.showdate.setGeometry(QtCore.QRect(470, 390, 131, 16))
        self.showdate.setObjectName("showdate")
        self.confirmbtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmbtn.setGeometry(QtCore.QRect(470, 430, 181, 32))
        self.confirmbtn.setObjectName("confirmbtn")
        self.showmanage = QtWidgets.QLabel(self.centralwidget)
        self.showmanage.setGeometry(QtCore.QRect(530, 220, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.showmanage.setFont(font)
        self.showmanage.setObjectName("showmanage")
        self.showbaht = QtWidgets.QLabel(self.centralwidget)
        self.showbaht.setGeometry(QtCore.QRect(750, 310, 41, 16))
        self.showbaht.setObjectName("showbaht")
        self.resetbtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetbtn.setGeometry(QtCore.QRect(660, 430, 114, 32))
        self.resetbtn.setObjectName("resetbtn")
        self.showpiece = QtWidgets.QLabel(self.centralwidget)
        self.showpiece.setGeometry(QtCore.QRect(750, 350, 41, 20))
        self.showpiece.setObjectName("showpiece")
        self.actioncombobox = QtWidgets.QComboBox(self.centralwidget)
        self.actioncombobox.setGeometry(QtCore.QRect(490, 180, 151, 32))
        self.actioncombobox.setObjectName("actioncombobox")
        self.selectbtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectbtn.setGeometry(QtCore.QRect(650, 180, 114, 32))
        self.selectbtn.setObjectName("selectbtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thiswindow = MainWindow
        self.prewindow = prewindow
        self.dataadmininput = dataadmininput
        self.selectaction = "Select Action"

        self.showlistveget()

        self.tablevegetable.clicked.connect(self.showselectitem)
        self.tablevegetable.doubleClicked.connect(self.showselectitem)
        self.resetbtn.clicked.connect(self.resetdatainblock)
        self.deletebtn.clicked.connect(self.deleteselect)
        self.selectbtn.clicked.connect(self.setactiontype)
        self.confirmbtn.clicked.connect(self.checkaction)
        self.backbutton.clicked.connect(self.backtomenu)

        self.actioncombobox.addItems(self.addlistaction())
        self.setblockfordefault()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Organic vegetable order online"))
        self.title.setText(_translate("MainWindow", "Organic vegetable order online"))
        self.showinfolist.setText(_translate("MainWindow", "List Of Vegetable"))
        item = self.tablevegetable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tablevegetable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price (Baht.)"))
        item = self.tablevegetable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tablevegetable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock"))
        self.deletebtn.setText(_translate("MainWindow", "Delete"))
        self.showselect.setText(_translate("MainWindow", "Select Action to Update or Add"))
        self.showdelete.setText(_translate("MainWindow", "Delete Select Vegetable"))
        self.backbutton.setText(_translate("MainWindow", "Back"))
        self.dateinput.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.showname.setText(_translate("MainWindow", "Name Of Vegetable"))
        self.showprice.setText(_translate("MainWindow", "Price Of Vegetable"))
        self.showstock.setText(_translate("MainWindow", "Stock Of Vegetable"))
        self.showdate.setText(_translate("MainWindow", "Date Of Vegetable"))
        self.confirmbtn.setText(_translate("MainWindow", "Manage"))
        self.showmanage.setText(_translate("MainWindow", "Manage Data Vegetable"))
        self.showbaht.setText(_translate("MainWindow", "Baht."))
        self.resetbtn.setText(_translate("MainWindow", "Reset"))
        self.showpiece.setText(_translate("MainWindow", "Pieces"))
        self.selectbtn.setText(_translate("MainWindow", "Select"))

    def addlistaction(self):
        dataaction = ["Select Action","Update","Add"]
        return dataaction

    def backtomenu(self):
        self.thiswindow.hide()
        self.prewindow.show()

    def showlistveget(self):
        dataveget = getallveget()
        listveget = []
        for showdata in dataveget:
            listdata = []
            listdata.append(showdata['name'])
            listdata.append(str(showdata['price']))
            listdata.append(showdata['date'])
            listdata.append(str(showdata['quantity']))
            listveget.append(listdata)

        countitem = 0
        for rowdata in (listveget):
            self.tablevegetable.insertRow(countitem)
            countcol = 0
            for data in (rowdata):
                self.tablevegetable.setItem(countitem,countcol,QtWidgets.QTableWidgetItem((data)))
                countcol = countcol + 1
            countitem = countitem+1

        self.tablevegetable.update()
        self.tablevegetable.repaint()

        if self.tablevegetable.item(0,0) != None:
            self.tablevegetable.selectRow(0)
            if self.selectaction == "Update":
                self.showselectitem()
        else:
            if self.selectaction == "Add":
                self.errorWarShow("Wait!!!","No vegetable in list to show for update!!!\nPlease Add vegetable first")
            else:
                self.errorWarShow("Wait!!!","No vegetable in list to show for update!!!\nPlease Add vegetable from select action to ' Add ' first")

    def setblockforadddata(self):
        self.inputname.setEnabled(True)
        self.inputstock.setEnabled(True)
        self.inputprice.setEnabled(True)
        self.dateinput.setEnabled(True)
        self.confirmbtn.setEnabled(True)
        self.resetbtn.setEnabled(True)

        self.inputname.setReadOnly(False)
        self.dateinput.setReadOnly(True)

        self.confirmbtn.setText("Add")

        self.inputname.clear()
        self.inputstock.setValue(0)
        self.inputprice.setValue(0.00)

        thisdate = date.today()

        self.dateinput.setDate(QtCore.QDate(QtCore.QDate(thisdate)))


    def setblockforupdatedata(self):
        self.inputname.setEnabled(True)
        self.inputstock.setEnabled(True)
        self.inputprice.setEnabled(True)
        self.dateinput.setEnabled(True)
        self.confirmbtn.setEnabled(True)
        self.resetbtn.setEnabled(True)

        self.inputname.setReadOnly(True)
        self.dateinput.setReadOnly(True)

        self.confirmbtn.setText("Update")

        self.showselectitem()


    def setblockfordefault(self):

        thisdate = date.today()

        self.inputname.setEnabled(False)
        self.inputstock.setEnabled(False)
        self.inputprice.setEnabled(False)
        self.dateinput.setEnabled(False)
        self.confirmbtn.setEnabled(False)
        self.resetbtn.setEnabled(False)

        self.inputname.clear()
        self.inputstock.setValue(0)
        self.inputprice.setValue(0.00)
        self.dateinput.setDate(QtCore.QDate(QtCore.QDate(thisdate)))
        self.confirmbtn.setText("Manage")

    def setactiontype(self):
        self.selectaction = self.actioncombobox.currentText()
        if self.selectaction == "Select Action":
            self.setblockfordefault()
        elif self.selectaction == "Update":
            if self.tablevegetable.item(0,0) != None:
                self.setblockforupdatedata()
            else:
                self.selectaction = "Select Action"
                self.actioncombobox.setCurrentIndex(0)
                self.setblockfordefault()
                self.errorWarShow("Wait!!!","No vegetable in list to show for update!!!\nPlease Add vegetable from select action to ' Add ' first")
        else:
            self.setblockforadddata()
        self.inputname.update()
        self.inputprice.update()
        self.inputstock.update()
        self.dateinput.update()
        self.inputname.repaint()


    def showselectitem(self):

        dataitem = []
        for select in self.tablevegetable.selectionModel().selectedIndexes():
            row_select = select.row()
            column_select = select.column()
            dataitem.append(self.tablevegetable.item(row_select,column_select).text())

        nameselect = dataitem[0]
        priceselect = float(dataitem[1])
        dateselect = dataitem[2]
        quantity = int(dataitem[3])

        dateselect = datetime.strptime(dateselect,"%Y-%m-%d").date()

        if self.selectaction == "Update":
            self.dateinput.setDate(QtCore.QDate(QtCore.QDate(dateselect)))
            self.inputname.setText(nameselect)
            self.inputprice.setValue(priceselect)
            self.inputstock.setValue(quantity)

    def resetdatainblock(self):
        if self.selectaction == "Update":
            self.showselectitem()
            self.inputprice.update()
            self.inputstock.update()
            self.inputprice.repaint()
        else:
            self.inputname.clear()
            self.inputprice.setValue(0.00)
            self.inputstock.setValue(0)
            self.inputprice.update()
            self.inputstock.update()
            self.inputprice.repaint()

    def checkaction(self):
        if self.selectaction == "Update":
            self.doupdate()
        else:
            self.doadddata()

    def doupdate(self):

        nameveget = self.inputname.text()
        priceveget = self.inputprice.text()
        quanveget = self.inputstock.text()
        dateinput = self.dateinput.dateTime().toString("yyyy-MM-dd")
        rowselect = int(self.tablevegetable.currentRow())

        if checkNoBlankInUpdate(priceveget,quanveget):
            if datanotsameolddata(nameveget,float(priceveget),dateinput,int(quanveget)):
                if checklessorzeroprice(priceveget):
                    if checklessorzeroquan(quanveget):
                        datatoupdate = {"name":nameveget,"price":float(priceveget),"date":dateinput,
                                           "quantity":int(quanveget),"updatebyadmin":self.dataadmininput[1]}
                        if updatevegetable(datatoupdate):
                            self.sucessShow("Sucess!!!","Update this Vegetable to Vegetable List Sucessful!!!")
                            self.tablevegetable.setRowCount(0)
                            self.showlistveget()
                            self.tablevegetable.update()
                            self.tablevegetable.repaint()
                            self.tablevegetable.selectRow(rowselect)
                            self.showselectitem()
                            self.tablevegetable.repaint()
                        else:
                            self.errorCriShow("Error!!!","Update this vegetable to Vegetable Database Fail!!!")
                            self.resetdatainblock()
                    else:
                        self.errorWarShow("Error!!!","Quantity must have more than 0 Pieces")
                else:
                    self.errorWarShow("Error!!!","Price must have more than 0 Baht.")
            else:
                self.errorWarShow("Wait!!!","Data input to update is same old data!!!\nPlease edit data and click update again")
        else:
            self.errorWarShow("Error!!!","Price or Quantity can't be Blank!!!")


    def doadddata(self):

        nameveget = self.inputname.text()
        priceveget = self.inputprice.text()
        quanveget = self.inputstock.text()
        dateinput = self.dateinput.dateTime().toString("yyyy-MM-dd")

        if checkNoBlank(nameveget,priceveget,quanveget):
            if checklessorzeroprice(priceveget):
                if checklessorzeroquan(quanveget):
                    if checknoduplicate(nameveget,dateinput):
                        datatoinput = {"name":nameveget,"price":float(priceveget),"date":dateinput,
                                       "quantity":int(quanveget),"addbyadmin":self.dataadmininput[1]}
                        if insertvegetable(datatoinput):
                            self.sucessShow("Sucess!!!","Add this Vegetable to Vegetable List Sucessful!!!")
                            self.resetdatainblock()
                            self.tablevegetable.setRowCount(0)
                            self.showlistveget()
                            self.tablevegetable.update()
                            self.tablevegetable.repaint()
                        else:
                            self.errorCriShow("Error!!!","Add this vegetable to Vegetable Database Fail!!!")
                            self.resetdatainblock()
                    else:
                        self.errorCriShow("Error!!!","Have this vegetable in this date already!!!\nYou can manage this vegetable by select action to ' Update '")
                        self.inputname.clear()
                        self.inputprice.setValue(0.00)
                        self.inputstock.setValue(0)
                else:
                    self.errorWarShow("Error!!!","Quantity must have more than 0 Pieces")
            else:
                self.errorWarShow("Error!!!","Price must have more than 0 Baht.")
        else:
            self.errorWarShow("Error!!!","Name or Price or Quantity can't be Blank!!!")

    def deleteselect(self):
        if self.tablevegetable.item(0,0) != None:
            dataitem = []
            for select in self.tablevegetable.selectionModel().selectedIndexes():
                row_select = select.row()
                column_select = select.column()
                dataitem.append(self.tablevegetable.item(row_select,column_select).text())
            self.wardeleteshow("Confirm to delete?","Are you sure to delete this item\n\nVegetable name : {0}\nPrice : {1}\nDate : {2}\nStock left : {3}\n\n".format(dataitem[0],dataitem[1],dataitem[2],dataitem[3]),dataitem)
        else:
            self.errorWarShow("Wait!!!","No vegetable in list to selected for Delete!!!\nPlease Add vegetable from select action to ' Add ' first")

    def wardeleteshow(self,title,message,dataitem):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Warning)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        WarBox.setDefaultButton(QMessageBox.Cancel)
        Ans = WarBox.exec_()

        if Ans == QtWidgets.QMessageBox.Ok:

            if deletevegetableselect(dataitem,self.dataadmininput[1]):
                self.sucessShow("Sucess!!!","Sucessful Delete\n\nVegetable name : {0}\nPrice : {1}"
                                            "\nDate : {2}\nStock left : {3}\n\nFrom System\n\nYou can view log item in LogDeleteVegetable folder".format(dataitem[0],dataitem[1],dataitem[2],dataitem[3]))
                self.tablevegetable.setRowCount(0)
                self.tablevegetable.update()
                self.tablevegetable.repaint()
                self.showlistveget()


                if self.tablevegetable.item(0,0) != None:
                    self.showselectitem()
                else:
                    if self.selectaction == "Update":
                        self.selectaction = "Select Action"
                        self.actioncombobox.setCurrentIndex(0)
                        self.setblockfordefault()

                self.tablevegetable.update()
                self.tablevegetable.repaint()

            else:
                self.errorCriShow("Error!!!","Delete selected vegetable from Database fail!!!")


    def errorWarShow(self,title,message):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Warning)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        WarBox.exec_()

    def sucessShow(self,title,message):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Information)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        WarBox.exec_()

    def errorCriShow(self,title,message):
        CriBox = QtWidgets.QMessageBox()
        CriBox.setIcon(QtWidgets.QMessageBox.Critical)
        CriBox.setWindowTitle(title)
        CriBox.setText(message)
        CriBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        CriBox.exec_()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormManageVeget = QtWidgets.QMainWindow()
    ui = Ui_MainWindowManageVeget()
    ui.setupUiManageVeget(FormManageVeget)
    FormManageVeget.show()
    sys.exit(app.exec())
