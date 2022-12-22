class Notific:
    def __init__(self,OrderId,Detail):
        self.OrderId=OrderId
        self.Detail=Detail
    def GetorderId(self):
        return self.OrderId
    def GetDetail(self):
        return self.Detail