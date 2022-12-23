class User:
    def __init__(self,userT):
        self.userId=userT[0]
        self.userName=userT[1]
        self.password=userT[2]
        self.userRole=userT[3]
        self.name=userT[4]
        self.age=userT[5]
        self.contactNum=userT[6]
        self.Email=userT[7]
        self.CNIC=userT[8]
        self.BankAccount=userT[9]
        self.createdDate=userT[10]
        self.updatedDate=userT[11]
    def getUserName(self) :
        return self.userName
    def getName(self):
        return self.name   
    def getUserRole(self) :
        return self.userRole
    def getID(self) :
        return self.userId
    def getAge(self) :
        return self.age
    def getnumber(self) :
        return self.contactNum
    def getCNIC(self) :
        return self.CNIC
    def getbankaccount(self) :
        return self.BankAccount
    def getcreatedDate(self) :
        return self.createdDate
    def getupdatedDate(self) :
        return self.updatedDate
    def getpassword(self) :
        return self.password
    def getmail(self) :
        return self.Email
        
