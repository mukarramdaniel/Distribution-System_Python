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
from Core.Notification import Notific
from DL.AttendenceCRUD import AttendenceCRUD
from Core.ProductList import ProducList
from DL.StockOrder_DL import StockOrder_DL
from DL.Inventory import Inventory
from random import randint
from DL.UserCRUD import UserCRUD
from DL.NotificationDL import Notifications
#import Login_Code
from email.message import EmailMessage
import smtplib
from datetime import datetime,date



class InventoryMainWindow(QMainWindow):
    #def __init__(self,parent=None):
    def __init__(self,user):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        self.inventory=Inventory()
        self.inventory.readFromTable()
        self.orderStockDL=StockOrder_DL()
        self.orderStockDL.loadFromTable()
        self.Notification_DL=Notifications()
        self.Notification_DL.loadFromTable()

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
        self.ui.btn_ReportCost.clicked.connect(lambda: self.OpenPageViewStock(4))
        self.ui.btn_AddtoCart.clicked.connect(lambda: self.AddToCart_Stock())
        self.ui.btn_RequestOrder.clicked.connect(lambda: self.orderStockFromCart())
        self.ui.btn_ViewHistory.clicked.connect(lambda: self.openViewHistory())
        self.ui.btn_Dashboard.clicked.connect(lambda: self.openDashboard())
        self.ui.btn_StockReport.clicked.connect(lambda: self.generate_report_cost())
        self.ui.btn_CheckIn.clicked.connect(lambda: self.checkInStock())
        self.ui.btn_MarkAttendance_2.clicked.connect(lambda: self.mark_attendance())
        self.ui.calendarWidget.clicked.connect(lambda: self.printDate())
        self.ui.lineEdit.setText(str(self.get_presents(self.attendanceDL)))
        self.ui.lineEdit_3.setText(str(self.get_absents(self.attendanceDL)))
        self.ui.btn_Calculate.clicked.connect(lambda: self.Calculate_Selling_Price())
        #self.ui.cmb_Category_2.view().pressed.connect(lambda: self.Handle_Product_Names())
        self.ui.cmb_Category_2.currentIndexChanged.connect(lambda: self.Handle_Product_Category())
        self.show()

    def openDashboard(self):
        self.ui.mainBody.setCurrentIndex(3)
    def openViewHistory(self):
        self.ui.mainBody.setCurrentIndex(5)
        self.Load_Table_History()
    def Load_Table_History(self):
        row=0
        DlinkList=self.orderStockDL.getDLinklist()
        self.ui.tableWidget_History.setRowCount(self.calculateRow_History())
        while(DlinkList!=None):
            #if(DlinkList.data.getStatus()==1):
            for prod in DlinkList.data.getShoeList():
                self.ui.tableWidget_History.setItem(row, 0, QtWidgets.QTableWidgetItem(str(DlinkList.data.getOrderID())))
                self.ui.tableWidget_History.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod.getProductCategory())))
                self.ui.tableWidget_History.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod.getColor())))
                self.ui.tableWidget_History.setItem(row, 3, QtWidgets.QTableWidgetItem(str(prod.getBuyPrice())))
                self.ui.tableWidget_History.setItem(row, 4, QtWidgets.QTableWidgetItem(str(DlinkList.data.date)))
                self.ui.tableWidget_History.setItem(row, 5, QtWidgets.QTableWidgetItem(str(DlinkList.data.date)))
                row +=1
                    
            DlinkList=DlinkList.next
    def calculateRow_History(self):
        count=0
        DlinkList=self.orderStockDL.getDLinklist()
        while(DlinkList!=None):
            for prod in DlinkList.data.getShoeList():
                count+=1
            DlinkList=DlinkList.next
        return count
    def Handle_Product_Category(self):
        Category=self.ui.cmb_Category_2.currentText()
        isFound=False
        for bucket in self.inventory.getInventoryStock():
            for prod in bucket:
                if(prod!=None and prod[1].getProductCategory()==Category):
                    self.ui.txt_BuyingPrice.setText(str(prod[1].getBuyPrice()))
                    isFound=True
                    break
            if(isFound):
                break
        if(isFound==False):
            QMessageBox.warning(self,"Category not Found" , "Product Category not available")


    def Calculate_Selling_Price(self):
        Category=self.ui.cmb_Category_2.currentText()
        Buy_Price=(self.ui.txt_BuyingPrice.text())
        Gov_Tax=(self.ui.txt_GovernmentTaxes.text())
        Profit_Margin=(self.ui.txt_ProfitMargin.text())
        Comapny_Expense=(self.ui.txt_Expenses.text())
        if(Category!="" and Buy_Price!="" and Gov_Tax!="" and Profit_Margin!="" and Comapny_Expense!=""):
            Margin=float(Buy_Price)*(float(Profit_Margin)/100)
            Tax=float(Buy_Price)*(float(Gov_Tax)/100)
            Sell_Price=float(Buy_Price)+Margin+Tax+float(Comapny_Expense)
            self.ui.txt_CalculatedPrice.setText(str(Sell_Price))
            isFound=False
            for bucket in self.inventory.getInventoryStock():
                for prod in bucket:
                    if(prod!=None and prod[1].getProductCategory()==Category):
                        prod[1].setSellPrice(Sell_Price)
                        prod[1].setProfirMargin(float(Profit_Margin))
                        isFound=True
                        
        else:
            QMessageBox.warning(self,"Input Error" , "All inputs must be filled")
    def checkInStock(self):
        self.ui.table_UpdateStock.clearContents()
         
        DlinkList=self.orderStockDL.getDLinklist()
        while(DlinkList!=None):
            if(DlinkList.data.getStatus()==1):

                # for prod in DlinkList.data.getShoeList():
                #     self.inventory.setProduct(prod.getProductCategory(),prod)
                DlinkList.data.setStatus(2)
                
            DlinkList=DlinkList.next
        self.orderStockDL.UpdateTable()
        

    def orderStockFromCart(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M:%S")
        OrderID=self.orderStockDL.generateOrderID()
        order=ProducList(OrderID,date,self.temp_OrderList,0)
        self.orderStockDL.Insert(order)
        self.orderStockDL.UpdateTable()
        self.row_cart.clear()
        self.emptyTableAndList()
        n=Notific(OrderID, "Order is placed. Kindly check Email for Further Details")
        self.Notification_DL.Add_Notification(n)
        self.Notification_DL.updateTable()
        self.send_mail(order)
        if(len(self.row_cart)==0):
            self.ui.btn_RequestOrder.setEnabled(0)
        else:
            self.ui.btn_RequestOrder.setEnabled(1)
    
    def send_mail(self,order) :
        listt = []
        list2=[]
        list3=[]
        list4=[]
        for i in order.getShoeList():
            listt.append(i.getShoeSize())
            list2.append(i.getColor())
            list3.append(i.getBuyPrice())
            list4.append(i.getProductCategory())
        sizes = set(listt)
        color=set(list2)
        price=set(list3)
        ctype=set(list4)
        email_sender = "rasheedrayan514@gmail.com"
        email_password = 'zpzsrqeasritevbu' 
        email_receiver="ammadaslam07@gmail.com"
        subject = "Products Purchasing"
        body = '''
        Dear Manager,
        Please check your notification for confirmation of the order '''+ str(order.getOrderID())+ ''' from ADIDAS New York.
        The details are given below:
        • Quantity:'''+str(len(order.getShoeList())) + '''pieces
        • Size:'''+str(sizes)+ ''' 
        • Color:'''+str(color)+'''
        • Type:'''+str(ctype)+'''
        • Price:'''+str(price)+''' per piece
        Regards,
        Inventory Supervisor
        '''
        em = EmailMessage()
        em['from'] = email_sender
        em['to'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        with smtplib.SMTP_SSL('smtp.gmail.com' , 465 ) as smtp:
            smtp.login(email_sender , email_password)
            smtp.sendmail(email_sender , email_receiver , em.as_string())
    def emptyTableAndList(self):
        self.ui.Table_BuyCartStock.clearContents()
        self.temp_OrderList=[]
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
        if(int(Product_Quantity)>0 and int(Product_Size)>0 and int(Product_Price)>0 and Product_Price.isdigit()):
            self.row_cart.append((Product_Category,Product_Quantity,Product_Size,Product_Color,Product_Price,t_price))
            prodID=self.generateProdID()
            self.clearField()
            for i in range(int(Product_Quantity)):
                shoe = Shoe(Product_Category, Product_Price, 0 , Product_Size, 0 , Product_Color, prodID,"men")
                t_price +=int(Product_Price)
                self.temp_OrderList.append(shoe)
            self.loadUpdate_tableWidget(t_price)

            QMessageBox.information(self,"ADDED" ,"Product Added")
        else:
            QMessageBox.warning(self,"Invalid" ,"Invalid Input")
            self.clearField()
    def clearField(self):
        self.ui.cmb_Category.clearEditText()
        self.ui.spb_Quantity.cleanText()
        self.ui.spb_Size.cleanText()
        self.ui.cmb_Color.clearEditText()
        self.ui.txt_PriceperShoes.clear()
    def generateProdID(self):
        from random import randint
        start = 10**(6-1)
        end = (10**6)-1
        code = str(randint(start,end))
        return code

    def loadUpdate_tableWidget(self,t_price):
        row=0
        self.ui.Table_BuyCartStock.setRowCount(len(self.row_cart))
        for prod in self.row_cart:
            self.ui.Table_BuyCartStock.setItem(row, 0, QtWidgets.QTableWidgetItem(str(prod[0])))
            self.ui.Table_BuyCartStock.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod[1])))
            self.ui.Table_BuyCartStock.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod[2])))
            self.ui.Table_BuyCartStock.setItem(row, 3, QtWidgets.QTableWidgetItem(str(prod[3])))
            self.ui.Table_BuyCartStock.setItem(row, 4, QtWidgets.QTableWidgetItem(str(prod[4])))
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
            self.attendanceDL.insert_attendance(self.attendanceDL.getAttendancelist())
        else :
            QMessageBox.warning(self,"Invalid Date" , "Please Select today's Date")
    def get_presents (self,attendanceDL) :
        count = 0
        for i in attendanceDL.getAttendancelist():
            if (i.getUserName() == self.user.getUserName()) :
                for j in i.dateTimeList :
                    count = count + 1
        return count
    def get_absents (self, attendanceDL):
        presents = 0
        currentday = date.today().day
        presents = self.get_presents(attendanceDL)
        absents = currentday - presents
        return absents        
    def generate_report_cost (self) :
        from fpdf import FPDF
        pdf = FPDF ()
        pdf.add_page()
        pdf.set_font("Arial" ,"B" ,size= 20)
        page_width = pdf.w - 2 *  pdf.l_margin
        cell_height = pdf.font_size
        pdf.cell(page_width,0.0,"Report Cost",ln=10,align="C")
        pdf.ln(10)
        pdf.set_font("Arial" ,"B" ,size= 8)
        pdf.cell(32,cell_height, "Category")
        pdf.cell(32,cell_height, "Buying Price")
        pdf.cell(32,cell_height, "Color")
        pdf.cell(32,cell_height, "Shoe Size")
        pdf.cell(32,cell_height, "Selling Price")
        pdf.line(x1 = 10, y1 = 27.5, x2 = 200, y2 = 27.5)
        pdf.set_font("Arial" ,size= 8)
        pdf.ln(cell_height+1)
        stock=self.orderStockDL.getDLinklist()
        while(stock!=None):
            s=stock.getData() 
            for x in s.getShoeList(): 
                pdf.cell(32,cell_height,str(x.getProductCategory()))
                pdf.cell(32,cell_height,str(x.getBuyPrice()))
                pdf.cell(32,cell_height,str(x.getColor()))
                pdf.cell(32,cell_height,str(x.getShoeSize()))
                pdf.cell(32,cell_height,str(x.getSellPrice()))
                pdf.ln(cell_height+1)
            stock=stock.next
        pdf.output("sample1.pdf" , "F")

        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=InventoryMainWindow("name")
    window.show()
    sys.exit(app.exec_())