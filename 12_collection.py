from collections import defaultdict

#------------------
# 1. defaultdict
#------------------
# dict와 달리 defaultdict를 사용하면 key값의 존재 유무를 확인할 필요가 없다.
colors = ( 
    ('A', 'yellow'),
    ('B', 'blue'),
    ('C', 'green'),
    ('B', 'black'),
    ('A', 'red'),
    ('D', 'silver'))
print(type(colors)) # tuple
favoriteColor = defaultdict(list)

for name, color in colors:
    favoriteColor[name].append(color)
print(favoriteColor)
# defaultdict(<class 'list'>, 
# {'A': ['yellow', 'red'], 
#  'B': ['blue', 'black'], 
#  'C': ['green'], 
#  'D': ['silver']})

# 또다른 중요한 사용방법은 dict 안에 nested list(리스트 안에 리스트가 있는 형태)를 추가하는 것.
# 키 값이 사전 안에 존재하지 않는다면, KeyError가 발생할 것이다. 
# defaultdict는 이런 문제를 창의적으로 해결한다. 
# KeyError가 뜨는 예시를 보고나서 defaultdict 사용법을 알아보자

# Problem
#some_dict = {}
#some_dict['colors']['favorite'] = 'yellow' # KeyError: 'colors'

# Solution
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colors']['favorite'] = 'yellow'

# json.dumps를 사용해서 some_dict를 출력할 수도 있다.
import json
print(json.dumps(some_dict)) # {"colors": {"favorite": "yellow"}}

#------------------
# 2. orderedDict
#------------------
# orderedDict는 처음 삽입될 때의 순서대로 항목을 정렬된 상태로 유지한다.
# 기존 키의 값을 덮어 쓰더라도 해당 키의 위치는 변경되지 않는다.

# Problem
colors = {"red": 198, "green": 170, "blue": 160}
for key, value in colors.items():
    print(key, value)
# random 한 순서로 출력됨.

# Solution
from collections import OrderedDict

colors = OrderedDict( [("red", 198), ("green", 170), ("blue", 160)] )
for key, value in colors.items():
    print(key, value)

#------------------
# 3. counter
#------------------
# Counter는 특정 아이템의 개수를 세는 함수이다.
from collections import defaultdict
from collections import Counter

colors = ( 
    ('A', 'yellow'),
    ('B', 'blue'),
    ('C', 'green'),
    ('B', 'black'),
    ('A', 'red'),
    ('D', 'silver'))

favs = Counter(name for name, color in colors)
print(favs) # Counter({'A': 2, 'B': 2, 'C': 1, 'D': 1}

# 파일 안에서 가장 많이 반복된느 줄을 세는데 사용할 수도 있다.
# lineCount = None
# with open('fileName', 'rb') as f:
#     lineCount = Counter(f)
# print(lineCount)

#------------------
# 4. deque
#------------------
#
# 추가나 삭제가 양쪽에서 가능한 double ended queue.

from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
print(d[0])
print(d[-1])

d = deque([i for i in range(5)])
print(len(d))
d.popleft()
d.pop()
print(d)

d = deque(maxlen=30)
# 30 개 이상의 아이템을 넣으면, 왼쪽의 가장 앞에 있는 것이 튀어나올 것이다.
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)

#------------------
# 5. namedtuple
#------------------
#
# 튜플은 기본적으로 값의 시퀀스를 쉼표로 구분하여 저장할 수 있는 불변(immutable) 리스트이다.
# 리스트와 거의 비슷하지만 몇가지 중요한 차이점이 있다. 
# 주요한 점은 리스트와 달리, 튜플에 있는 항목을 재할당 할 수 없다는 것이다. 
# 튜플 안의 값에 접근하기 위해서는 아래와 같이 정수 인덱스를 사용한다. 

man = ('ali', 30)
print(man[0])

# namedetuples 사용하면 튜플 안의 값들에 접근하기 위해 정수 인덱스 값들을 사용할 필요가 없다. 
# 사전형이라고 생각할 수 있지만, 사전형과 달리 불변형이다.

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry  = Animal(name='perry', age=31, type='cat')
print(perry)
print(perry.name)
print(perry.age)
print(perry.type)

# 연산자를 사용하여 이름만으로 튜플의 멤버에 접근할 수 있음을 알 수 있다. 
# namedtuple는 인자 2개가 필요하다.(튜플 이름, 필드 이름) 
# 위 예제에서는 tuple name: Animal이고 필드_names는 ('name', 'age', 'type')
# nametuple은 자가문서화(self-document) 시킨다. 
# 튜플의 멤버에 접근하기 위해 정수 인덱스를 사용할 필요가 없으므로 코드를 유지관리하기가 더 쉽다.
# namedtuple의 instance는 instance 당 사전들을 가지지 않으므로, 일반 튜플보다 더 가볍고 메모리 사용량을 줄일 수 있다.
# 그래서 사전형보다도 더 빠르다. 그러나 튜플이기 때문에 불변임을 명심해야한다. 

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')
print(perry)
#perry.age = 20 # AttriguteError: can't set attribute

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')
print(perry[0])
print(perry._asdict())

#-------------------------
# 6. enum.Enum
#-------------------------

from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat         = 1
    dog         = 2
    horse       = 3
    aardvark    = 4
    butterfly   = 5
    owl         = 6
    platypus    = 7
    dragon      = 8
    unicorn     = 9

    kitten = 1
    puppy  = 2

Animal  = namedtuple('Animal', 'name age type')
perry   = Animal(name='Perry', age=31, type=Species.cat)
dragon  = Animal(name='Dragon', age=4, type=Species.dragon)
tom     = Animal(name='Tom', age=75, type=Species.cat)
charlie = Animal(name='Charlie', age=2, type=Species.kitten)

print(perry.type == tom.type)
print(charlie.type == tom.type)









