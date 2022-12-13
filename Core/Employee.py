from Core.User import User
class Employee(User):
    def __init__(self,userT,salary) -> None:
        super().__init__(userT)
        self._salary=salary
    def getSalary(self):
        return self._salary
    def setSalary(self,salary):
        self._salary=salary