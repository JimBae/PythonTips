import os
import sys

# set datastructure
#aSet = {''}
#print(type(aSet)) # set

someList = ['a', 'a', 'b', 'c', 'd', 'e', 'e']
someSet = set(someList)
print(someSet)

# brute force version
duplicateList = []
for value in someList:
    if someList.count(value) > 1:
        if value not in duplicateList:
            duplicateList.append(value)
print(duplicateList)

# more nice code by using set
someList = ['a', 'a', 'b', 'c', 'd', 'e', 'e']
duplicateSet = set([x for x in someList if someList.count(x) > 1])
print(list(duplicateSet))

#-------------
# set methods
#-------------
#>>> intersection 
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
inSet = set(['red', 'brown'])
print(inSet.intersection(valid))

#>>> difference
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
inSet = set(['red', 'brown'])
print(inSet.difference(valid))

