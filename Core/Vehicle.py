class Vehicle:
    def __init__(self,model,number,fuelAverage) :
        self.model=model
        self.number=number
        self.fuelAverage=fuelAverage
        self.riderID=None
   
    def setRider(self,rider):
        self.riderID=rider