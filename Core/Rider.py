from User import User;
class Driver(User):
    def __init__(self,userT,resetToken):
        super().__init__(userT)
        fieldArea=""
        adjList=[]
        self.resetToken=resetToken
        startLocation=[]
        fuelRecord=[]
def main():
    d=Driver(("1","e","e","e","re","er","er","er","re","re","er","re"),"dfsfd") 
    d=User(Driver) 
    print(d.age)    
if __name__=="__main__":
    main()
