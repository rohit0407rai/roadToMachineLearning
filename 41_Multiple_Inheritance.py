class Employee:
    company="Visa"
    ecode=120
class FreeLancer:
    company="Fiverr"
    level=0
    def upgrade_level(self):
        print(f"The level increased to {self.level+1}")
class Programmr(Employee,FreeLancer): # if we write employee fisrt so common functions are preffered of first class in a bracket
    name="Rohit"
p=Programmr()
p.upgrade_level()
print(p.company)