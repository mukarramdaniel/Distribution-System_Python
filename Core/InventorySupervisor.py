from Core.User import User
class InventorySupervisor(User):
    def __init__(self,userT,resetToken,attendenceDate):
        super().__init__(userT,resetToken)
        self.attendenceDate=attendenceDate
        