import sys
from Rider import *
from Maps.maps import distance_between_places,getLocation
from Maps.SelectShop import * 
from Core.Shop import Shop
from DL.ShopCRUD import *
from PyQt5 import QtWidgets
from DL.UserCRUD import *
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
from datetime import datetime
class RiderMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_RiderWindow()
        self.ui.setupUi(self)
        self.shopDL=ShopCRUD()
        self.shopDL.loadFromTable()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_15.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_27.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_26.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_42.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_47.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_67.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_18.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_4.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_51.setGraphicsEffect(self.shadow)

        self.ui.menuBtn_8.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_11.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_7.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_9.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_10.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_12.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_13.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn_8.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_11.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_7.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_9.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_10.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_12.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_13.clicked.connect(lambda: self.SlideRightMenu())

        self.ui.btn_Dashboard.clicked.connect(lambda: self.OpenDashBoard())
        self.ui.btn_AddShop.clicked.connect(lambda: self.OpenAddShop())
        self.ui.btn_TakeOrder.clicked.connect(lambda: self.OpenTakeOrder())
        self.ui.btn_DeliverOrder.clicked.connect(lambda: self.OpenDeliverOrder())
        self.ui.btn_ViewStock_2.clicked.connect(lambda: self.OpenViewStock())
        self.ui.btn_ToDoList.clicked.connect(lambda: self.OpenTodoList())
        self.ui.btn_History.clicked.connect(lambda: self.OpenHistory())
        self.ui.btn_AddShop.clicked.connect(lambda: self.addShopMenu())
        self.ui.btn_Add.clicked.connect(lambda: self.addShop())
        self.ui.btn_Map.clicked.connect(lambda: self.selectShopMap())
        
       
        self.show()
    def selectShopMap():
        pass
        # self.MainWindow = QtWidgets.QMainWindow()
        # self.ui=MapViewer()
        # self.ui.show()
        
    def addShopMenu(self):
        self.ui.mainBody.setCurrentIndex(4)
    def addShop(self):
        name=self.ui.txt_Name.text()
        cnic=self.ui.txt_Cnic.text()
        email=self.ui.txt_Email.text()
        Address=self.ui.txt_Address.text()
        loca=getLocation(Address)
        location=Location(loca[1],loca[2],loca[0])
        print(loca[0],loca[1],loca[2])
        PhoneNumber=self.ui.txt_PhoneNumber.text()
        AccountNo=self.ui.txt_AccountNo.text()
        Area=self.ui.cmb_Area.currentText()
        shopName=self.ui.txt_Shop.text()
        openTime=self.ui.timeEdit.text()
        closeTime=self.ui.timeEdit_2.text()
        now = datetime.now()
        created_on = now.strftime("%d-%m-%Y %H:%M:%S")
        shop=Shop(4,name,cnic,email,location,PhoneNumber,AccountNo,Area,shopName,openTime,closeTime,created_on)
        self.shopDL.Insert(shop)
        self.shopDL.updateTable()
    def OpenDashBoard(self):
        self.ui.mainBody.setCurrentIndex(3)
    def OpenAddShop(self):
        self.ui.mainBody.setCurrentIndex(4)
    def OpenTakeOrder(self):
        self.ui.mainBody.setCurrentIndex(1)
    def OpenDeliverOrder(self):
        self.ui.mainBody.setCurrentIndex(0)
    def OpenViewStock(self):
        self.ui.mainBody.setCurrentIndex(2)
    def OpenTodoList(self):
        self.ui.mainBody.setCurrentIndex(6)
    def OpenHistory(self):
        self.ui.mainBody.setCurrentIndex(5)   
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

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=RiderMainWindow()
    window.show()
    sys.exit(app.exec_())