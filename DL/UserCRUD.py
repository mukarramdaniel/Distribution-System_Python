import sys
sys.path.insert(2,"Core")
from Core.Manager import Manager
from Core.InventorySupervisor import InventorySupervisor
from Core.SaleAgent import SaleAgent
from Core.Rider import Rider

# from Core.Rider import Rider
# from Core.SaleAgent import SaleAgent

class UserCRUD:
  
    def __init__(self):
        self.size = 29
        self.hashTable = self.createHashTable()
  
    def createHashTable(self):
        return [[] for _ in range(self.size)]
    def getHashTable(self):
        return self.hashTable
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
    def getUserReturn(self, key):
        hashed_key = hash(key) % self.size
          
        bucket = self.hashTable[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key:
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
    def deleteUser(self, key, value):
        
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
        othercursor=mydb.cursor()
        ridercursor = mydb.cursor()
        mycursor.execute("SELECT userID,userName,password,userRole,name,age,contactNum,Email,Cnic,bankAccount,resetToken,created_on,update_on  FROM manager")

        myresult = mycursor.fetchall()
        for x in myresult:
            userName=x[1]
            user=Manager((x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[11],x[12]),x[10])
            
            self.setUser(userName,user)
        
        othercursor.execute("SELECT userID,userName,password,userRole,name,age,contactNum,Email,Cnic,bankAccount,salary,created_on,update_on,dateTime,Salary_Status  FROM employee")
        myEmployee=othercursor.fetchall()
        for x in myEmployee:
            userName1=x[1]
            if(int(x[3])==1):
                user=InventorySupervisor((x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[11],x[12]),x[10],x[13])
                user.set_s_status(x[14])
            if(int(x[3])==2):
                user=SaleAgent((x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[11],x[12]),x[10],x[13])
                user.set_s_status(x[14])
            self.setUser(userName1,user)
        ridercursor.execute("SELECT userID,userName,password,userRole,name,age,contactNum,Email,Cnic,bankAccount,resetToken,created_on,updated_on,date,time,latitude,longitutde,fieldArea,VehicleNumber  FROM rider")
        myrider = ridercursor.fetchall()
        for x in myrider :
            userName1=x[1]
            if(int(x[3])==3):
                user=Rider((x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[11],x[12]),x[10],x[13])
                user.set_s_status(x[14])
                user.set_fieldarea(x[17])
            self.setUser(userName1,user)
        mydb.close()
    def insert_rider (self) :
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        mycursor.execute("TRUNCATE TABLE rider")
        mydb.commit()
        sql = "INSERT INTO rider(userName,password,userRole,name,age,contactNum,Email,Cnic,bankAccount,resetToken,created_on,updated_on,date,time,latitude,longitutde,fieldArea,VehicleNumber) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for bucket in self.hashTable:
            if(bucket!=None):
                for rider in bucket:
                    if (rider[1].getUserRole() == '3') :
                        obj = rider[1]
                        val = (obj.getUserName() , obj.getpassword() , obj.getUserRole() , obj.getName() ,obj.getAge() , obj.getnumber() , obj.getmail() , obj.getCNIC() , obj.getbankaccount() , obj.getSalary() , obj.getcreatedDate() , obj.getupdatedDate() ,obj.get_s_status(), "" , float(obj.getLatitude()) , float(obj.getLongitude()) ,obj.getFieldarea() , obj.getVehicle())
                        mycursor.execute(sql,val)
                        mydb.commit()
        mydb.close()
        print("Inserted") 
        
   
