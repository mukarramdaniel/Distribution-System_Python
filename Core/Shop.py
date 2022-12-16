class Shop:
    def __init__(self,riderID,name,Cnic,Email,location,phoneNum,accountNo,fieldArea,shopName,openTime,closeTime,created_on):
        self.__riderID=riderID
        self.__Cnic=Cnic
        self.__name=name
        self.__Email=Email
        self.__phoneNum=phoneNum
        self.__openTime=openTime
        self.__closeTime=closeTime
        self.__accountNo=accountNo
        self.__created_on=created_on
        self.__accountNo=accountNo
        self.__shopName=shopName
        self.__location=location
        self.__fieldArea=fieldArea
    def getShopName(self):
        return self.__shopName
    def setShopName(self,shopName):
        self.__shopName=shopName
    def getriderID(self):
        return self.__riderID
    def setriderID(self,riderID):
        self.__riderID=riderID
    def getCnic(self):
        return self.__Cnic
    def setCnic(self,Cnic):
        self.__Cnic=Cnic
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    def getlocation(self):
        return self.__location
    def setlocation(self,location):
        self.__location=location
    def getfieldArea(self):
        return self.__fieldArea
    def setfieldArea(self,fieldArea):
        self.__fieldArea=fieldArea
    def getEmail(self):
        return self.__Email
    def setEmail(self,Email):
        self.__Email=Email
    def getphoneNum(self):
        return self.__phoneNum
    def setphoneNum(self,phoneNum):
        self.__phoneNum=phoneNum
    def getopenTime(self):
        return self.__openTime
    def setopenTime(self,openTime):
        self.__openTime=openTime
    def getcloseTime(self):
        return self.__closeTime
    def setcloseTime(self,closeTime):
        self.__closeTime=closeTime
    def getaccountNo(self):
        return self.__accountNo
    def setaccountNo(self,accountNo):
        self.__accountNo=accountNo
    def getaccountNo(self):
        return self.__accountNo
    def setaccountNo(self,accountNo):
        self.__accountNo=accountNo
    def getcreated_on(self):
        return self.__created_on
    def setcreated_on(self,created_on):
        self.__created_on=created_on
    