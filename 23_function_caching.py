
# memoization : 이전에 계산한 값을 메모리에 저장함으로써, 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 향상시키는 기술.

# 함수 캐싱은 전달 인자에 따른 함수의 반환 값들을 캐싱합니다.
# (여기서 캐싱은 캐시를 저장하다 의미로 쓰인다.)
# I/O 바인딩 함수가 동일한 인수를 사용하여 주기적으로 호출될 때 시간을 절약할 수 있다.
# Python 3.2+ 버전부터 lru_cache 데코레이터를 사용해서 쉽게 함수의 반환값들을 캐싱 혹은 언캐싱할 수있다.

#  
# 피보나치수열 lru_cache로 구현

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n<2:
        return n

    return fib(n-1) + fib(n-2)

# maxsize 인자는 lru_cache에 캐싱해야할 최근 반환값의 수를 알려준다. 
print([fib(n) for n in range(10)])

# 아래와 같이 언캐싱 할 수 있다.
fib.cache_clear()


#----------------
# python2.+
#----------------
from functools import wraps

def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def fibonacci(n):
    if n< 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(25)
