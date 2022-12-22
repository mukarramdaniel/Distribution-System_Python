class Notifications:
    def __init__(self):
        self.Notification_Stack=[]
    def Add_Notification(self,Noti):
        self.Notification_Stack.append(Noti)
    def Clear_Notification(self):
        self.Notification_Stack.pop()
    def GetNotification(self):
        return self.Notification_Stack