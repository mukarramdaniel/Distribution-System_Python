import User
class Employee(User):
    _salary = None
    def __init__(self,userT,salary) -> None:
        super().__init__(userT)
        self.resetToken=salary
            