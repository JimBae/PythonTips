
#------------
# 1. dir
#------------
# object attribute and method
myList = [1,2,3]
print(dir(myList))

#-----------------
# 2. type and id
#-----------------
#
print(type(''))
print(type([]))
print(type({}))
print(type(bool))
print(type(3))

# id는 다양한 객체의 unique id를 반환한다. 
name = 'yahoo'
print(id(name))

#-----------------
# 3. inspect 
#-----------------
# 살아있는 객체 정보를 알아내기 위한 몇가지 유용한 함수들을 제공한다.
# 예를 들면, 객체의 멤버를 확인할 수 있다.
import inspect
print(inspect.getmembers(str))

