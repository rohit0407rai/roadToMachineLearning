class Sample:
    a="Harry"
    @staticmethod
    def  greet():
        print("Good Morning Guys")
obj=Sample()
obj.a="gadha" # it wont change the class attribute it will only change the instance attribute
print(obj.a)
# Sample.a="hello"
print(Sample.a)
obj.greet()