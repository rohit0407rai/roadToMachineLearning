class Person:
    def __init__(self):
        print("Person is born")
    country="India"

    def takeBreak(self):
        print("I am breahing")
class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Person becme employee")
    company="Honda"

    def salary(self):
        print(f"Salary is {self.salary}")
    def takeBreak(self):
        super().takeBreak()#hame naya print karana hai but sth mai hi parent class ke takebreak kabhi
        print("I am human so i am breathing also..")
class Programmer(Employee):
   def __init__(self):
    super().__init__()
    company = "Fiverr"
    def getSalary(self):
        print(f"No salary to programmrd")
    def takeBreak(self):
        super().takeBreak()
        print("I am programmer")
# p=Person()
# e=Employee()
pr=Programmer()


# pr.takeBreak()# because inherited by employee
