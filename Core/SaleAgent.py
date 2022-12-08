from Employee import Employee
from User import User
class SaleAgent(Employee):
    def __init__(self,userT,resetToken,attendenceDate):
        super().__init__(userT,resetToken)
        self.attendenceDate=attendenceDate