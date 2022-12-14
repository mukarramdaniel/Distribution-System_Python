
from UI.Login import Ui_LoginWindow
from DL.UserCRUD import *
import sys
#from Stacked_DesignUI1 import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
import re  #imported to validate he email
from Manager_UI import ManaMainWindow
from Inventory_Code import InventoryMainWindow
import os
from email.message import EmailMessage
import smtplib
from random import randint

class MainWindow(QMainWindow):
    code = 0
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.user=UserCRUD()
        self.user.readFromTable()
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.forgotbtn.clicked.connect(lambda: self.OpenForgetScreen())
        self.ui.loginbtn.clicked.connect(lambda: self.Handle_Login())
        self.ui.backbtn.clicked.connect(lambda: self.BactTo_Login(0))
        self.ui.sendbtn.clicked.connect(lambda: self.send_resetmail(self.ui.emailtxt.text() , 6))
        self.ui.resetbtn.clicked.connect(lambda: self.create_newpassword(self.ui.passwordtxt.text() , self.ui.emailtxt.text()))
        self.ui.backbtn_2.clicked.connect(lambda: self.BactTo_Login(0))
        self.show()
    
    
        
    def Handle_Login(self):
        
        Email=self.ui.emailinp.text()
        Password=self.ui.passwordinp.text()
        flag=self.Validate_Email_password(Email,Password)
        if(flag):
            retrive=self.user.verify(Email,Password)
            print(retrive.userRole)
            
            if(retrive!=None):
                if(retrive.userRole==0):
                    self.Open_Manager_Window()
                elif(retrive.userRole==1):
                    self.Open_Inventory_Window()
        else:
            QMessageBox.warning(self,'Error','Incorrect Email and Password')
            self.ui.emailinp.clear()
            self.ui.passwordinp.clear()
            
    def Validate_Email_password(self,Email,password):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,Email)):
            if(len(password)>8):
                return True  
        else:   
            return False 
    def send_resetmail(self , email , n) :
        start = 10**(n-1)
        end = (10**n)-1
        self.code = randint(start,end)
        email_sender = "rasheedrayan514@gmail.com"
        email_password = 'zpzsrqeasritevbu'
        email_flag = self.validate_email(email) 
        if(email_flag):
            getuser = self.user.getUserReturn(email)
            
            if(getuser!=None):
                email_receiver=email
                subject = "Forget Password"
                body = '''
                Dear User,
                Your new password of the account is '''+str(self.code)+'''Enter this now to have access to your account.
                Regards,
                ARM limited
                '''
                em = EmailMessage()
                em['from'] = email_sender
                em['to'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)
                with smtplib.SMTP_SSL('smtp.gmail.com' , 465 ) as smtp:
                    smtp.login(email_sender , email_password)
                    smtp.sendmail(email_sender , email_receiver , em.as_string())
                self.Open_newpassword_Screen()

            
            
        
    def validate_email(self,email) :
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex,email)):
            return True
        else:
            return False
    def create_newpassword(self , password , email) :
        if(str(self.code) == self.ui.codetxt.text()) :
            if (self.ui.passwordtxt.text() != '' ):
                if (password == self.ui.confirmtxt.text()):
                    changed_user = self.user.getUserReturn(email)
                    changed_user.password = password
                    self.BactTo_Login(0)
                    #update()
                else :
                    QMessageBox.warning(self,'Error','Password must be same')
            else :
                QMessageBox.warning(self,'Error','Password cannot be empty')
        else:
            QMessageBox.warning(self,'Error','Incorrect code')


    def Open_Manager_Window(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui=ManaMainWindow()
        self.close()
        #self.ui.setupUi(self.MainWindow)
        #self.MainWindow.show()
    def Open_Inventory_Window(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui=InventoryMainWindow()
    def OpenForgetScreen(self):
        self.ui.loginStackedWidget.setCurrentIndex(1)
    def Open_newpassword_Screen(self):
        self.ui.loginStackedWidget.setCurrentIndex(2)
    def BactTo_Login(self , n):
        self.ui.loginStackedWidget.setCurrentIndex(n)
        
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())