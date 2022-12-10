import User
class Employee(User):
    def __init__(self,userT,resetToken) -> None:
        super().__init__(userT)
        self.resetToken=resetToken
            