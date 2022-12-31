class Employee:
    company="Camelin"
    salary=100
    location="Delhi"
    @classmethod # it will directly change the cass attribute and no need of changing the object attribute
    def changeSalary(cls,sal):
        cls.salary=sal#it is used to chnage the  salary of class and not of object __class__
e=Employee()
print(e.salary)
e.changeSalary(455) # it made an copy instance changed he value of tht , it doesnt change the real functions salary value
print(e.salary)
print(Employee.salary)