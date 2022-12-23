import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
from datetime import datetime
from Core.Rider import Rider
from DL.UserCRUD import UserCRUD
from Sales_Agent import *


class SalesAgentMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_SalesAgentWindow()
        self.ui.setupUi(self)
        self.userDL = UserCRUD()
        self.userDL.readFromTable()
        self.ui.btn_Add.clicked.connect(lambda: self.assign_location())
        self.ui.btn_AssignVehicle_2.clicked.connect(lambda: self.assign_vehicle())
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_4.setGraphicsEffect(self.shadow)
        self.rider_displays(self.ui.cmb_Rider)
        self.rider_displays(self.ui.cmb_rider)
        self.vehicle_display()
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
        self.ui.widget_12.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame.setGraphicsEffect(self.shadow)

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
        self.ui.widget_47.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_52.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_53.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_67.setGraphicsEffect(self.shadow)

        self.ui.menuBtn_10.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn_10.clicked.connect(lambda: self.SlideRightMenu())

        self.ui.btn_Dashboard.clicked.connect(lambda: self.OpenDashBoard())
        self.ui.btn_AssignLocation.clicked.connect(lambda: self.OpenAssignLocation())
        self.ui.btn_AssignVehicle.clicked.connect(lambda: self.OpenAssignVehicle())
        self.ui.btn_ViewCashbook.clicked.connect(lambda: self.OpenViewCashbook())
        self.ui.btn_TrackOrder.clicked.connect(lambda: self.OpenTrackOrder())

        self.show()
    def OpenTrackOrder(self):
        self.ui.mainBody.setCurrentIndex(1)
    def OpenViewCashbook(self):
        self.ui.mainBody.setCurrentIndex(4)
    def OpenAssignVehicle(self):
        self.ui.mainBody.setCurrentIndex(0)
        self.load_ViewRider_table1()
    def OpenAssignLocation(self):
        self.ui.mainBody.setCurrentIndex(3)
        self.load_ViewRider_table()
    def OpenDashBoard(self):
        self.ui.mainBody.setCurrentIndex(2)
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
    def rider_displays (self,a) :
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        query = 'SELECT name FROM rider'
        mycursor.execute(query)
        rows = mycursor.fetchall()
        column_list = [row[0] for row in rows]
        mydb.close()
        a.addItems(column_list)
    def vehicle_display (self) :
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        query = 'SELECT number FROM vehicle'
        mycursor.execute(query)
        rows = mycursor.fetchall()
        column_list = [row[0] for row in rows]
        mydb.close()
        self.ui.cmb_Vehicle.addItems(column_list)
    def get_object (self , name) :
        for i in self.userDL.getHashTable():
            for j in i :
                if(j!=None):
                    if (str(j[1].getName()) == name) :
                        print(j[0])
                        obj = self.userDL.getUserReturn(j[0])
                        return obj
    def assign_location (self) :
        obj = self.get_object(self.ui.cmb_rider.currentText())
        obj.set_fieldarea(self.ui.cmb_location.currentText())
        self.userDL.insert_rider()
        self.load_ViewRider_table()
    def assign_vehicle (self) :
        obj = self.get_object(self.ui.cmb_Rider.currentText())
        obj.set_vehicle(self.ui.cmb_Vehicle.currentText())
        self.userDL.insert_rider()
        self.load_ViewRider_table1()
    def load_ViewRider_table (self) :
        row = 0
        self.ui.tableWidget_ViewRider.setRowCount(self.Get_Table_Row_Length())
        for i in self.userDL.getHashTable():
            for j in i :
                if(j!=None):
                    if(j[1].getUserRole()== '3'):
                            self.ui.tableWidget_ViewRider.setItem(row, 0, QtWidgets.QTableWidgetItem(str(j[0])))
                            self.ui.tableWidget_ViewRider.setItem(row, 1, QtWidgets.QTableWidgetItem(str(j[1].getID())))
                            self.ui.tableWidget_ViewRider.setItem(row, 2, QtWidgets.QTableWidgetItem(str(j[1].getName())))
                            if (j[1].getFieldarea() != "") :
                                self.ui.tableWidget_ViewRider.setItem(row, 3, QtWidgets.QTableWidgetItem(str(j[1].getFieldarea())))
                            else :
                                self.ui.tableWidget_ViewRider.setItem(row, 3, QtWidgets.QTableWidgetItem("None"))
                            row = row+1
    def load_ViewRider_table1 (self) :
        row = 0
        self.ui.tableWidget_ViewRider_2.setRowCount(self.Get_Table_Row_Length())
        for i in self.userDL.getHashTable():
            for j in i :
                if(j!=None):
                    if(j[1].getUserRole()== '3'):
                            self.ui.tableWidget_ViewRider_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(j[1].getID())))
                            self.ui.tableWidget_ViewRider_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(j[1].getName())))
                            self.ui.tableWidget_ViewRider_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(j[1].getCNIC())))
                            if (j[1].getVehicle() != "") :
                                self.ui.tableWidget_ViewRider_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(j[1].getVehicle())))
                            else :
                                self.ui.tableWidget_ViewRider_2.setItem(row, 3, QtWidgets.QTableWidgetItem("None"))
                            row = row+1
                    


        

    def Get_Table_Row_Length(self):
        count=0
        for i in self.userDL.getHashTable():
            for j in i:
                if(j!=None and j[1].getUserRole() == "3"):
                    count+=1
        return count
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=SalesAgentMainWindow()
    window.show()
    sys.exit(app.exec_())