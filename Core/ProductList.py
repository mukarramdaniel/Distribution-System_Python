class ProducList:
    def __init__(self,category,ShoeList,productID) -> None:
        self.productID=productID
        self.category=category
        self.ShoeList=ShoeList
    def addShoeInList(self,shoe):
        self.ShoeList.append(shoe)
    def getShoeList(self):
        return self.ShoeList
    def shoeExistinList(self,shoe):
        if shoe in self.ShoeList:
            return True
        return False