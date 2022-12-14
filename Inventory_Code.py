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
from DL.Inventory import Inventory
from random import randint
from datetime import date



class InventoryMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.temp_OrderList=[]
        self.total = 0
        #self.prodList=ProducList()

        #self.ShoesDL=Inventory()
        #self.ShoesDL=ProducList(ShoeList, productID)
        self.ui.btnBuyStock.clicked.connect(lambda: self.OpenPages(0))
        self.ui.btn_Update_Stock.clicked.connect(lambda: self.OpenPages(1))
        self.ui.btn_ViewStock.clicked.connect(lambda: self.OpenPages(2))
        self.ui.btn_AddtoCart.clicked.connect(lambda: self.AddToCart_Stock())
        self.show()

    def OpenPages(self,idx):
        self.ui.mainBody.setCurrentIndex(idx)
    
    def AddToCart_Stock(self):
        Product_Category=self.ui.cmb_Category.currentText()
        Product_Quantity=self.ui.spb_Quantity.text()
        Product_Size=self.ui.spb_Size.text()
        Product_Color=self.ui.cmb_Color.currentText()
        Product_Price=self.ui.txt_PriceperShoes.text()
        
        prodID="001"
        
        for i in range(int(Product_Quantity)):
            shoe = Shoe(Product_Category, Product_Price, 0 , Product_Size, 0 , Product_Color, prodID)
            self.temp_OrderList.append(shoe)
            #self.total = self.total + Pro
        self.loadUpdate_tableWidget()
        
        #ProducList(shoe, prodID)
        #self.ShoesDL.setProduct(Product_Category, shoe)
        QMessageBox.information(self,"ADDED" ,"Product Added")
    def loadUpdate_tableWidget(self):
        row=0
        self.ui.Table_BuyCart.setRowCount(len(self.temp_OrderList))
        for prod in self.temp_OrderList:

            self.ui.Table_BuyCart.setItem(row, 0, QtWidgets.QTableWidgetItem(str(prod.getprodID())))
            self.ui.Table_BuyCart.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod.getProductCategory())))
            self.ui.Table_BuyCart.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod.getShoeSize())))
            self.ui.Table_BuyCart.setItem(row, 3, QtWidgets.QTableWidgetItem(prod.getColor()))
            self.ui.Table_BuyCart.setItem(row, 4, QtWidgets.QTableWidgetItem(str(prod.getBuyPrice())))
            row=row+1
    def create_object(self, temp_OrderList):
        order_obj= ProducList(temp_OrderList, "001")
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=InventoryMainWindow()
    window.show()
    sys.exit(app.exec_())