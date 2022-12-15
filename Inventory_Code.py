import sys
from Inventory_Supervisor import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
import re
from Core.Shoe import Shoe
from Core.ProductList import ProducList
from Core.Attendence import Attendence
from DL.AttendenceCRUD import AttendenceCRUD
from DL.StockOrder_DL import StockOrder_DL
from DL.Inventory import Inventory
from random import randint
from datetime import date
import datetime
from DL.UserCRUD import UserCRUD
import Login_Code


class InventoryMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        inventory=Inventory()
        #inventory.readFromTable()
        self.orderStockDL=StockOrder_DL()
        #self.orderStockDL.loadFromTable()
        self.temp_OrderList=[]
        self.total = 0
        
        #self.prodList=ProducList()

        #self.ShoesDL=Inventory()
        #self.ShoesDL=ProducList(ShoeList, productID)
        self.loginWindow = Login_Code.MainWindow()
        self.attendanceDL = AttendenceCRUD()
        self.ui.btnBuyStock.clicked.connect(lambda: self.OpenPages(0))
        self.ui.btn_Update_Stock.clicked.connect(lambda: self.OpenPages(1))
        self.ui.btn_ViewStock.clicked.connect(lambda: self.OpenPages(2))
        self.ui.btn_AddtoCart.clicked.connect(lambda: self.AddToCart_Stock())
        self.ui.btn_RequestOrder.clicked.connect(lambda: self.orderStockFromCart())
        self.ui.btn_MarkAttendance_2.clicked.connect(lambda: self.mark_attendance())
        self.ui.calendarWidget.clicked.connect(lambda: self.printDate())
        self.ui.lineEdit.setText(str(self.get_presents(self.attendanceDL)))
        self.ui.lineEdit_3.setText(str(self.get_absents(self.attendanceDL)))
        self.show()
    def orderStockFromCart(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M:%S")
        order=ProducList(self.orderStockDL.generateOrderID(),date,self.temp_OrderList)
        self.orderStockDL.Insert_at_Head(order)
        self.emptyTableAndList()
    def emptyTableAndList(self):
        self.ui.Table_BuyCartStock.clearSpans()
        self.temp_OrderList.clear()
    def OpenPages(self,idx):
        self.ui.btn_CheckIn.setEnabled(0)
        self.ui.mainBody.setCurrentIndex(idx)
        self.ui.table_UpdateStockLoad()
    def table_UpdateStockLoad(self):
        if(self.orderStockDL.getDLinklist().data.getStatus()==0):
            pass
    def AddToCart_Stock(self):
        Product_Category=self.ui.cmb_Category.currentText()
        Product_Quantity=self.ui.spb_Quantity.text()
        Product_Size=self.ui.spb_Size.text()
        Product_Color=self.ui.cmb_Color.currentText()
        Product_Price=self.ui.txt_PriceperShoes.text()
        prodID=self.generateProdID()
        self.clearField()
        for i in range(int(Product_Quantity)):
            shoe = Shoe(Product_Category, Product_Price, 0 , Product_Size, 0 , Product_Color, prodID,"men")
            self.temp_OrderList.append(shoe)
        self.loadUpdate_tableWidget()
        
        #ProducList(shoe, prodID)
        #self.ShoesDL.setProduct(Product_Category, shoe)
        QMessageBox.information(self,"ADDED" ,"Product Added")
    def clearField(self):
        self.ui.cmb_Category.clearEditText()
        self.ui.spb_Quantity.cleanText()
        self.ui.spb_Size.cleanText()
        self.ui.cmb_Color.clearEditText()
        self.ui.txt_PriceperShoes.clear()
    def generateProdID(self):
        import random
        return "%0.12d" % random.randint(0,999999999999)

    def loadUpdate_tableWidget(self):
        row=0
        self.ui.Table_BuyCartStock.setRowCount(len(self.temp_OrderList))
        for prod in self.temp_OrderList:

            self.ui.Table_BuyCartStock.setItem(row, 0, QtWidgets.QTableWidgetItem(str(prod.getprodID())))
            self.ui.Table_BuyCartStock.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod.getProductCategory())))
            self.ui.Table_BuyCartStock.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod.getShoeSize())))
            self.ui.Table_BuyCartStock.setItem(row, 3, QtWidgets.QTableWidgetItem(prod.getColor()))
            self.ui.Table_BuyCartStock.setItem(row, 4, QtWidgets.QTableWidgetItem(str(prod.getBuyPrice())))
            row=row+1
    def create_object(self, temp_OrderList):
        order_obj= ProducList(temp_OrderList, "001")
    def get_Object_for_attendance (self) :
        a = self.loginWindow.get_object()
        return a
    def printDate(self):
        qDate = self.ui.calendarWidget.selectedDate()
        date =('{0}-{1}-{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        self.ui.txt_SelectedDate.setText(date)
    def mark_attendance(self) :
        today = date.today()
        selected_date = self.ui.calendarWidget.selectedDate()
        if (today == selected_date) :
            user = self.get_Object_for_attendance()
            att = Attendence(user.userName , user.name)
            att.addInDateTimeList(today)
            self.attendanceDL.addIntoList(att)
        else :
            QMessageBox.warning(self,"Invalid Date" , "Please Select today's Date")
    def get_presents (self,DL) :
        count = 0
        user = self.get_Object_for_attendance()
        for i in DL:
            if (i.userID == user.userName) :
                for j in i.dateTimeList :
                    count = count + 1
        return count
    def get_absents (self, DL):
        presents = 0
        currentday = date.today().day
        presents = self.get_presents(DL)
        absents = currentday - presents
        return absents
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=InventoryMainWindow()
    window.show()
    sys.exit(app.exec_())