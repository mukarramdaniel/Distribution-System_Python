from UI.Login import Ui_LoginWindow
import sys
#from Stacked_DesignUI1 import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
#import mysql.connector()
import re  #imported to validate he email
from Manager_UI import ManaMainWindow
#import Manager_UI
import os
from email.message import EmailMessage
import smtplib
from random import randint
from email_validator import validate_email

class MainWindow(QMainWindow):
    code = 0
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.forgotbtn.clicked.connect(lambda: self.OpenForgetScreen())
        self.ui.loginbtn.clicked.connect(lambda: self.Handle_Login())
        self.ui.backbtn.clicked.connect(lambda: self.BackTo_Login(0))
        self.ui.sendbtn.clicked.connect(lambda: self.send_resetmail(self.ui.emailtxt.text() , 6))
        self.ui.resetbtn.clicked.connect(lambda: self.create_newpassword(self.ui.passwordtxt.text()))
        self.ui.backbtn_2.clicked.connect(lambda: self.BackTo_Login(1))

        self.show()
    
    
        
    def Handle_Login(self):
        
        Email=self.ui.emailinp.text()
        Password=self.ui.passwordinp.text()
        flag=self.Validate_Email_password(Email,Password)
        if(flag):
            QMessageBox.information(self,'Info','user and password ok')
            
        else:
            QMessageBox.warning(self,'Error','Incorrect Email and Password')
            self.ui.emailinp.clear()
            self.ui.passwordinp.clear()
        self.Open_Manager_Window()
            
    def Validate_Email_password(self,Email,password):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,Email)):
            if(len(password)>8):
                return True  
        else:   
            return False
    def validate_email(self,email) :
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex,email)):
            return True
        else:
            return False
    def send_resetmail(self , email , n) :
        if (self.validate_email(email)) :
            start = 10**(n-1)
            end = (10**n)-1
            self.code = randint(start,end)
            email_sender = "rasheedrayan514@gmail.com"
            email_password = 'zpzsrqeasritevbu'
            email_receiver = email

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
        else :
            QMessageBox.warning(self,'Error','Enter valid Email')
    def create_newpassword(self , password) :
        if(str(self.code) == self.ui.codetxt.text()) :
            if (self.ui.passwordtxt.text() != '' ):
                if (self.ui.passwordtxt.text() == self.ui.confirmtxt.text()):
                    QMessageBox.information(self,'Info','user and password ok')
                else :
                    QMessageBox.warning(self,'Error','Password must be same')
            else :
                QMessageBox.warning(self,'Error','Password cannot be empty')
        else:
            QMessageBox.warning(self,'Error','Incorrect code')
    def Open_Manager_Window(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui=ManaMainWindow()
        #self.ui.setupUi(self.MainWindow)
        #self.MainWindow.show()
        
       

    def OpenForgetScreen(self):
        self.ui.loginStackedWidget.setCurrentIndex(1)
    def Open_newpassword_Screen(self):
        self.ui.loginStackedWidget.setCurrentIndex(2)
    def BackTo_Login(self , n):
        self.ui.loginStackedWidget.setCurrentIndex(n)
    
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())