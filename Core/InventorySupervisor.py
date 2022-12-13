from Core.User import User
from Core.Employee import Employee
class InventorySupervisor(Employee):
    def __init__(self,userT,resetToken,attendenceDate):
        super().__init__(userT,resetToken)
        self.attendenceDate=attendenceDate
        