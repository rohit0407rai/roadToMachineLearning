# n=int(input("Enter the number:-"))
# for i in range(1,11):
#     print(str(n)+" X "+str(i)+" = "+str(n*i))
#q2
# l1=["Harry","Soham","Sachin","Rahul"]
# for item in l1:
#     if(item.startswith("S")):
#         print("Hello "+item)
#q3
# prime=True
# n=int(input("Enter the number:-"))
# for i in range(2,n):
#     if(n%i==0):
#         prime=False
#         break
# if prime:
#     print("This prime")
# else:
#     print("This is not  a prime")
# #q4
# num=1
# n=int(input("Enter the number:-"))
# for i in range(1,n+1):
#     num=num*i
# print("The factorial is "+str(num))

# n=4
# for i in range(4):
#     print("*"*(i+1))
for i in range(3):
    print(" "*(3-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(3-i-1))


