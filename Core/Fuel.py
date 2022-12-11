class Fuel:
    __litre=None
    __amount=None
    __date=None
    __riderID=None
    def __init__(self,litre,amount,date,riderID) -> None:
        self.litre=litre
        self.amount=amount
        self.date=date
        self.riderID=riderID