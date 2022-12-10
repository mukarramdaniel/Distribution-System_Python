class Bill:
    def __init__(self,cnic,orderID,billDate,amountPKR,remaining,shopID) -> None:
        self.cnic=cnic
        self.orderID=orderID
        self.billDate=billDate
        self.amountPKR=amountPKR
        self.remaining=remaining
        self.shopID=shopID