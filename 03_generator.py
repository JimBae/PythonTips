import os
import sys

#--------------
# * iterable
# * iterator
# * iteration
# * generator
#--------------

# * iterable : 반복가능한 객체
# __iter__ or __getitem__ method가 정의된 파이썬의 모든 객체.

# * iterator : 반복자 
# next() or __next__() method가 정의된 모든 객체.

# * iteration : 반복
# 리스트 같은 저장소에서 아이템을 가져오는 과정.

# * generator 
# generator는 iterator이지만 단 한 번만 반복한다.
# 메모리에 모든 값을 저장하지 않기 때문에 값을 사용할 때 즉시 생성한다.
# for loop를 사용하거나 반복하는 함수나 구조에 생성된 값들을 전달하여 반복을 사용한다.
# 대부분 generator는 함수로 구현된다. 그러나 값을 return하지 않고, yield(산출)될 뿐이다.


# generator 모든 결과물들을 메모리에 저장하지 않으면서 동시에, 많은 양의 결과 셋을 계산해야할 때 좋다.
# 특히 루프 그 자체를 포함한 계산을 할때. 

# fibonacci generator version
def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for x in fibonacci(100):
    print(x)

gen = fibonacci(100)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# str type은 iterable 이지만 iterator는 아니다. 
# next()는 못쓰지만, iter 를 사용하면 된다.
myStr = "abcdefg"
myIter = iter(myStr)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
#print(next(myIter)) # error

