class Employee:
    company_name="Google" #class attributes
    salary=110


harry=Employee()
rajan=Employee()
print(harry.company_name)
print(rajan.company_name)

# harry.salary=100 #instance attributes  first the attribute declared by object is preffered
# rajan.salary=400
Employee.company_name="Youtube"
#creating instance attribute salary for both objects
# print(harry.company_name)
# print(rajan.company_name)
harry.salary=45
print(harry.salary)
print(rajan.salary)
#first it will  print instnace attribute
#them it will print clss instance
# print(rajni.address) it is wrong beacuse we havent declared address attribute neither in class nor as an instance
