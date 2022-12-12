import sys
sys.path.insert(1,"E:\Final Term\ARM\cs261f22finalpid05")
sys.path.insert(1,"E:\Final Term\ARM\cs261f22finalpid05\Core")

from Core.Manager import Manager
# from Core.Rider import Rider
# from Core.SaleAgent import SaleAgent

class Inventory:
  
    def __init__(self):
        self.size = 29
        self.hashTable = self.createHashTable()
  
    def createHashTable(self):
        return [[] for _ in range(self.size)]
    def setUser(self,key,value):
        keyFound = False
        hashedKey = hash(key) % self.size
        bucket = self.hashTable[hashedKey]
        for index, record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                keyFound = True
                break
  
        if keyFound:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))
    def getUser(self, key,value):
        
        hashed_key = hash(key) % self.size
          
        bucket = self.hashTable[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val==value:
                found_key = True
                break
  
        if found_key:
            return record_val
        else:
            return None
    def verify(self, key,password):
        
        hashed_key = hash(key) % self.size
          
        bucket = self.hashTable[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val.password==password:
                found_key = True
                break
  
        if found_key:
            return record_val
        else:
            return None
    def deletUser(self, key, value):
        
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
    def storeIntoTable(self):
        pass
    def readFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT userID,userName,password,name,age,contactNum,Email,Cnic,bankAccount,resetToken,created_on,update_on  FROM manager")

        myresult = mycursor.fetchall()
        for x in myresult:
            userRole=0
            userName=x[1]
            user=Manager((x[0],x[1],x[2],userRole,x[3],x[4],x[5],x[6],x[7],x[8],x[10],x[11]),x[9])
            self.setUser(userName,user)
           # print(self.verify(userName,"admin"))
