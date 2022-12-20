from Core.User import User
from Core.Employee import Employee

class SaleAgent(Employee):
    def __init__(self,userT,salary, attendenceDate):
        super().__init__(userT,salary)
        self.attendenceDate=attendenceDate
    def getUsername(self):
        return self.userName