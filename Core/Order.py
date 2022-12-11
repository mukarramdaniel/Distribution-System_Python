class Order:
    def __init__(self,cart,trackingID,riderID,shopID,orderID,created_on,upDate_on) -> None:
        self.cart=cart
        self.trackingID=trackingID
        self.riderID=riderID
        self.shopID=shopID
        self.orderID=orderID
        self.created_on=created_on
        self.upDate_on=upDate_on