#Q1
# a=int(input("Enter the numbers:-"))
# b=int(input("Enter the numbers:-"))
# c=int(input("Enter the numbers:-"))
# d=int(input("Enter the numbers:-"))
# if(a>b and b>c and c>d):
#     print(a,"is greatest")
# elif(b>c and b>d and b>a):
#     print(b, "is greatest")
# elif(c>a and c>d and c>b):
#     print(c,"is greatest ")
# else:
#     print(d,"is greaest")

#Q2
# s1=int(input("Enter the first subjct marks:-"))
# s2=int(input("Enter the first subjct marks:-"))
# s3=int(input("Enter the first subjct marks:-"))
# if(s1<33 or s2<33 or s3<33):
#     print("FAIL")
# if((s1+s2+s3)/3<40):
#     print("FAIL")
# else:
#     print("PASS")
#Q3
text=input("Enter the text")
# spam=False
# if("make a lot of money" in text):
#     spam=True
# elif("buy now" in text):
#     spam=True
# elif("click this"in text):
#     spam=True
# elif("subscribe this" in text):
#     spam=True
# else:
#     spam=False
#
# if(spam):
#     print("This is a spam")
# else:
#     print("This is not a spam")

# if(len(text)>10):
#     print("It big")
# elif(len(text)<=10):
#     print("It small")
myName=["Sakshi","Shankar","Sonu"]
name=input("Enter the name:-")
if(name in myName):
    print(name,"is found in list")
else:
    print("Not present")