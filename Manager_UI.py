#from UI.Login import Ui_LoginWindow
import sys
from Stacked_DesignUI1 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
import re
from Core import User, InventorySupervisor, Rider , SaleAgent, Vehicle
from DL.UserCRUD import UserCRUD
from DL.VehicleCRUD import VehicleCRUD

from random import randint
from datetime import date



class ManaMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.userDL = UserCRUD()
        self.userDL.readFromTable()
        self.vehicleDL=VehicleCRUD()
        self.vehicleDL.loadFromTable()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card1.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card2.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card3.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card4.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_TopClients.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame_TableWhatsNew.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame_GoalsCompleted.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Account_Widget.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Input_Widget.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.HeaderFrame_3.setGraphicsEffect(self.shadow)

        #--------------Shadow Add Vehicle--------------
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_17.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_12.setGraphicsEffect(self.shadow)
        #----------------------------------------------

        #self.ui.btnUpdateStock.clicked.connect(lambda: self.OpenUpdatePage())
        #self.ui.btnBuyStock.clicked.connect(lambda: self.OpenBuyStockPage())
        #self.ui.btn_Report_Cost.clicked.connect(lambda: self.OpenReportCostPage())
        self.ui.menuBtn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_2.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_3.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_4.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_5.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_2.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_3.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_4.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_5.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.btnAddEmployee.clicked.connect(lambda: self.OpenAddEmployee())
        self.ui.btnDashboard.clicked.connect(lambda: self.OpenDashboardManager())
        self.ui.btnUpdateEmployee.clicked.connect(lambda: self.OpenUpdateEmployee())
        self.ui.btn_AddVehicle.clicked.connect(lambda: self.OpenAddVehicleManager())
        self.ui.btnCheckAttendance.clicked.connect(lambda: self.OpenCheckAttendanceManager())
        self.ui.btn_AddEmployee.clicked.connect(lambda: self.Add_Employee())
        self.ui.btn_GenerateID.clicked.connect(lambda: self.generate_userID())
        self.ui.btn_GeneratePassword.clicked.connect(lambda: self.generate_password(8,self.ui.txt_Passsword))
        self.ui.btn_UpdateDetails.clicked.connect(lambda: self.ShowToUpdateEmployee())
        self.ui.btn_Delete.clicked.connect(lambda: self.deleteEmployee(self.updateEmpObj))
        self.ui.btn_Update.clicked.connect(lambda: self.update_employee(self.updateEmpObj))
        self.ui.Update_tableWidget.verticalHeader().sectionClicked.connect(lambda: self.getTableRow())
        self.ui.btn_AddVehicle_2.clicked.connect(lambda: self.addVehicle())
        
        
        
        self.show()
    def getTableRow(self):
       
        tableRow=self.ui.Update_tableWidget.currentRow()
        userName=self.ui.Update_tableWidget.item(tableRow,7)
        self.updateEmpObj=self.userDL.getUserReturn(userName.text())
        if(self.updateEmpObj!=None):
            self.ui.btn_UpdateDetails.setEnabled(1)
            self.ui.btn_Delete.setEnabled(1)
        
            
  
    def OpenCheckAttendanceManager(self):
        self.ui.mainBody.setCurrentIndex(4)
    def OpenAddVehicleManager(self):
        self.ui.mainBody.setCurrentIndex(1)
        self.loadVehicle_tableWidget()   
        
    def OpenUpdateEmployee(self ):
        self.ui.mainBody.setCurrentIndex(2) 
        self.loadUpdate_tableWidget()   
    def OpenUpdateEmployeeManager(self ,n):
        self.ui.mainBody.setCurrentIndex(n)
    def OpenDashboardManager(self):
        self.ui.mainBody.setCurrentIndex(0)
    def ShowToUpdateEmployee(self):
        self.ui.mainBody.setCurrentIndex(3)
        self.EditToUpdate_employee(self.updateEmpObj)
    def SpecificldReturnUI(self,n):
        self.ui.mainBody.setCurrentIndex(n)
        
    def OpenAddEmployee(self):
        self.ui.mainBody.setCurrentIndex(4)
    
    def slideLeftMenu(self):
        width=self.ui.LeftMenu.width()
        if(width==0):
            newWidth=220
            #self.ui.menuBtn_2.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/chevron-left.svg"))
        else:
            newWidth=0
            #self.ui.menuBtn.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/align-left.svg"))
        self.animation = QPropertyAnimation(self.ui.LeftMenu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def SlideRightMenu(self):
        width=self.ui.profileCont.width()
        if(width==0):
            newWidth=105
        else:
            newWidth=0
        self.animation = QPropertyAnimation(self.ui.profileCont, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()
    def generate_password (self,n,a) :
        start = 10**(n-1)
        end = (10**n)-1
        code = randint(start,end)
        a.setText(str(code))
    def generate_userID(self) :
        userID=0
        for bucket in self.userDL.getHashTable():
            for user in bucket:
                if(user!=None):
                    userID +=1
        self.Employee_userID=userID+1 
        self.ui.txt_GenerateId.setText(str(self.Employee_userID))
                  
                    
    def clear_screen (self) :
        self.ui.txt_Name.clear()
        self.ui.txt_Name.clear()
        self.ui.txt_Age.clear()
        self.ui.txt_Cnic.clear()
        self.ui.txt_Email.clear()
        self.ui.txt_PhoneNumber.clear()
        self.ui.txt_BankAccount.clear()
        self.ui.spinBox_Salary.clear()
        self.ui.txt_Passsword.clear()
    def Add_Employee(self):
        #Employee_userID = "3"
        Employee_Name =self.ui.txt_Name.text()
        Employee_username = self.ui.txt_Name.text()
        Employee_Age =self.ui.txt_Age.text()
        Employee_CNIC =self.ui.txt_Cnic.text()
        Employee_Email =self.ui.txt_Email.text()
        Employee_PhoneNo =self.ui.txt_PhoneNumber.text()
        Employee_BankAccount =self.ui.txt_BankAccount.text()
        Employee_Status =self.ui.cmb_Employee.currentIndex()+1
        
        Employee_Salary =self.ui.spinBox_Salary.text()
        Employee_password = self.ui.txt_Passsword.text()
        Employee_createDate = date.today()
        Employee_updateDate = date.today()
        my_user = (self.Employee_userID ,Employee_username,Employee_password,Employee_Status,Employee_Name,Employee_Age,Employee_PhoneNo,Employee_Email,Employee_CNIC,Employee_BankAccount,Employee_createDate , Employee_updateDate)
        if(Employee_Status==1):
            inventory_supervisor = InventorySupervisor.InventorySupervisor(my_user,Employee_Salary,Employee_createDate)
            self.userDL.setUser(Employee_username,inventory_supervisor)
            QMessageBox.information(self,"ADDED" ,"Employee Added")
            self.clear_screen()
        if(Employee_Status==3):
            rider = Rider.Driver(my_user,Employee_Salary)
            self.userDL.setUser(Employee_username,rider)
            QMessageBox.information(self,"ADDED" ,"Employee Added")
            self.clear_screen()
        if(Employee_Status==2):
            sales_agent = SaleAgent.SaleAgent(my_user,Employee_Salary,Employee_createDate)
            self.userDL.setUser(Employee_username,sales_agent)
            QMessageBox.information(self,"ADDED" ,"Employee Added")
            self.clear_screen()
    def EditToUpdate_employee (self, employee) :
        self.ui.txt_Name_2.setText(employee.name) 
        self.ui.txt_CNIC.setText(str(employee.CNIC))
        self.ui.txt_Age_2.setText(str(employee.age))
        self.ui.txt_Email_2.setText(employee.Email)
        self.ui.txt_PhonoNumber.setText(str(employee.contactNum))
        self.ui.txt_BankAccount_2.setText(str(employee.BankAccount))
        self.ui.lineEdit_7.setText(str(employee.getSalary())) 
    def update_employee (self,employee) :
        employee.name = self.ui.txt_Name_2.text() 
        employee.CNIC = self.ui.txt_CNIC.text()
        employee.age = self.ui.txt_Age_2.text()
        employee.Email = self.ui.txt_Email_2.text()
        employee.contactNum = self.ui.txt_PhonoNumber.text()
        employee.BankAccount = self.ui.txt_BankAccount_2.text()
        employee.setSalary(self.ui.lineEdit_7.text())
        employee.updatedDate = date.today()
        self.OpenUpdateEmployee()
    def deleteEmployee(self,employee):
        self.userDL.deleteUser(employee.getUsername(),employee)
        self.OpenUpdateEmployee()
    def loadUpdate_tableWidget(self):
        self.ui.btn_UpdateDetails.setEnabled(0)
        self.ui.btn_Delete.setEnabled(0)
        self.ui.Update_tableWidget.clear()
        hashtable=self.userDL.getHashTable()
        row=0
        userRole=""
        for bucket in hashtable:
            for user in bucket:
                if(user!=None and user[1].userRole!=0):
                    self.ui.Update_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user[1].userId)))
                    self.ui.Update_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1].name))
                    self.ui.Update_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[1].CNIC))
                    if(user[1].userRole==1):
                        userRole="Inventory Supervisor"
                    elif(user[1].userRole==2):
                        userRole="Sales Agent"
                    elif(user[1].userRole==3):
                        userRole="Rider"
                    self.ui.Update_tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(userRole))
                    self.ui.Update_tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(user[1].contactNum))
                    self.ui.Update_tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(user[1].age)))
                    self.ui.Update_tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[1].Email))
                    self.ui.Update_tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(user[1].userName))
                    row=row+1
                    
    def loadVehicle_tableWidget(self):
        self.ui.btn_Edit.setEnabled(0)
        self.ui.btn_Delete_2.setEnabled(0)
        DLinkList=self.vehicleDL.getList()
        self.ui.table_Vehicle.clearSpans()
        row=0
        for data in DLinkList:
            self.ui.table_Vehicle.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data.model)))
            self.ui.table_Vehicle.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data.number)))
            self.ui.table_Vehicle.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data.fuelAverage)))
            row=row+1
    def addVehicle(self):
        model=self.ui.txt_VehicleModel.text()
        number=self.ui.txt_VehicleNumber.text()
        fuelAverage=self.ui.txt_FuelAverage.text()
        if(model!="" and model!="" and model!=""):
            self.ui.txt_VehicleModel.clear()
            self.ui.txt_VehicleNumber.clear()
            self.ui.txt_FuelAverage.clear()
            vehicle=Vehicle.Vehicle(model,number,fuelAverage)
            self.vehicleDL.addToList(vehicle)
            self.loadVehicle_tableWidget()
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ManaMainWindow()
    window.show()
    sys.exit(app.exec_())