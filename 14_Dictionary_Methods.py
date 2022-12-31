myDict={
    "Fast":"In a Quick Manner",
    "Harry":"A coder",
    "marks": [1,2,5],
    "anotherdict": {'Hary':"Player"},
    1:2
}
print(myDict.keys()) #prints the keys
print(myDict.values())
print(myDict.items()) #print thee keys and values of all contents
print(myDict)
updateDict={
    "Lovish":"Friend"
}
myDict.update(updateDict)#updating the dictionary
#if we write same values so it updates the old values present in dictionaries
print(myDict)
#differenece between get() and []
print(myDict.get("Harry"))#here error  doesnnt come if key is not find othe than that it returns the None
print(myDict["Harry"])#it is not good because if harry ke doesnt exist so error occurs
