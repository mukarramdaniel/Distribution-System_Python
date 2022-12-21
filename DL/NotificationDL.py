class Notifications:
    def __init__(self):
        self.Notification_Stack=[]
    def Add(self,Noti):
        self.Notification_Stack.append(Noti)
    def Clear_Notification(self):
        self.Notification_Stack.pop()
        