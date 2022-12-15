import sys
sys.path.insert(2,"Core")
from Core import Shoe
from Core.ProductList import ProducList

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None

class StockOrder_DL:
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
        return self.linklist
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
            
    def getDLinklist(self):
        return self.head
    def Print_List(self,node):
        while(node!=None):
            print(" {}".format(node.data))
            node=node.next
        
    def loadFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()    

        mycursor.execute("SELECT prodCategory,buyPrice,profitMargin,shoeSize,selPrice,color,prodID,type,orderID,date,status FROM stock_order_crud")

        myresult = mycursor.fetchall()
        id=1
        date=""
        temp=[]
        while(True):
            flag=False
            
            temp=[]
            for x in myresult:
                if(x[8]==id):
                    flag=True
                    date=x[9]
                    status=x[10]
                    shoe=Shoe.Shoe(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
                    temp.append(shoe)
            if(flag):
                order=ProducList(id,date,temp,status)
                self.Insert(order) 
            if(flag==False):
                break
            id +=1       
            
        mydb.close()
    def generateOrderID(self):
        count=0
        alter=self.head
        while(alter!=None):
            count +=1
            alter=alter.next
        return count+1
    