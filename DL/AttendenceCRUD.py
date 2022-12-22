from Core.Attendence import Attendence
class AttendenceCRUD:
    def __init__(self):
        self.listAttendence=[]
    def addIntoList(self,attendence):   #attendence object
        self.listAttendence.append(attendence)
    def getAttendancelist(self) :
        return self.listAttendence
    def insert_attendance(self , listt) :
        from random import randint
        start = 10**(8-1)
        end = (10**8)-1
        code = str(randint(start,end))
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO attendence(userName,name,date,id) VALUES (%s,%s,%s,%s)"
        for i in listt :
            for j in i.getAttendenceList() :
                code = str(randint(start,end))
                val = (i.getUserID(), i.getname(),j,code)
                mycursor.execute(sql,val)
        mydb.commit()
    def readData (self) :
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT userName,name,date FROM attendence')
        my = list(mycursor.fetchall())
        myattendance = list(map(list , my))
        print(myattendance)
        for x in myattendance :
            username=x[0]
            if (username != "None") :
                att = Attendence(x[0] , x[1])
            else:
                att=None
            for j in myattendance :
                if (j[0] == username and j[0]!="None") :
                    j[0] = "None"
                    att.addInDateTimeList(j[2])
            if(att!=None)        :
                self.addIntoList(att)
        print(self.getAttendancelist())
        mydb.close()






