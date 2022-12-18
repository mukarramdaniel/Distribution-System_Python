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
from Core.Attendence import Attendence
from DL.AttendenceCRUD import AttendenceCRUD
from Core.ProductList import ProducList
from DL.StockOrder_DL import StockOrder_DL
from DL.Inventory import Inventory
from random import randint
from DL.UserCRUD import UserCRUD
#import Login_Code
from datetime import datetime,date



class InventoryMainWindow(QMainWindow):
    #def __init__(self,parent=None):
    def __init__(self,user):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        self.inventory=Inventory()
        #self.inventory.readFromTable()
        self.orderStockDL=StockOrder_DL()
        #self.orderStockDL.loadFromTable()
        self.temp_OrderList=[]
        self.total = 0
        self.row_cart=[]    #esy database mai store bhe krvana ha abhi
        self.attendanceDL = AttendenceCRUD()
        #self.prodList=ProducList()

        #self.ShoesDL=Inventory()
        #self.ShoesDL=ProducList(ShoeList, productID)
        self.ui.btnBuyStock.clicked.connect(lambda: self.OpenPages(0))
        self.ui.btn_Update_Stock.clicked.connect(lambda: self.OpenPages(1))
        self.ui.btn_ViewStock.clicked.connect(lambda: self.OpenPageViewStock(2))
        self.ui.btn_AddtoCart.clicked.connect(lambda: self.AddToCart_Stock())
        self.ui.btn_RequestOrder.clicked.connect(lambda: self.orderStockFromCart())
        self.ui.btn_CheckIn.clicked.connect(lambda: self.checkInStock())
        self.ui.btn_MarkAttendance_2.clicked.connect(lambda: self.mark_attendance())
        self.ui.calendarWidget.clicked.connect(lambda: self.printDate())
        self.ui.lineEdit.setText(str(self.get_presents(self.attendanceDL)))
        self.ui.lineEdit_3.setText(str(self.get_absents(self.attendanceDL)))
        self.show()
    def checkInStock(self):
        self.ui.table_UpdateStock.clearContents()
      
        DlinkList=self.orderStockDL.getDLinklist()
        while(DlinkList!=None):
            if(DlinkList.data.getStatus()==1):
                for prod in DlinkList.data.getShoeList():
                    self.inventory.setProduct(prod.getProductCategory(),prod)
                DlinkList.data.setStatus(2)
            DlinkList=DlinkList.next
        

    def orderStockFromCart(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M:%S")
        order=ProducList(self.orderStockDL.generateOrderID(),date,self.temp_OrderList,0)
        self.orderStockDL.Insert(order)
        self.row_cart.clear()
        self.emptyTableAndList()
        if(len(self.row_cart)==0):
            self.ui.btn_RequestOrder.setEnabled(0)
        else:
            self.ui.btn_RequestOrder.setEnabled(1)
    def emptyTableAndList(self):
        self.ui.Table_BuyCartStock.clearContents()
        self.temp_OrderList.clear()
    def OpenPages(self,idx):
        
       
        self.ui.mainBody.setCurrentIndex(idx)
        self.table_CheckInLoad()
    def OpenPageViewStock(self,idx):
        self.ui.mainBody.setCurrentIndex(idx)
        self.table_ViewStockLoad()
    def table_ViewStockLoad(self):
        row=0
        n=self.calculateRow()
        if(n<10):
            self.ui.table_ViewStock.setRowCount(10)
        else:
            self.ui.table_ViewStock.setRowCount(n)
        
        for bucket in (self.inventory.getInventoryStock()):
            for prod in bucket:
                if(prod!=None):
                    self.ui.table_ViewStock.setItem(row, 0, QtWidgets.QTableWidgetItem(str(prod[1].getprodID())))
                    self.ui.table_ViewStock.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod[1].getProductCategory())))
                    self.ui.table_ViewStock.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod[1].getBuyPrice())))
                    if(prod[1].getSellPrice()==0):
                        self.ui.table_ViewStock.setItem(row, 3, QtWidgets.QTableWidgetItem("None"))
                    else:
                        self.ui.table_ViewStock.setItem(row, 3, QtWidgets.QTableWidgetItem(str(prod[1].getSellPrice())))
                           
                    
                    
                    
                    row +=1
                    
    def calculateRow(self):
        stockCount =0
        for i in self.inventory.getInventoryStock():
            for j in i:
                if(j!=None):
                    stockCount +=1
        return stockCount
    def table_CheckInLoad(self):
        
        row=0
        DlinkList=self.orderStockDL.getDLinklist()
        while(DlinkList!=None):
            if(DlinkList.data.getStatus()==1):
                # for prod in DlinkList.data.getShoeList():
                #     self.ui.table_CheckInStockLoad.setItem(row, 0, QtWidgets.QTableWidgetItem(str(prod.getProductCategory())))
                #     self.ui.table_CheckInStockLoad.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod.getColor())))
                #     self.ui.table_CheckInStockLoad.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod.getBuyPrice())))
                #     self.ui.table_CheckInStockLoad.setItem(row, 3, QtWidgets.QTableWidgetItem(str('Received')))
                #     self.ui.table_CheckInStockLoad.setRowCount(row)
                self.ui.table_UpdateStock.setItem(row, 0, QtWidgets.QTableWidgetItem(str(DlinkList.data.getOrderID())))
                self.ui.table_UpdateStock.setItem(row, 1, QtWidgets.QTableWidgetItem(str(DlinkList.data.date)))
                self.ui.table_UpdateStock.setItem(row, 2, QtWidgets.QTableWidgetItem(str('Received')))
                row +=1
                    
            DlinkList=DlinkList.next
                
                
    def AddToCart_Stock(self):
        Product_Category=self.ui.cmb_Category.currentText()
        Product_Quantity=self.ui.spb_Quantity.text()
        Product_Size=self.ui.spb_Size.text()
        Product_Color=self.ui.cmb_Color.currentText()
        Product_Price=self.ui.txt_PriceperShoes.text()
        t_price=0
        self.row_cart.append((Product_Category,Product_Quantity,Product_Size,Product_Color,Product_Price,t_price))
        prodID=self.generateProdID()
        self.clearField()
        for i in range(int(Product_Quantity)):
            shoe = Shoe(Product_Category, Product_Price, 0 , Product_Size, 0 , Product_Color, prodID,"men")
            t_price +=int(Product_Price)
            self.temp_OrderList.append(shoe)
        self.loadUpdate_tableWidget(t_price)
        
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

    def loadUpdate_tableWidget(self,t_price):
        row=0
        self.ui.Table_BuyCartStock.setRowCount(len(self.row_cart))
        for prod in self.row_cart:
            self.ui.Table_BuyCartStock.setItem(row, 0, QtWidgets.QTableWidgetItem(str(prod[0])))
            self.ui.Table_BuyCartStock.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod[1])))
            self.ui.Table_BuyCartStock.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod[1])))
            self.ui.Table_BuyCartStock.setItem(row, 3, QtWidgets.QTableWidgetItem(str(prod[1])))
            self.ui.Table_BuyCartStock.setItem(row, 4, QtWidgets.QTableWidgetItem(str(prod[1])))
            row +=1
        row=row+1
        if(len(self.row_cart)!=0):
            self.ui.btn_RequestOrder.setEnabled(1)
        else:
            self.ui.btn_RequestOrder.setEnabled(0)
            
    #####################################################################################
    def printDate(self) :
        qDate = self.ui.calendarWidget.selectedDate()
        date =('{0}-{1}-{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        self.ui.txt_SelectedDate.setText(date)
    def mark_attendance(self) :
        now1 = datetime.now()
        dateTime = now1.strftime("%Y-%m-%d %H:%M:%S")
        
        date = dateTime.split()
        today=date[0]
        print(today)
        
        #today = date.today()
        selected = self.ui.calendarWidget.selectedDate().getDate()
        selected_date=str(selected[0])+"-"+str(selected[1])+"-"+str(selected[2])
        print(str(selected_date))
        
        if (today == selected_date) :
            att = Attendence(self.user.getUserName() , self.user.getName())
            att.addInDateTimeList(today)
            self.attendanceDL.addIntoList(att)
            self.attendanceDL.insert_attendance()
        else :
            QMessageBox.warning(self,"Invalid Date" , "Please Select today's Date")
    def get_presents (self,attendanceDL) :
        count = 0
        for i in attendanceDL.getAttendancelist():
            if (i.userID == self.user.getUserName()) :
                for j in i.dateTimeList :
                    count = count + 1
        return count
    def get_absents (self, attendanceDL):
        presents = 0
        currentday = date.today().day
        presents = self.get_presents(attendanceDL)
        absents = currentday - presents
        return absents        
    

        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=InventoryMainWindow("name")
    window.show()
    sys.exit(app.exec_())