from Core.User import User
class Employee(User):
    def __init__(self,userT,salary) -> None:
        super().__init__(userT)
        self._salary=salary
        self.salary_status = 0
    def getSalary(self):
        return self._salary
    def setSalary(self,salary):
        self._salary=salary
    def set_s_status (self , Flag):
        self.salary_status = Flag
    def get_s_status(self):
        return self.salary_status