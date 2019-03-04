import os

# bad example
def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1)) #[1]
print(add_to(2)) #[1,2]
print(add_to(3)) #[1,2,3]

# if you want to 
# [1]
# [2]
# [3]

# correct 
def add_to2(element, target=None):
    if target == None:
        target = []
        target.append(element)
    return target

print(add_to2(1)) #[1]
print(add_to2(2)) #[2]
print(add_to2(3)) #[3]








