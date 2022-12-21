import sys
sys.path.insert(1,"Core")
from Core.Shop import Shop
from Core.Location import Location



class Node:
    def __init__(self,val):
        self.__data=val
        self.next=None
        self.prev=None
    def getData(self):
        return self.__data
    def setData(self,data):
        self.__data=data
   

class ShopCRUD:
    def __init__(self):
        self.head=None
  
    def Insert_at_Head(self,val): # insert at head
        New_Node=Node(val)
        New_Node.next=self.head
        if(self.head != None):
            self.head.prev=New_Node
        self.head=New_Node
        New_Node.prev=None
    def getList(self):
        return self.head
    def Insert(self,val):
        New_Node=Node(val)
        last=self.head
        New_Node.next=None
        if(self.head==None):
            New_Node.prev=None
            self.head=New_Node
            return
        
        while(last.next!=None):
            last=last.next
        last.next=New_Node
        New_Node.prev=last
    
    def Insert_btw_Nodes(self,prev_Node,val):
        if(prev_Node==None):
            print("Previous node cannot be empty")
            return
        New_Node=Node(val)
        New_Node.next=prev_Node.next
        prev_Node.next=New_Node
        New_Node.prev=prev_Node
        if(New_Node.next!=None):
            New_Node.next.prev=New_Node

    def Delete(self,val):
        start=self.head
        Node_Deleted=False

        if(start==None):
            return
        elif(start.data==val): # deleting from start
            self.head=start.next
            return
        while(start!=None):
            if(start.data==val):
                break
            start=start.next
        if(start.next==None): #deleting from end
            start=start.prev
            start.next=None
        else:
            start.prev.next=start.next
            start.next.prev=start.prev
            

    def Print_List(self,node):
        while(node!=None):
            print(" {}".format(node.data))
            node=node.next
    def loadFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user2",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT riderID,name,Cnic,Email,latitude,longitude,address,phoneNum,accountNo,FieldArea,shopName,timeOpen,timeClose,created_on FROM shop")
        myresult = mycursor.fetchall()
        for x in myresult:
            loca=Location(x[4],x[5],x[6])
            shop=Shop(x[0],x[1],x[2],x[3],loca,x[7],x[8],x[9],x[10],x[11],x[12],x[13])
            self.Insert(shop)
        mydb.close()
    def updateTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        sql = "INSERT IGNORE INTO shop(riderID,name,Cnic,Email,latitude,longitude,address,phoneNum,accountNo,FieldArea,shopName,timeOpen,timeClose,created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  "
        shops=self.head
        while(shops!=None):
            shop=shops.getData()    
            val = (shop.getriderID(),shop.getname(),shop.getCnic(),shop.getEmail(),shop.getlocation().getLatitude(),shop.getlocation().getLongitude(),shop.getlocation().getaddress(),shop.getphoneNum(),shop.getaccountNo(),shop.getfieldArea(),shop.getShopName(),shop.getopenTime(),shop.getcloseTime(),shop.getcreated_on())
            mycursor.execute(sql,val)
            shops=shops.next
            mydb.commit()
        mydb.close()
        print("Inserted") 
