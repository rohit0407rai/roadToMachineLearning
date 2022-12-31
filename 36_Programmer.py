class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name is {self.name}")
        print(f"The product on which they are working {self.product}")
harry=Programmer("Harry","Skype")
alka=Programmer("kishor","Github")
harry.getInfo()
alka.getInfo()  #in Python self is passed because class doesnt know about the functions because here the functions are defined
#so as we said class knows there is object but we have specify the object using self in pythoon
