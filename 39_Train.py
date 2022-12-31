class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getInfo(self):
        print(f"The name is {self.name}")
        print(f"The fare is {self.fare}")
        print(f"The no of seats are {self.seats}")

intercity=Train("Intercity Exprss:1092",90,300)
intercity.getInfo()#we are using self so that object can be passed to call arguments because here function srae defined so they dont know what object will call them so self means passing object as a parameter to function so that they know this object is gonna call
#and static method is applid where no valus of class is to be printed and normal printing of sentences is needed

