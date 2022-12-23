from Core.Notification import Notific
class Notifications:
    def __init__(self):
        self.Notification_Stack=[]
    def Add_Notification(self,Noti):
        self.Notification_Stack.append(Noti)
    def Clear_Notification(self):
        self.Notification_Stack.pop()
    def Pop_Up(self,orderid):
        for idx,obj in enumerate(self.GetNotification()):
            if(obj.GetorderId()==orderid):
                self.Notification_Stack.pop(idx)
                
    def GetNotification(self):
        return self.Notification_Stack
    
    def loadFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT OrderID,Detail FROM notifications")
        myresult = mycursor.fetchall()
        for x in myresult:
            noti=Notific(x[0],x[1])
            self.Add_Notification(noti)
        mydb.close()

    def updateTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )
        mycursor = mydb.cursor()
        mycursor.execute("TRUNCATE TABLE notifications")
        mydb.commit()
        sql = "INSERT IGNORE INTO notifications(OrderID,Detail) VALUES (%s,%s)  "
        noti=self.GetNotification()
        for i in noti:
            n=(i.GetorderId(),i.GetDetail())
            mycursor.execute(sql,n)
            mydb.commit()
        mydb.close()
        
        print("Inserted") 