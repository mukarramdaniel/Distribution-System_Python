from Core.User import User
from Core.Employee import Employee

class SaleAgent(Employee):
    def __init__(self,userT,resetToken,attendenceDate):
        super().__init__(userT,resetToken)
        self.attendenceDate=attendenceDate
    def getUsername(self):
        return self.userName