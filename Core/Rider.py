from Core.User import User
class Rider(User):
    def __init__(self,userT,salary ,salary_status):
        super().__init__(userT)
        self.fieldArea=""
        self.salary=salary
        self.vehicle = None#vehicle object
        self.startLocation = None#location object
        self.salary_status = salary_status
    def getSalary(self):
        return self._salary
    def setSalary(self,salary):
        self._salary=salary
    def set_s_status (self , Flag):
        self.salary_status = Flag
    def get_s_status(self):
        return self.salary_status
