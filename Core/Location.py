import math
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
    def distance_to(self, other):
        
        R = 6371 
        lati = math.radians(other.latitude-self.latitude)
        longi = math.radians(other.longitude-self.longitude)
        a = math.sin(lati/2) * math.sin(lati/2) + math.cos(math.radians(self.latitude)) * math.cos(math.radians(other.latitude)) * math.sin(longi/2) * math.sin(longi/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c 
        return d
        