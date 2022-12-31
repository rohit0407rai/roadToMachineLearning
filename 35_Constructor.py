class Employee:
    company="Google"
    def getSalary(self): # when we wrote harry then object was made using class jis  object ke andar company tha aur salary bhi ....self is used for the paramters
        print(f"Salry is {self.salary}  ")

    @staticmethod  # we use statc mthod so that we dont use self where parameter is not needed
    def greet():
        print("Good mrning")

    def __init__(self):
        print("Employee is admitted ")
harry=Employee()