class Attendence:
    __userID=None
    __name = None
    __dateTimeList=None
    def __init__(self,userID , name):
        self.userID=userID
        self.name = name
    def addInDateTimeList(self,attendDate):
        self.dateList.append(attendDate)
    def getAttendenceList(self):
        return self.dateList
    def getUserID(self):
        return self.userID
    def setDateTimeList(self,dateList):
        self.dateList=dateList
    def setUserID(self,id):
        self.userID=id
    