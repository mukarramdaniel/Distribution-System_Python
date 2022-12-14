from User import User
class Manager(User):
    def __init__(self,userT,PasswordReset):
        super().__init__(userT)
        self.PasswordReset=PasswordReset
    def getUsername(self):
        return self.userName