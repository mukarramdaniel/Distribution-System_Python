from User import User;
class Rider(User):
    def __init__(self,userT,resetToken):
        super().__init__(userT)
        self._fieldArea=""
        self._adjList=[]
        self._resetToken=resetToken
        self._vehicle=None#vehicle object
        self._startLocation=None#location object
        self._fuelRecord=[]
    def __init__(self,userT,resetToken,fieldArea,vehicle,startLocation)
        super().__init__(userT)
    

