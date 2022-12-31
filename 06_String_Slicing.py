name="Harry"
greeting="Good Morning, "
print(type(name))
c=greeting+name
print(c)
print(name[0])
print(name[2])
#Strings are immutable no working
# name[3]=df is not applicable
print(name[0:3])
# 0 1 and 2 are counted but 3 isnt counted
print(name[0:4])
# 0 1 2 3 will be counted and not 4 th one
print(name[0:5])
print(name[1:5])
print(name[:4])# is same as [0:4]
print(name[1:])#it is like[1:5]
print(name[0:])#it is like[0:5]
#0=-5 1=-4 2=-3 3=-4 4=-5 it will also works same as index starting from 0


word="amazing"
print(word[1:4:1])# here printing will be from 1 to 3 index with the gap of 1 but no skip for 1
print(word[1:4:2]) # hre the 3 wala part 3-1 is the number of time skipping occurs
