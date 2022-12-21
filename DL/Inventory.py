import sys
sys.path.insert(1,"Core")
from Core.Shoe import Shoe
from Core.Order import Order
class Inventory:
  
    def __init__(self):
        self.size = 13
        self.hashTable = self.createHashTable()
  
    def createHashTable(self):
        return [[] for _ in range(self.size)]
    def setProduct(self,key,value):
        keyFound = False
        hashedKey = hash(key) % self.size
        bucket = self.hashTable[hashedKey]
        bucket.append((key,value))
        
    def getItem(self, key,size,color,price):
        
        hashed_key = self.getHash()
          
        bucket = self.hashTable[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val.getShoeSize()==size and record_val.getColor()==color and record_val.getBuyPrice()==price:
                found_key = True
                break
  
        if found_key:
            return record_val
        else:
            return None
    def getHash(self,key):
        hashed_key = hash(key) % self.size
        return hashed_key
        
    def deleteItem(self, key, value):
        
        hashed_key = hash(key) % self.size
          
        bucket = self.hashTable[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val==value:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    def getInventoryStock(self):
        return self.hashTable
    def getShoe(self,quant,category,color,type):
        quantity=int(quant)
        i=self.getHash(category)
        cart=[]
        for product in self.hashTable[i]:
            if(product[0]==category):
                prod=product[1]
                
                if(quantity>0):
                    if(category==prod.getProductCategory(),color==prod.getColor(),type==prod.getType()):
                        #prod.remove(prod)
                        cart.append(prod)
                        quantity -=1
        if(quantity==0):
            return cart
        else:
            return None
    def deductFromInventory(self,quant,category,color,type):
        quantity=int(quant)
        cart=[]
        tup=[]

        i=self.getHash(category)
        list=self.hashTable[i]
        for product in list:
            
            if(product[0]==category):
                prod=product[1]
                
                if(quantity>0):
                    if(category==prod.getProductCategory(),color==prod.getColor(),type==prod.getType()):
                        cart.append(prod)
                        tup.append(product)
                        quantity -=1
        if(quantity==0):
            for pro in tup:
                self.hashTable[i].remove(pro)
            return cart
                
        else:
            return None          
                  
    def readFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
    

        mycursor = mydb.cursor()

        mycursor.execute("SELECT prodCategory,buyPrice,profitMargin,shoeSize,selPrice,color,prodID,type FROM inventory")

        myresult = mycursor.fetchall()
        for x in myresult:
            prodCategory=x[0]
          
            shoe=Shoe(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
            self.setProduct(x[0],shoe)            
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
        mycursor.execute("TRUNCATE TABLE inventory")
        mydb.commit()
        sql = "INSERT IGNORE INTO inventory(prodCategory,buyPrice,profitMargin,shoeSize,selPrice,color,prodID,type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)  "
        for bucket in self.hashTable:
            if(bucket!=None):
                for prod in bucket:
                    shoe=prod[1]
                    val = (shoe.getProductCategory(),shoe.getBuyPrice(),shoe.getProfirMargin(),shoe.getShoeSize(),shoe.getSellPrice(),shoe.getColor(),shoe.getprodID(),shoe.getType())
                    mycursor.execute(sql,val)
                    mydb.commit()
        mydb.close()
        print("Inserted") 
