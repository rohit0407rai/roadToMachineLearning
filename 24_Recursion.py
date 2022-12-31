# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# n=int(input("Enter the number:-"))
# fact=factorial(n)
# print("The factorial is"+str(fact))
# def maximum(num1,num2,num3):
#     if(num1>num2 and num2>num3):
#         return num1
#     elif(num2>num3 and num2>num1):
#         return num2
#     else:
#         return num3
# print("The value of max is :-"+str(maximum(23,56,13)))

# print("Hello",end=" ")#end="no space" no next line if space is there so it creates a gap
# print("And",end=" ")

def Nsum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n+Nsum(n-1)
print("The sum of given number is "+str(Nsum(5)))

