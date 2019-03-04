import os
import sys

#* map
#* filter

#-----------
# * map
#-----------
# map 은 입력 리스트의 모든 항목에 함수를 적용한다.
#
# map(function_to_apply, list_of_inputs)

# without map
itemList = [1,2,3,4,5]
resultList = []
for each in itemList:
    resultList.append(each**2)
print(resultList)

# use map
itemList = [1,2,3,4,5]
resultList = map(lambda x: x**2, itemList)
print(list(resultList))

# new example
def mul(x):
    return x*x

def add(x):
    return x+x

funcs = [mul, add]
for i in range(5):
    value = map(lambda x:x(i), funcs)
    print(list(value))

#------------
# * filter
#------------
# 함수에서 true를 반환하는 요소들로 구성되는 리스트를 생성한다.

inList = range(-5, 5)
lessThanZero = list(filter(lambda x: x<0, inList))
print(lessThanZero)


#------------
# * reduce
#------------
# reduce는 리스트로 몇가지 계산을 수행하고 반환하는 매우 유용한 함수다.
# 예를 들어 리스트의 곱을 계산하려고 하면, 
from functools import reduce
output = reduce( (lambda x, y: x*y), [1,2,3,4] )
print(output)




# 정리
# map
inList = [1,2,3,4,5]
outList = list(map( lambda x: x*x, inList))
print(outList) # [1,4,9, 16, 25]

# filter
inList = [1,2,3,4,5]
outList = list(filter(lambda x: x>3, inList))
print(outList) # [4,5]

# reduce
from functools import reduce
inList = [1,2,3,4,5]
outList = reduce(lambda x,y: x*y, inList)
print(outList) # 120






