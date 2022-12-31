class Employee:
    company="Camelin"
    salary=100
    location="Delhi"
    def changeSalary(self,sal):
        self.__class__.salary=sal#it is used to chnage the  salary of class and not of object __class__
e=Employee()
print(e.salary)
e.changeSalary(455) # it made an copy instance changed he value of tht , it doesnt change the real functions salary value
print(e.salary)
print(Employee.salary)