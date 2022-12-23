from Core.User import User
class Rider(User):
    def __init__(self,userT,salary ,salary_status):
        super().__init__(userT)
        self.fieldArea=""
        self.salary=salary
        self.vehicle = None#vehicle object
        self.startLocation = None#location object
        self.latitude = 0
        self.longitude = 0
        self.salary_status = salary_status
    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        self.salary=salary
    def set_s_status (self , Flag):
        self.salary_status = Flag
    def get_s_status(self):
        return self.salary_status
    def set_fieldarea (self, area) :
        self.fieldArea = area
    def set_vehicle (self, vehic) :
        self.vehicle = vehic
    def getFieldarea (self) :
        return self.fieldArea
    def getVehicle(self) :
        return self.vehicle
    def getLatitude(self) :
        return self.latitude
    def getLongitude(self) :
        return self.longitude
