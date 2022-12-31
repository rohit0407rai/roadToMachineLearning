myDict={
    "Fast":"In a Quick Manner",
    "Harry":"A coder",
    "marks": [1,2,5],
    "anotherdict": {'Hary':"Player"}


}
print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['marks'])
print(myDict['anotherdict']['Hary']) #its accesing the dictiionary ke andar dictionary
#it is unordered
#it is mutable
#it is indexed
myDict['marks']=[23,45,67]
print(myDict['marks'])
#cannot contain duplicate keys