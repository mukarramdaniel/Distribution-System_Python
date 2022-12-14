class Shoe:
    
    def __init__(self,category,buyPrice,profitMargin,shoeSize,selPrice,color,prodID) -> None:
        self.__prodID=prodID
        self.__category=category
        self.__buyPrice=buyPrice
        self.__profitMargin=profitMargin
        self.__shoeSize=shoeSize
        self.__selPrice=selPrice
        self.__color=color
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
    def getprodID(self):
        return self.__prodID