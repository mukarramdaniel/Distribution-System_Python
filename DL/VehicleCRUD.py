import sys
sys.path.insert(1,"Core.Vehicle")
from Core.Vehicle import Vehicle

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None

class VehicleCRUD:
    def __init__(self):
        self.head=None
        self.linklist=[]
    def addToList(self,val):
        self.linklist.append(val)
    def Insert_at_Head(self,val): # insert at head
        New_Node=Node(val)
        New_Node.next=self.head
        if(self.head != None):
            self.head.prev=New_Node
        self.head=New_Node
        New_Node.prev=None
    def getList(self):
        return self.linklist
    def Insert(self,val):
        New_Node=Node(val)
        last=self.head
        New_Node.next=None
        if(self.head==None):
            New_Node.prev=None
            self.head=New_Node
            return
        
        while(last.next!=None):
            last=last.next
        last.next=New_Node
        New_Node.prev=last
    
    def Insert_btw_Nodes(self,prev_Node,val):
        if(prev_Node==None):
            print("Previous node cannot be empty")
            return
        New_Node=Node(val)
        New_Node.next=prev_Node.next
        prev_Node.next=New_Node
        New_Node.prev=prev_Node
        if(New_Node.next!=None):
            New_Node.next.prev=New_Node

    def Delete(self,val):
        start=self.head
        Node_Deleted=False

        if(start==None):
            return
        elif(start.data==val): # deleting from start
            self.head=start.next
            return
        while(start!=None):
            if(start.data==val):
                break
            start=start.next
        if(start.next==None): #deleting from end
            start=start.prev
            start.next=None
        else:
            start.prev.next=start.next
            start.next.prev=start.prev
            

    def Print_List(self,node):
        while(node!=None):
            print(" {}".format(node.data))
            node=node.next
    def loadFromTable(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="Rosepetal514@",
        database="dbarm"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT model,number,fuelAverage,riderID  FROM vehicle")
        DlinkList=VehicleCRUD()
        myresult = mycursor.fetchall()
        for x in myresult:
            vehicle=Vehicle(x[0],x[1],x[2])
            vehicle.setRider(x[3])
            self.addToList(vehicle)
        mydb.close()

# if __name__ == "__main__":
#     list1=VehicleCRUD()
#     list1.Insert_at_Head(10)
#     list1.Insert_at_End(9)
#     list1.Insert_btw_Nodes(list1.head, 50)
#     #list1.Insert_at_End(6)
#     #list1.Insert_btw_Nodes(list1.head.next, 8)
#     list1.Print_List(list1.head)
#     list1.Delete(50)
#     list1.Print_List(list1.head)