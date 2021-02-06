# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homewinforuser.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
#from getdatahomeuser import checkwithcon,showwithnocheck
#from savedatatodb import savereciepe,saveincome,editveget

class Ui_MainWindowHomeUser(object):
    def setupUiHomeUser(self, MainWindow , previouswindow , datalogin):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listvegetshow = QtWidgets.QLabel(self.centralwidget)
        self.listvegetshow.setGeometry(QtCore.QRect(160, 40, 171, 31))
        self.listvegetshow.setObjectName("listvegetshow")
        self.TotalCost = QtWidgets.QLineEdit(self.centralwidget)
        self.TotalCost.setGeometry(QtCore.QRect(450, 490, 311, 41))
        self.TotalCost.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TotalCost.setFont(font)
        self.TotalCost.setObjectName("TotalCost")
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(10, 10, 114, 32))
        self.backbtn.setObjectName("backbtn")
        self.conbtn = QtWidgets.QPushButton(self.centralwidget)
        self.conbtn.setGeometry(QtCore.QRect(460, 550, 114, 32))
        self.conbtn.setObjectName("conbtn")
        self.bucketlist = QtWidgets.QTableWidget(self.centralwidget)

        self.bucketlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.bucketlist.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.bucketlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.bucketlist.setGeometry(QtCore.QRect(450, 140, 311, 311))
        self.bucketlist.setObjectName("bucketlist")
        self.bucketlist.setColumnCount(5)
        self.bucketlist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bucketlist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bucketlist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bucketlist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bucketlist.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bucketlist.setHorizontalHeaderItem(4, item)
        self.showBuc = QtWidgets.QLabel(self.centralwidget)
        self.showBuc.setGeometry(QtCore.QRect(560, 100, 171, 31))
        self.showBuc.setObjectName("showBuc")
        self.selectdateshow = QtWidgets.QLabel(self.centralwidget)
        self.selectdateshow.setGeometry(QtCore.QRect(450, 40, 221, 31))
        self.selectdateshow.setObjectName("selectdateshow")
        self.vegetablelist = QtWidgets.QTableWidget(self.centralwidget)
        self.vegetablelist.setGeometry(QtCore.QRect(40, 80, 371, 461))

        self.vegetablelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.vegetablelist.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.vegetablelist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.vegetablelist.setObjectName("vegetablelist")
        self.vegetablelist.setColumnCount(5)
        self.vegetablelist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.vegetablelist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vegetablelist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vegetablelist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vegetablelist.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.vegetablelist.setHorizontalHeaderItem(4, item)
        self.showTotal = QtWidgets.QLabel(self.centralwidget)
        self.showTotal.setGeometry(QtCore.QRect(570, 460, 171, 31))
        self.showTotal.setObjectName("showTotal")
        self.listdate = QtWidgets.QComboBox(self.centralwidget)
        self.listdate.setGeometry(QtCore.QRect(450, 70, 171, 32))
        self.listdate.setObjectName("listdate")
        self.datetimenow = QtWidgets.QLineEdit(self.centralwidget)
        self.datetimenow.setGeometry(QtCore.QRect(670, 10, 91, 31))
        self.datetimenow.setReadOnly(True)
        self.datetimenow.setObjectName("datetimenow")
        self.addtocart = QtWidgets.QPushButton(self.centralwidget)
        self.addtocart.setGeometry(QtCore.QRect(160, 550, 114, 32))
        self.addtocart.setObjectName("addtocart")
        self.searchfromselect = QtWidgets.QPushButton(self.centralwidget)
        self.searchfromselect.setGeometry(QtCore.QRect(630, 70, 114, 32))
        self.searchfromselect.setObjectName("searchfromselect")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(640, 550, 114, 32))
        self.clearbtn.setObjectName("clearbtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.searchfromselect.clicked.connect(self.showfromcondi)
        self.backbtn.clicked.connect(self.backtologin)
        self.vegetablelist.doubleClicked.connect(self.getvegetselect)
        self.bucketlist.doubleClicked.connect(self.deletefromcart)
        self.clearbtn.clicked.connect(self.cleardata)
        self.addtocart.clicked.connect(self.addtocartbybtn)
        self.conbtn.clicked.connect(self.contobuy)

        datenow = datetime.datetime.now()
        self.datetimenow.setText(datenow.strftime("%Y-%m-%d"))

        self.listdate.addItems(self.checklistdate(datenow))

        self.showlistveg("",datenow)

        self.TotalCost.setText("0.00 Baht.")

        self.thiswindow = MainWindow
        self.previouswindow = previouswindow
        self.userdata = datalogin

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Organic vegetable order online"))
        self.listvegetshow.setText(_translate("MainWindow", "List Of Vegetable"))
        self.backbtn.setText(_translate("MainWindow", "Back"))
        self.conbtn.setText(_translate("MainWindow", "Confirm"))
        item = self.bucketlist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.bucketlist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price (Baht.)"))
        item = self.bucketlist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.bucketlist.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.bucketlist.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Discount (%)"))
        self.showBuc.setText(_translate("MainWindow", "Your Bucket"))
        self.selectdateshow.setText(_translate("MainWindow", "Please Select Date Of Vegetable"))
        item = self.vegetablelist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.vegetablelist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price (Baht.)"))
        item = self.vegetablelist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.vegetablelist.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.vegetablelist.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Discount (%)"))
        self.showTotal.setText(_translate("MainWindow", "Total Cost"))
        self.addtocart.setText(_translate("MainWindow", "Add to Cart"))
        self.searchfromselect.setText(_translate("MainWindow", "Search"))
        self.clearbtn.setText(_translate("MainWindow", "Clear"))

    def cleardata(self):
        self.WarClearShow("Clear Cart?","Are you sure to clear all your cart?")

    def contobuy(self):
        totalmontopay = self.TotalCost.text()
        totalmontopay = float(totalmontopay[0:-6])
        if totalmontopay == 0.00:
            self.errorWarShow("Error!!!","No item in your Cart!!!")
        else:
            dataallincart = self.getalldataincart()
            allitemtoshow = ""
            numitem = 1
            for iteminrow in dataallincart:
                numcol = 0
                nameitem = ""
                dayitem = ""
                priceitem = 0.00
                quanitem = 0
                disitem = 0
                for itemincol in iteminrow:
                    if numcol == 0:
                        nameitem = itemincol
                    if numcol == 1:
                        priceitem = float(itemincol)
                    if numcol == 2:
                        dayitem = itemincol
                    if numcol == 3:
                        quanitem = int(itemincol)
                    if numcol == 4:
                        disitem = int(itemincol)
                    numcol = numcol + 1
                allitemtoshow = allitemtoshow + "{0}. {1} ({2})\n     {3} Baht.".format(numitem,nameitem,dayitem,priceitem)
                if disitem > 0:
                    allitemtoshow = allitemtoshow + "(Discount {0}%)".format(disitem)
                allitemtoshow = allitemtoshow + " x {0} Pieces.\n     Total = {1} Baht.\n".format(quanitem,((priceitem*quanitem)-((priceitem*quanitem)*(float(disitem)/100))))
                numitem = numitem + 1

            self.WarConShow("Confirm to buy?","Are you sure to buy all item in your cart?\n\nList Item\n\n{0}\nTotal Price = {1} Baht.".format(allitemtoshow,totalmontopay),dataallincart,allitemtoshow,totalmontopay)


    def checklistdate(self,dateinput):
        listdate = []
        datetodelete = 0
        listdate.append("All Date")
        for x in range(7):
            datetoshow = dateinput + datetime.timedelta(datetodelete)
            listdate.append(datetoshow.strftime("%Y-%m-%d"))
            datetodelete = datetodelete-1
        return (listdate)

    def showfromcondi(self):
        dateselect = str(self.listdate.currentText())
        datenow = datetime.datetime.now()
        if(dateselect=="All Date"):
            self.showlistveg("",datenow)
        else:
            self.showlistveg(dateselect,datenow)


    def showlistveg(self,condi,dateinput):

        listdate = []
        datetodelete = 0
        for x in range(7) :
            datetoshow = dateinput + datetime.timedelta(datetodelete)
            listdate.append(datetoshow.strftime("%Y-%m-%d"))
            datetodelete = datetodelete-1

        if condi == "":
            result = showwithnocheck()
        else:
            result = checkwithcon(condi)
        listitem = []
        for showdata in result:
            listdata = []
            listdata.append(showdata['name'])
            listdata.append(str(showdata['price']))
            listdata.append(showdata['date'])
            listdata.append(str(showdata['quantity']))

            checkday = 0
            morethan7day = True
            for day in listdate:
                if day == showdata['date']:
                    morethan7day = False
                    break
                checkday = checkday+1

            if morethan7day == True:
                listdata.append(str(50))
            else:
                listdata.append(str(checkday*5))

            listitem.append(listdata)

        if self.bucketlist.rowCount() != 0:
            editlist = self.editlistveforeshow(listitem)
            self.toshowdata(editlist)
        else:
            self.toshowdata(listitem)

    def toshowdata(self,listitem):
        self.vegetablelist.setRowCount(0)
        countitem = 0
        for rowdata in (listitem):
            self.vegetablelist.insertRow(countitem)
            countcol = 0
            for data in (rowdata):
                self.vegetablelist.setItem(countitem,countcol,QtWidgets.QTableWidgetItem((data)))
                countcol = countcol + 1
            countitem = countitem+1

        if self.vegetablelist.item(0,0) != None:
            self.vegetablelist.selectRow(0)
            self.vegetablelist.update()
            self.vegetablelist.repaint()
        else:
            self.errorWarShow("Wait!!!","No vegetable in list in this date!!!")
            self.vegetablelist.repaint()


    def editlistveforeshow(self,listitem):

        rowcount = str(self.bucketlist.rowCount())
        getquan = 0
        getrow = 0
        getcol = 0
        listdatall = []

        countrowfromvegetlist= 0
        for rangeitem in (range(len(listitem))):
            countduplirow = 0
            for rownum in (range(int(rowcount))):
                checksameuser = False
                checksameday = False
                countduplicol = 0
                for datainlistdb in (listitem[countrowfromvegetlist]):
                    datainlist = self.bucketlist.item(countduplirow,countduplicol).text()
                    if countduplicol == 0:
                        if datainlist==datainlistdb:
                            checksameuser = True
                    if countduplicol == 2:
                        if datainlist==datainlistdb:
                            checksameday = True
                    if countduplicol == 3:

                        datainlistdb = int(datainlistdb)-int(datainlist)

                        getquan = int(datainlistdb)
                        getrow = countrowfromvegetlist
                        getcol = countduplicol

                    countduplicol = countduplicol+1

                if (checksameuser==True) and (checksameday==True):
                    listdata = []
                    listdata.append(getquan)
                    listdata.append(getrow)
                    listdata.append(getcol)
                    listdatall.append(listdata)

                countduplirow = countduplirow+1
            countrowfromvegetlist = countrowfromvegetlist+1

        return (self.changedata(listitem,listdatall))

    def changedata(self,listitem,listdataall):

        for rowdata in listdataall:
            count = 0
            getdata = 0
            getrow = 0
            getcol = 0
            for coldata in rowdata:
                if count == 0:
                    getdata = coldata
                if count == 1:
                    getrow = coldata
                if count == 2:
                    getcol = coldata
                count = count+1
            listitem[getrow][getcol] = str(getdata)
        return (listitem)

    def backtologin(self):
        self.WarBackShow("Want to Back?","Are you sure to back to Menu?")

    def deletefromcart(self):
        selectrow = self.bucketlist.currentRow()
        rowcount = str(self.bucketlist.rowCount())
        numstock = 0
        numrow = 0
        stockempty = False

        listdatatoaddback = []
        for dataincart in range(int(rowcount)):
            if selectrow == numrow:
                getnumdata = 0
                for getdata in range(5):
                    if getnumdata == 3:
                        numstock = int(self.bucketlist.item(selectrow,getnumdata).text())
                        if numstock > 1:
                            numstock = numstock-1
                            self.bucketlist.setItem(selectrow,3,QtWidgets.QTableWidgetItem(str(numstock)))

                        else:
                            numstock = numstock-1
                            stockempty = True

                        listdatatoaddback.append(str(numstock))
                    else:
                        listdatatoaddback.append(self.bucketlist.item(selectrow,getnumdata).text())
                    getnumdata = getnumdata+1
            numrow = numrow+1

        if stockempty == True:
            self.bucketlist.removeRow(self.bucketlist.currentRow())

        listnew = []
        listnew.append(listdatatoaddback)
        self.addbacktolistveg(listnew)

    def addbacktolistveg(self,listdatatoaddback):
        rowcount = str(self.vegetablelist.rowCount())
        checksameuser = False
        checksameday = False
        getquan = 0
        getrow = 0
        getcol = 0
        havedata = False

        countduplirow = 0
        for alldata in range(int(rowcount)):
            countduplicol = 0
            for data in (listdatatoaddback[countduplicol]):
                datainlistback = self.vegetablelist.item(countduplirow,countduplicol).text()
                if countduplicol == 0:
                    if (datainlistback)==data:
                        checksameuser = True
                if countduplicol == 2:
                    if (datainlistback)==data:
                        checksameday = True
                if countduplicol == 3:
                    getquan = int(datainlistback)
                    getrow = countduplirow
                    getcol = countduplicol
                countduplicol = countduplicol+1

            if (checksameuser==True) and (checksameday==True):
                dataforplus = [getrow,getcol,getquan]
                self.addnumbacktoveg(dataforplus)
                havedata = True
                break

            countduplirow = countduplirow+1

        if havedata == False:
            self.showtotalmoney()

    def addnumbacktoveg(self,dataforplus):
        plusquan = int(dataforplus[2])+1
        self.vegetablelist.setItem(dataforplus[0],dataforplus[1],QtWidgets.QTableWidgetItem(str(plusquan)))
        self.showtotalmoney()

    def checksamebeforeadd(self,listselect):
        rowcount = str(self.bucketlist.rowCount())
        checksameuser = False
        checksameday = False
        datasame = False
        getquan = 0
        getrow = 0
        getcol = 0

        countduplirow = 0
        for alldata in range(int(rowcount)):
            countduplicol = 0
            for data in (listselect[countduplicol]):
                datainlist = self.bucketlist.item(countduplirow,countduplicol).text()
                if countduplicol == 0:
                    if (datainlist)==data:
                        checksameuser = True
                if countduplicol == 2:
                    if (datainlist)==data:
                        checksameday = True
                if countduplicol == 3:
                    getquan = int(datainlist)
                    getrow = countduplirow
                    getcol = countduplicol
                countduplicol = countduplicol+1

            if (checksameuser==True) and (checksameday==True):
                dataforplus = [getrow,getcol,getquan]
                self.editcart(dataforplus)
                datasame = True
                break

            countduplirow = countduplirow+1

        return (datasame)

    def editcart(self,dataforplus):
        plusquan = dataforplus[2]+1
        self.bucketlist.setItem(dataforplus[0],dataforplus[1],QtWidgets.QTableWidgetItem(str(plusquan)))

    def editlistveg(self,editdata):
        minusquan = int(editdata[10])-1
        if minusquan >= 0:
            self.vegetablelist.setItem(editdata[6],editdata[7],QtWidgets.QTableWidgetItem(str(minusquan)))

    def addlistcart(self,listselect):
        if (self.checksamebeforeadd(listselect)!=True):
            countitem = 0
            for rowdata in (listselect):
                self.bucketlist.insertRow(countitem)
                countcol = 0
                for data in (rowdata):
                    if countcol==3:
                        self.bucketlist.setItem(countitem,countcol,QtWidgets.QTableWidgetItem(str(1)))
                    else:
                        self.bucketlist.setItem(countitem,countcol,QtWidgets.QTableWidgetItem((data)))
                    countcol = countcol + 1
                countitem = countitem+1
        self.showtotalmoney()

    def getvegetselect(self):
        dataselect = self.vegetablelist.currentRow()
        if(self.vegetablelist.item(dataselect,3).text() == "0"):
            self.errorWarShow("Wait!!!","No have vegetable you select left in stock")
        else:
            listselect = []
            dataitem = []
            dataedit = []
            for select in self.vegetablelist.selectionModel().selectedIndexes():
                row_select = select.row()
                column_select = select.column()
                dataitem.append(self.vegetablelist.item(row_select,column_select).text())
                dataedit.append(row_select)
                dataedit.append(column_select)

            listselect.append(dataitem)

            dataedit.append(dataitem[3])

            if(int(dataitem[3])) > 0:
                self.editlistveg(dataedit)
                self.addlistcart(listselect)


    def showtotalmoney(self):
        totalmoney = 0.00
        rowcountdata = str(self.bucketlist.rowCount())
        countduplirow = 0
        for alldata in range(int(rowcountdata)):
            countduplicol = 0
            totalstock = 0
            totalprice = 0.00
            totaldiscount = 0.00
            summoney = 0
            for data in range(5):
                datainlist = self.bucketlist.item(countduplirow,countduplicol).text()
                if countduplicol == 1:
                    totalprice = float(datainlist)
                if countduplicol == 3:
                    totalstock = int(datainlist)
                if countduplicol == 4:
                    totaldiscount = float(datainlist)
                countduplicol = countduplicol+1
            summoney = ((totalprice*totalstock)-((totalprice*totalstock)*(totaldiscount/100)))
            totalmoney = summoney+totalmoney
            countduplirow = countduplirow+1
        moneyall = "{0:,.2f} Baht.".format(totalmoney)
        self.TotalCost.setText(moneyall)


    def WarBackShow(self,title,message):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Warning)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        WarBox.setDefaultButton(QMessageBox.Cancel)
        Ans = WarBox.exec_()

        if Ans == QtWidgets.QMessageBox.Ok:
            self.thiswindow.hide()
            self.previouswindow.show()

    def WarClearShow(self,title,message):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Warning)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        WarBox.setDefaultButton(QMessageBox.Cancel)
        Ans = WarBox.exec_()

        if Ans == QtWidgets.QMessageBox.Ok:
            self.bucketlist.setRowCount(0)
            self.TotalCost.clear()
            self.TotalCost.setText("0.00 Baht.")
            self.TotalCost.update()
            datenow = datetime.datetime.now()
            self.datetimenow.setText(datenow.strftime("%Y-%m-%d"))
            self.listdate.setCurrentIndex(0)
            self.listdate.update()
            self.showfromcondi()
            self.bucketlist.repaint()

    def addtocartbybtn(self):
        if self.vegetablelist.item(0,0) == None:
            self.errorWarShow("Wait!!!","No vegetable in list to select!!!")
        else:

            self.getvegetselect()

            self.vegetablelist.repaint()
            self.vegetablelist.update()
            self.bucketlist.update()

    def WarConShow(self,title,message,listdataincart,allitemtoshow,totalmontopay):
        WarBox = QtWidgets.QMessageBox()
        WarBox.setIcon(QtWidgets.QMessageBox.Information)
        WarBox.setWindowTitle(title)
        WarBox.setText(message)
        WarBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        WarBox.setDefaultButton(QMessageBox.Cancel)
        Ans = WarBox.exec_()

        if Ans == QtWidgets.QMessageBox.Ok:
            datebuy = self.datetimenow.text()
            timebuy = datetime.datetime.now().strftime("%I:%M:%S %p")

            datareciepe = savereciepe(allitemtoshow,self.userdata,datebuy,timebuy,totalmontopay)

            if datareciepe[0]:
                if saveincome(self.userdata,listdataincart,datebuy,timebuy):
                    if editveget(listdataincart):
                        self.sucessShow("Buy Suceccful","Thank you {0}\n\nYour ReciepeID is : {1} \n\nAt : {2} Date : {3}\n\nTotal Balance is {4:,.2f} Baht.\n\n"
                                        "We will delivered Our vegetable to you in 6 Hours\n\nWe hope you enjoy with our fresh vegetable!!!\n\n"
                                        "Note. You can check status of deliver by menu ' View All Reciepe' "
                                        .format((self.userdata[3]+" "+self.userdata[4]+" "+self.userdata[5]),datareciepe[1],timebuy,datebuy,totalmontopay))
                        self.thiswindow.hide()
                        self.previouswindow.show()
                    else:
                        self.errorWarShow("Error!!!","Edit Database Vegetable Fail!!!")
                else:
                    self.errorWarShow("Error!!!","Save Income to Database Fail!!!")
            else:
                self.errorWarShow("Error!!!","Save Reciepe to Database Fail!!!")



    def getalldataincart(self):

        numallrow = int(self.bucketlist.rowCount())

        numrow = 0

        listdataincart = []
        for rowdata in range(numallrow):
            numcol = 0
            listdemo = []
            for coldata in range(5):
                listdemo.append(self.bucketlist.item(numrow,numcol).text())
                numcol = numcol+1
            listdataincart.append(listdemo)
            numrow = numrow+1

        return listdataincart

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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formuser = QtWidgets.QMainWindow()
    ui = Ui_MainWindowHomeUser()
    ui.setupUiHomeUser(Formuser)
    Formuser.show()
    sys.exit(app.exec())
