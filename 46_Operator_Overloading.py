class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num
    def __mul__(self, other): #n2 act as other
        print("Lets multiply")
        return self.num*other.num#n2 have constructr num which is assigned and then added other is object and . num is value
n1=Number(4)#it sets num as 4
n2=Number(5)# its sets num as 5
sum=n1+n2#it sets sum and n1 gives its num and in add n2 value goes as other and its same for multiplication and else
multi=n1*n2
print(sum)
print(multi)