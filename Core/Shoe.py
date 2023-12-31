class Shoe:
    
    def __init__(self,category,buyPrice,profitMargin,shoeSize,selPrice,color,prodID,type) -> None:
        self.__prodID=prodID
        self.__category=category
        self.__buyPrice=buyPrice
        self.__profitMargin=profitMargin
        self.__shoeSize=shoeSize
        self.__selPrice=selPrice
        self.__color=color
        self.__type=type
    def __iter__(self):
        return self
    def getProductCategory(self):
        return self.__category
    def setProfirMargin(self,profit):
        self.__profitMargin=profit
    def getProfirMargin(self):
        return self.__profitMargin
    def setSellPrice(self,price):
        self.__selPrice=price
    def getSellPrice(self):
        return self.__selPrice
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color
    def getShoeSize(self):
        return self.__shoeSize
    def setShoeSize(self,size):
        self.__shoeSize=size
    def getBuyPrice(self):
        return self.__buyPrice
    def setBuyPrice(self,price):
        self.__buyPrice=price
    def getprodID(self):
        return self.__prodID
    def setprodID(self,prodID):
        self.__prodID=prodID
    def getType(self):
        return self.__type
    def setType(self,type):
        self.__type=type