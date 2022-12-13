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
from Core import User, InventorySupervisor, Rider , SaleAgent
from DL.UserCRUD import UserCRUD
from random import randint
from datetime import date



class ManaMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.userDL = UserCRUD()
        self.userDL.readFromTable()
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
        self.ui.btnUpdateEmployee.clicked.connect(lambda: self.OpenUpdateEmployeeManager())
        self.ui.btn_AddVehicle.clicked.connect(lambda: self.OpenAddVehicleManager())
        self.ui.btnCheckAttendance.clicked.connect(lambda: self.OpenCheckAttendanceManager())
        self.ui.btn_AddEmployee.clicked.connect(lambda: self.Add_Employee())
        self.ui.btn_GeneratePassword.clicked.connect(lambda: self.generate_password(8,self.ui.txt_Passsword))
        
        self.show()
        
    def OpenCheckAttendanceManager(self):
        self.ui.mainBody.setCurrentIndex(4)
    def OpenAddVehicleManager(self):
        self.ui.mainBody.setCurrentIndex(1)
    def OpenUpdateEmployeeManager(self):
        self.ui.mainBody.setCurrentIndex(2)
    def OpenDashboardManager(self):
        self.ui.mainBody.setCurrentIndex(0)
    def OpenAddEmployee(self):
        self.ui.mainBody.setCurrentIndex(3)
    
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
    #def generate_userID() :
    def clear_screen (self) :
        self.ui.txt_Name.clear()
        self.ui.txt_Name.clear()
        self.ui.txt_Age.clear()
        self.ui.txt_Cnic.clear()
        self.ui.txt_Email.clear()
        self.ui.txt_PhoneNo.clear()
        self.ui.txt_BankAccount.clear()
        self.ui.spinBox_Salary.clear()
        self.ui.txt_Passsword.clear()
    def Add_Employee(self):
        Employee_userID = "3"
        Employee_Name =self.ui.txt_Name.text()
        Employee_username = self.ui.txt_Name.text()
        Employee_Age =self.ui.txt_Age.text()
        Employee_CNIC =self.ui.txt_Cnic.text()
        Employee_Email =self.ui.txt_Email.text()
        Employee_PhoneNo =self.ui.txt_PhoneNo.text()
        Employee_BankAccount =self.ui.txt_BankAccount.text()
        Employee_Status =self.ui.cmb_Employee.currentText()
        Employee_Salary =self.ui.spinBox_Salary.text()
        Employee_password = self.ui.txt_Passsword.text()
        Employee_createDate = date.today()
        Employee_updateDate = date.today()
        my_user = (Employee_userID ,Employee_username,Employee_password,Employee_Status,Employee_Name,Employee_Age,Employee_PhoneNo,Employee_Email,Employee_CNIC,Employee_BankAccount,Employee_createDate , Employee_updateDate)
        if(Employee_Status=="Inventory Supervisor"):
            inventory_supervisor = InventorySupervisor.InventorySupervisor(my_user,Employee_Salary,Employee_createDate)
            self.userDL.setUser(Employee_username,inventory_supervisor)
            u=self.userDL.getUserReturn("rayan")
            print(u.Email)
            self.clear_screen()
        if(Employee_Status=="Rider"):
            rider = Rider.Driver(my_user,Employee_Salary)
            self.userDL.setUser(Employee_username,rider)
           # QMessageBox.information(self,"ADDED")
           
            self.clear_screen()
        if(Employee_Status=="Sales Agent"):
            sales_agent = SaleAgent.SaleAgent(my_user,Employee_Salary,Employee_createDate)
            self.userDL.setUser(Employee_username,sales_agent)
            QMessageBox.information(self,"ADDED")
            self.clear_screen()


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ManaMainWindow()
    window.show()
    sys.exit(app.exec_())