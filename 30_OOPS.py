class Number:
    def sum(self):
        return self.a+self.b
    #class is a template  and object is like pen which is used to write in a template
num=Number() #create an object
num.a=12
num.b=34
s=num.sum()
print(s)
