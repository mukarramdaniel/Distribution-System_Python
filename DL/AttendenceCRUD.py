class AttendenceCRUD:
    def __init__(self):
        self.listAttendence=[]
    def addIntoList(self,attendence):   #attendence object
        self.listAttendence.append(attendence)
    def getAttendancelist(self) :
        return self.listAttendence
    def insert_attendance(self) :
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO attendence(userName,name,date) VALUES (%s,%s,%s)"
        for i in self.listAttendence :
            for j in i.getAttendenceList() :
                val = (str(i.getUserID()), str(i.getName()),j)
                mycursor.execute(sql,val)
        mydb.commit()
        print("Inserted") 