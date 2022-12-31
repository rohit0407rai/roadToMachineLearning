class Employee:
    company="Bharat Gas"
    salary=5600
    salaryBonus=500
    # totalSalary=6100
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus
    

e=Employee()
print(e.totalSalary)#here we dont have to callit like a function
e.totalSalary=5800