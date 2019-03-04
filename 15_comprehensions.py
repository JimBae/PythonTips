import os
import sys

#---------------------------------
# 1. list comprehensions example
#---------------------------------
# variable = [out_exp for out_exp in inputList if outExpr == 2]

aList = [1,2,3,4,5,6,7]
outList = [x*x for x in aList if x%2==0]
print(outList) # [4, 16, 36]

#---------------------------------
# 2. dict comprehensions
#---------------------------------
mcase = {'a': 10, 'b': 34, 'A':7, 'Z':3}
mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) \
                    for k in mcase.keys() }
print(mcase_frequency) # {'a': 17, 'b': 34, 'z': 3}

#---------------------------------
# 3. set comprehensions
#---------------------------------
squared = {x**2 for x in [1, 1, 2]}
print(squared) # {1,4}

