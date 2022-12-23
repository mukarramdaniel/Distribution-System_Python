import sys
from Rider import *
#from Maps.maps import distance_between_places,getLocation
from Maps.SelectShop import * 
from Core.Shop import Shop
from DL.ShopCRUD import *
from Maps.maps import *
from PyQt5 import QtWidgets
from DL.UserCRUD import *
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
from datetime import datetime
from DL.Inventory import Inventory
from DL.OrderCRUD import *
from Maps.Graph import Graph
import folium
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
class RiderMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_RiderWindow()
        self.riderID="3130258066433"
        
        self.orderDL=RiderOrders()
        self.orderDL.loadFromTable()
        self.ui.setupUi(self)
        self.CartDL=Cart()
        self.CartDL.loadFromTable()
        self.cart=self.CartDL.getCart()
        self.shopDL=ShopCRUD()
        self.shopDL.loadFromTable()
        self.inventory=Inventory()
        self.inventory.readFromTable()
        self.cartProducts=None
        self.Shoes=None
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

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_62.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_68.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Account_Widget.setGraphicsEffect(self.shadow)

        self.ui.menuBtn_8.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_11.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_7.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_9.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_10.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_12.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_13.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_14.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn_8.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_11.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_7.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_9.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_10.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_12.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_13.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_14.clicked.connect(lambda: self.SlideRightMenu())

        self.ui.btn_Dashboard.clicked.connect(lambda: self.OpenDashBoard())
        self.ui.btn_AddShop.clicked.connect(lambda: self.OpenAddShop())
        self.ui.btn_TakeOrder.clicked.connect(lambda: self.OpenTakeOrder())
        #self.ui.btn_DeliverOrder.clicked.connect(lambda: self.OpenDeliverOrder())
        self.ui.btn_ViewStock_2.clicked.connect(lambda: self.OpenViewStock())
        self.ui.btn_FuelDetails.clicked.connect(lambda: self.OpenFuelDetails())
        self.ui.btn_ToDoList.clicked.connect(lambda: self.OpenTodoList())
        self.ui.btn_History.clicked.connect(lambda: self.OpenHistory())
        self.ui.btn_AddShop.clicked.connect(lambda: self.addShopMenu())
        self.ui.btn_Add.clicked.connect(lambda: self.addShop())
        self.ui.btn_Map.clicked.connect(lambda: self.selectShopMap())
        self.ui.btn_AddtoCart_2.clicked.connect(lambda: self.addToCart())
        self.ui.comboBox.currentIndexChanged.connect(self.showShopSummary)
        self.ui.btn_ConfirmOrder_2.clicked.connect(self.confirmOrder)
        self.ui.btn_deliverOrder.clicked.connect(self.deliverOrder)
        self.ui.btn_viewlocation.clicked.connect(lambda: self.todayRoute())
        
        
        
        
        
        
        
        self.show()
    def deliverOrder(self):
        pass
    
    def todayRoute(self):
        routeList=self.makeShortestRoute()
        self.todayMap(routeList)   
    def confirmOrder(self):
        prodsCart=[]
        if(len(self.temp)!=0):#temp is list the cart item of that shop to avoid again checkking of shop ordercart
            if(self.ui.tableWidget_Cart.rowCount()!=0):
                for idx in self.temp:
                    prod=self.cart[idx]
                    #quantity,category,color,type
                    
                    prodsCart=self.inventory.deductFromInventory(prod[1],prod[0],prod[2],prod[4])+prodsCart
                
                if(prodsCart):
                    self.addIntoOrders(prodsCart,prod[5])#orderiD=>shopID for that scenerio
                    self.temp.remove(idx)#temp int elemet(idx) stored delete whose orderdone
                    del self.cart[idx]#del from cart whole index stored in temp
                    self.CartDL.updateTable()
                    self.inventory.updateTable()
                        
        self.showInCart()
                
                        
                    #shoes that are in cart object list
                    
                
    def addIntoOrders(self,prodsCart,shopID):
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M:%S")
        orderID=len(self.orderDL.queue)+1
        riderID=self.riderID
        order=ProducList(orderID,date,[],1)
        order.setriderID(riderID)
        order.shopID=shopID
        for i in prodsCart:
            order.addShoeInList(i)
        self.orderDL.enqueue(order)
        self.orderDL.updateTable()
    def showShopSummary(self):
        checkShop=self.ui.comboBox.currentText()
        shops=self.shopDL.getList()
        while(shops!=None):
            if(checkShop==shops.getData().getShopName()):
                self.ui.txt_Cnic_2.setText(shops.getData().getCnic())
                self.ui.txt_Email_2.setText(shops.getData().getEmail())
                self.ui.txt_Address_2.setText(shops.getData().getlocation().getaddress())
                self.shopID=shops.getData().getCnic()
                self.ui.txt_PhoneNumber_2.setText(shops.getData().getphoneNum())
                self.ui.txt_Shop_2.setText(shops.getData().getShopName())
                break
            
            shops=shops.next
        self.showInCart()
        
    def selectShopMap(self):
        #pass
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui=MapViewer()
        self.ui.show()
    def OpenFuelDetails(self):
        self.ui.mainBody.setCurrentIndex(7)
        
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
        created_on = now.strftime("%Y-%m-%d %H:%M:%S")
        shop=Shop(self.riderID,name,cnic,email,location,PhoneNumber,AccountNo,Area,shopName,openTime,closeTime,created_on)
        self.shopDL.Insert(shop)
        self.shopDL.updateTable()
    def OpenDashBoard(self):
        self.ui.mainBody.setCurrentIndex(3)
    def OpenAddShop(self):
        self.ui.mainBody.setCurrentIndex(4)
        
    def OpenTakeOrder(self):
        self.ui.mainBody.setCurrentIndex(1)
        cmb=[]
        shops=self.shopDL.getList()
        while(shops!=None):
            cmb.append(shops.getData().getShopName())
            shops=shops.next
        self.ui.comboBox.addItems(cmb)
        self.ui.lineEdit_2.clear()#setting on screen
        
        
        
       
    def addToCart(self):
        self.inventory.getInventoryStock()
        shopName=self.ui.comboBox.currentText()
        category=self.ui.cmb_Category_2.currentText()
        quantity=self.ui.spb_Quantity_2.text()
        color=self.ui.cmb_Color_2.currentText()
        type=self.ui.cmb_type.currentText()
        self.Shoes=self.inventory.getShoe(quantity,category,color,type)#shoes that are in cart object list
        if(self.Shoes!=None):
            subTotal=self.calculateSubTotal(self.Shoes)# calculating subtotal of cart
            self.ui.lineEdit_2.setText(str(subTotal))#setting on screen
            self.CartDL.addIntoCart((category,int(quantity),color,type,subTotal,self.shopID))
            self.ui.tableWidget_Cart.setRowCount(len(self.cart))#setting row count of ui_datatable
            self.showInCart()
            self.CartDL.updateTable()#updating databasetable
        else:
            msg_box = QMessageBox()
            msg_box.setText("Item Unavailable")
            msg_box.setWindowTitle("Caution") 
        self.clearFields()  
    def clearFields(self):
        self.ui.cmb_Category_2.clearEditText()
        self.ui.spb_Quantity_2.clearMask()
        self.ui.cmb_type.clearEditText()
        self.ui.cmb_Color_2.clearMask()
    def calculateSubTotal(self,Shoes):
        total=0
        for shoe in Shoes:
            total +=shoe.getSellPrice()
        return total
               
    def showInCart(self):
        rowCount=0
        self.temp=[] 
        for idx,i in enumerate(self.cart):
            if(self.shopID==str(i[5])):
                self.temp.append(idx)
                rowCount +=1
        self.ui.tableWidget_Cart.clearContents()
        self.ui.tableWidget_Cart.setRowCount(rowCount)
        
        row=0
        self.total=0
        for j in self.temp:
            i=self.cart[j]
            self.ui.tableWidget_Cart.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_Cart.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[2])))
            self.ui.tableWidget_Cart.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i[3])))
            self.ui.tableWidget_Cart.setItem(row, 3, QtWidgets.QTableWidgetItem(str(i[4])))
            self.total +=int(i[4])
            row +=1
        self.ui.txt_Total.setText(str(self.total))
        
        
    def OpenDeliverOrder(self):
        self.ui.mainBody.setCurrentIndex(0)
    def OpenViewStock(self):
        self.ui.mainBody.setCurrentIndex(2)
    def OpenTodoList(self):
        self.ui.mainBody.setCurrentIndex(6)
        self.showInTodoTable()
    def showInTodoTable(self):
        import datetime as datetime
        orders=self.orderDL.getList()
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.ui.tableWidget_ToDoList.setRowCount(len(orders))
        row=0
        for order in orders:
            if(order.getDate().split(" ")[0]==str(yesterday) and order.getriderID()==self.riderID):
                info=self.shopDL.getShopName(order.shopID)#info name annd phione
                if(info):
                    self.ui.tableWidget_ToDoList.setItem(row, 0, QtWidgets.QTableWidgetItem(str(info[0])))
                    self.ui.tableWidget_ToDoList.setItem(row, 1, QtWidgets.QTableWidgetItem(str(order.getDate())))
                    self.ui.tableWidget_ToDoList.setItem(row, 2, QtWidgets.QTableWidgetItem(str(info[1])))
                    total=order.calculatePrice()
                    self.ui.tableWidget_ToDoList.setItem(row, 3, QtWidgets.QTableWidgetItem(str(info[2])))
                    self.ui.tableWidget_ToDoList.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total)))

                row +=1
                    
                
            
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
    def makeShortestRoute(self):
        graph=Graph()
        
        for order in self.orderDL.getList():
            if(order.riderID==self.riderID):
                coords=self.shopDL.getLatiLongi(order.shopID)
                if(coords):
                    graph.addNode(coords.getLatitude(),coords.getLongitude())
        graph.makeCompleteGraph()
        graph.calculateMST()
        mst=graph.returnMST()
        return mst
                

    def todayMap(self,mst):
        import folium
        api_key = 'AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0'
        start = mst[0]
        end = mst[len(mst)-1]
        
        #waypoints = [(float(31.57552403504949), float(74.35429530639927)), (float(31.55043477797966), float(74.31304116179827))]
        gmaps = googlemaps.Client(key=api_key)
        route = gmaps.directions(start, end, waypoints=mst, mode='driving')
        polyline = route[0]['overview_polyline']['points']
        path = googlemaps.convert.decode_polyline(polyline)
        path1=[]
        for i in path:
            coord_list = [(lng, lat) for lng, lat in i.items()]
            path1.append((coord_list[0][1],coord_list[1][1]))
        m = folium.Map(location=mst[0],zoom_start=1000)
        for i in mst:
            folium.Marker(location=[i[0],i[1]], popup=" ").add_to(m)
        folium.PolyLine(path1, color='red', weight=3, opacity=0.6).add_to(m)
        m.save('map.html')
        from PyQt5.QtWidgets import QApplication, QWidget
        app = QApplication([])
        self.ui.window = QMainWindow()
        webview = QWebEngineView()
        self.window = QMainWindow()
        self.window.setCentralWidget(webview)
        webview.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
        window.show()
        app.exec_()
        
        
        # Load a webpage


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=RiderMainWindow()
    window.show()
    sys.exit(app.exec_())
