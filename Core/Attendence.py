
class Attendence:
    __userID=None
    __dateTimeList=None
    def __init__(self,userID,dateList):
        self.userID=userID
        self.dateList=dateList
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
    