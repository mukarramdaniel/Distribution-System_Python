from Core.User import User
class Rider(User):
    def __init__(self,userT,salary):
        super().__init__(userT)
        fieldArea=""
        self.salary=salary
        vehicle=None#vehicle object
        startLocation=None#location object
        

