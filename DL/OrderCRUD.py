from Core.ProductList import *
from Core.Shoe import Shoe
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


 
class RiderOrders:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return not bool(self.queue)

    
    def loadFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT prodCategory,buyPrice,profitMargin,shoeSize,selPrice,color,prodID,type,orderID,date,status,riderID,shopID FROM riderorder")

        my = list(mycursor.fetchall())
        myprods = list(map(list , my))
        print(myprods)
        for prod in myprods :
            order=prod[8]
            if (order != None) :
                status=prod[10]
                riderID=prod[11]
                shopID=prod[12]
                order=ProducList(prod[8],prod[9],[],status)
                order.setriderID(riderID)
                order.shopID=shopID
            else:
                order=None
            for j in myprods :
                if (prod[8]== order and prod[8]!=None) :
                    prod[8] = None
                    order.addShoeInList(Shoe(prod[0],prod[1],prod[2],prod[3],prod[4],prod[5],prod[6],prod[7]))
            if(order!=None)        :
                self.enqueue(order)
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
        mycursor.execute("TRUNCATE TABLE riderorder")
        mydb.commit()
        
        sql = "INSERT IGNORE INTO riderorder(prodCategory,buyPrice,profitMargin,shoeSize,selPrice,color,prodID,type,orderID,date,status,riderID,shopID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  "
        while(self.is_empty()==False):
            
            productlist=self.dequeue()
            date=productlist.getDate()
            status=productlist.getStatus() 
            riderID=productlist.getriderID()   
            orderID=productlist.getOrderID()
            shoes=productlist.getShoeList()
            for shoe in shoes:
                val = (shoe.getProductCategory(),shoe.getBuyPrice(),shoe.getProfirMargin(),shoe.getShoeSize(),shoe.getSellPrice(),shoe.getColor(),shoe.getprodID(),shoe.getType(),orderID,date,status,riderID,productlist.shopID)
                mycursor.execute(sql,val)
                mydb.commit()
        mydb.close()
        print("Inserted") 
            
class Cart:
    def __init__(self) -> None:
        self.cart=None
    def addIntoCart(self,cart):
        self.cart.append(cart)
    def getCart(self):
        return self.cart
    def loadFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()    

        mycursor.execute("SELECT category, quantity, color, type,total,orderID  FROM cart")

        myresult = mycursor.fetchall()
        self.cart=list(map(list, myresult))
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
        mycursor.execute("TRUNCATE TABLE cart")
        mydb.commit()
        sql = "INSERT IGNORE INTO cart(category, quantity, color, type,total,orderID ) VALUES (%s,%s,%s,%s,%s,%s)  "
        for ca in self.cart:
            val = (ca[0],ca[1],ca[2],ca[3],ca[4],ca[5])
            mycursor.execute(sql,val)
            mydb.commit()
        mydb.close()
        
        
    
        
