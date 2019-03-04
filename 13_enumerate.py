
someList = ['a', 'b', 'c', 'd']
for counter, value in enumerate(someList):
    print(counter, value)

print("\n")
someList = ['apple', 'banana', 'grape', 'peach']
for counter, value in enumerate(someList, 2):
    print(counter, value)

someList = ['apple', 'banana', 'grape', 'peach']
counterList = list(enumerate(someList, 2))
print(counterList)

