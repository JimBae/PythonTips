
# lambda 는 1줄 함수.
# lambda argument: manipulate(argument)

# ex
add = lambda x, y: x + y
print(add(2,4))

# sort
a = [(1,2), (4,1), (9,10), (13,-3)]
a.sort(key = lambda x:x[1])
print(a)

# 병렬로 sort list
list1 = [1,2,3,4,5]
list2 = [9,8,5,3,1]
data = list(zip(list1, list2))
print(data)
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
