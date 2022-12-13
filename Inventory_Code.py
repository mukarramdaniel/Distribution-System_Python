import sys
from Inventory_Supervisor import *
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



class InventoryMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=InventoryMainWindow()
    window.show()
    sys.exit(app.exec_())