

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.capitalize()) # 첫글자 대문자로


#---------------
# 1. else 
#---------------
container = [1,2,3,4,5]
for item in container:
    if item == 6:
        print("Found it!")
        break
else:
    # 아무것도 못찾았을 떄
    print("Not found it")

# Ex: 2-10사이에 소수를 찾아보기
for n in range(2, 10):
    for x in range(2, n):
        if (n%x) == 0:
            print (n, '=', x, '*', n/x)
            break
    else:
        # 루프가 끝나고 요소를 못 찾았을 때 
        print (n, '은 소수입니다.')


