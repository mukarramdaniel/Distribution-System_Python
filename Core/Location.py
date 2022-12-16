class Location:
    def __init__(self,latitude,longitude,address) -> None:
        self.__latitude=latitude
        self.__longitude=longitude
        self.__address=address
    def getLatitude(self):
        return self.__latitude
    def getLongitude(self):
        return self.__longitude
    def setLatitude(self,latitude):
        self.__latitude=latitude
    def setLongitude(self,longitude):
        self.__longitude=longitude
    def getaddress(self):
        return self.__address
    def setaddress(self,address):
        self.__address=address
        