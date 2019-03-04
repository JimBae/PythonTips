
# more info
# https://wiki.python.org/moin/Powerful%20Python%20One-Liners

#-------------------------
# 1. simple web server
#-------------------------
#> python -m SimpleHTTPServer # python2
#> python -m http.server      # python3

#-------------------------
# 2. pretty printing
#-------------------------
# list and dict
from pprint import pprint
myDict = {'name': 'JJ', 'age': 19, 'sex': 'male'}
print(myDict)
pprint(myDict)

#-------------------------
# 3. 간단하게 json 파일을 예쁘게 출력하고 싶을때
#-------------------------
#> cat file.json | python -m json.tools

#-------------------------
# 4. Profiling a script
#-------------------------
#> python -m cProfile script.py

#-------------------------
# 5. CSV to json
#-------------------------
#> python -c "import csv, json; (print json.dumps(list(csv.reader(open('csvfile.csv')))))"

#-------------------------
# 6. List flattening
#-------------------------
# itertools packages, itertools.chain.from_iterable

import itertools
aList = [[1,2], [3,4], [5,6], [7,8]]
print(list(itertools.chain.from_iterable(aList)))

#-------------------------
# 7. 한줄 생성자
#-------------------------
class A(object):
    def __def__(self, a,b,c,d,e,f):
        self.__dict__.update({k: v for k, v in locals().items() if k!='self'})


