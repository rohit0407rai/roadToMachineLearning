class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        self.result=self.number*self.number
        print(f"The cube of {self.number} is {self.result}")
    def sqrt(self):
        print(f"The cube of number is {self.number **0.5}")
    def cube(self):
        print(f"The cube of number is {self.number **3}")

chase=Calculator(12)
chase.square()
chase.cube()
chase.sqrt()
# self.number **2