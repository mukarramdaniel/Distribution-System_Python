class ProducList:
    def __init__(self,orderID,date,ShoeList,status) -> None:
        self.orderID=orderID
        self.__status=status
        self.date=date
        self.ShoeList=ShoeList
        self.riderID=None
    def addShoeInList(self,shoe):
        self.ShoeList.append(shoe)
    def getShoeList(self):
        return self.ShoeList
    def shoeExistinList(self,shoe):
        if shoe in self.ShoeList:
            return True
        return False
    def setStatus(self,status):
        self.__status=status
    def getStatus(self):
        return self.__status
    def getOrderID(self):
        return self.orderID
    def getDate(self):
        return self.date
    def getriderID(self):
        return self.riderID
    def setriderID(self,riderID):
        self.riderID=riderID
    
         