class Shop:
    def __init__(self,riderID,name,Cnic,Email,location,phoneNum,accountNo,fieldArea,openTime,closeTime,created_on,update_on):
        self.__riderID=riderID
        self.__Cnic=Cnic
        self.__name=name
        self.__Email=Email
        self.__phoneNum=phoneNum
        self.__openTime=openTime
        self.__closeTime=closeTime
        self.__accountNo=accountNo
        self.__created_on=created_on
        self.__update_on=update_on
        self.__accountNo=accountNo
        self.__location=location
        self.__fieldArea=fieldArea
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
    