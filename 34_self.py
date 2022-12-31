class Employee:
    company="Google"
    def getSalary(self): # when we wrote harry then object was made using class jis  object ke andar company tha aur salary bhi ....self is used for the paramters
        print(f"Salry is {self.salary}  ")

    @staticmethod  # we use statc mthod so that we dont use self where parameter is not needed
    def greet():
        print("Good mrning")

harry=Employee()
harry.salary=10000
harry.getSalary() # if no self so harry was gong as a argment which gives error.. self is like a parmeter which passes when function is called using objects
harry.greet()