class Employee:
    company_name="Google" #class attributes


harry=Employee()
rajan=Employee()
print(harry.company_name)
print(rajan.company_name)

harry.salary=100 #instance attributes  first the attribute declared by object is preffered
rajan.salary=400
Employee.company_name="Youtube"

print(harry.company_name)
print(rajan.company_name)
print(harry.salary)
print(rajan.salary)