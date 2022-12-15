class User:
    _userId=None
    _userName=None
    _password=None
    _userRole=None
    _name=None
    _age=None
    _contactNum=None
    _Email=None
    _CNIC=None
    _BankAccount=None
    _createdDate=None
    _createdDate=None
    _updatedDate=None
    
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
        
        
