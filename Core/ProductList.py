class ProducList:
    def __init__(self,orderID,date,ShoeList) -> None:
        self.orderID=orderID
        self.__status=0
        self.date=date
        self.ShoeList=ShoeList
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