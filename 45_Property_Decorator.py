class Employee:
    company="Bharat Gas"
    salary=5600
    salaryBonus=500
    # totalSalary=6100
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus
    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus=val-self.salary

e=Employee()
print(e.totalSalary)#here we dont have to callit like a function
e.totalSalary=5800 # as it is a property wont work like functio but 5800 was an input to  uper function
print(e.salary)
print(e.salaryBonus)