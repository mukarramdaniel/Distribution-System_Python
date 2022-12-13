import sys
sys.path.insert(1,"Core")
from Core.Shoe import Shoe
from Core.ProductList import ProducList
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
        
        hashed_key = hash(key) % self.size
          
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
    def deleteItem(self, key, value):
        
        hashed_key = hash(key) % self.size
          
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val==value:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    def readFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT prodCategory,buyPrice,profitMargin,shoeSize,sellPrice,color,prodID")

        myresult = mycursor.fetchall()
        for x in myresult:
            prodCategory=x[1]
          
            shoe=Shoe(x[1],x[2],x[3],x[4],x[5],x[6],x[0])
            
           # print(self.verify(userName,"admin"))
        mydb.close()
