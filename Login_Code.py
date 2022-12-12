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
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.forgotbtn.clicked.connect(lambda: self.OpenForgetScreen())
        self.ui.loginbtn.clicked.connect(lambda: self.Handle_Login())
        self.ui.backbtn.clicked.connect(lambda: self.BactTo_Login())
        self.show()
    
    
        
    def Handle_Login(self):
        #   self.ui.passwordinp.setText('sdfsdf')
        
        # Email=self.ui.emailinp.text()
        # Password=self.ui.passwordinp.text()
        # flag=self.Validate_Email(Email,Password)
        # if(flag):
        #     QMessageBox.information(self,'Info','user and password ok')
            
        # else:
        #     QMessageBox.warning(self,'Error','Incorrect Email and Password')
        #     self.ui.emailinp.clear()
        #     self.ui.passwordinp.clear()
        self.Open_Manager_Window()
            
    def Validate_Email(self,Email,password):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,Email)):
            if(len(password)>8):
                return True  
        else:   
            return False 
    
    def Open_Manager_Window(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui=ManaMainWindow()
        #self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
       

    def OpenForgetScreen(self):
        self.ui.loginStackedWidget.setCurrentIndex(1)
        
    def BactTo_Login(self):
        self.ui.loginStackedWidget.setCurrentIndex(0)
        
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())