a={1,3,4,5,1}
print(type(a))
print(a)
#it doesnt give the repetitive elements
# a={} #empty set doesnt form using this syntax
b=set()
print(type(b))
b.add(4)
b.add(5)
b.add(4)
print(b)
#we cant add lists in the sets
# b.add([4,5,6]) it is not allowed because list is muttable
b.add((4,5,6))
#tuples can be added
#b.add({4:5}) #cannot add  list or dictionary because they can be updated
#sets are unordered
#sets are unindexed
#there is no way to change the items in sets
#sets cannot contain duplicate values
print(len(b))
print(b)
b.remove(5)
# b.remove(15)#it will show error if value is not present in the sets
print(b)
c=a.pop()
print(c)
print(a)
# s.clear empties the set
