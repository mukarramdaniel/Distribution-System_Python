from User import User;
class Driver(User):
    def __init__(self,userT,resetToken):
        super().__init__(userT)
        fieldArea=""
        adjList=[]
        self.resetToken=resetToken
        startLocation=[]
        fuelRecord=[]

