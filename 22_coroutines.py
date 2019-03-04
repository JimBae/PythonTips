
# ref
# http://www.dabeaz.com/coroutines/Coroutines.pdf


#-----------------------------------------
# https://blueshw.github.io/2016/01/25/python-co-routine-vs-sub-routine

# 코루틴의 개념을 살펴보기 전에 우선, 상반되는(반드시 상반된다고는 할 수 없지만..) 서브루틴에 대해서 한번 짚고 넘어가 보겠습니다. 
# 참고로 서브루틴의 상반되는 개념은 코루틴이 아닌 메인루틴(main-routine, 그냥 루틴이라고도 함)이라 할 수 있습니다.

# 서브루틴
# 서브루틴은 반복되는 특정 기능을 모아 별도로 묶어 놓아 이름을 붙여 놓은 것으로 메인루틴을 보조하는 역할을 합니다. 
# 보통 언어에서는 함수나 메소드 등으로 불리며 사용됩니다. 어떤 특정 기능을 모아놓고 이름을 붙였다는 것으로 매크로와 비슷하지만 
# 매크로의 경우 컴파일시에(C 언어에서와 같이) 매크로를 호출하는 부분을 모두 매크로 본문으로 대체해 버리므로 메모리 사용이 비효율적입니다. 
# 반면에 서브루틴은 별도의 메모리에 해당 기능을 모아 놓고 있어, 서브루틴이 호출될 때마다 저장된 메모리로 이동했다가 
# return 을 통해 원래 호출자의 위치로 돌아오게 됩니다. 호출할 때마다 매번 같은 위치로 이동하기 때문에 여러번 사용될 수 있으므로 
# 매크로에 비해서 훨씬 효율적이라 할 수 있겠지요.

# 코루틴
# 코루틴도 서브루틴처럼 기능들을 별도의 공간에 모아 놓고 있다는 점에서는 동일합니다. 
# 차이점이라 할 수 있는 것은, 서브루틴의 경우에는 메인루틴에서 특정 서브루틴의 공간으로 이동한 후에
# 리턴에 의해 호출자로 돌아와 다시 프로세스를 진행하는데 반해 코루틴의 경우에는 루틴을 진행하는 중간에 멈추어서 
# 특정 위치로 돌아갔다가 다시 원래 위치로 돌아와 나머지 루틴을 수행할 수 있습니다. 
# 또 한가지 차이점은 서브루틴은 진입점과 반환점이 단 하나밖에 없어 메인루틴에 종속적이지만, 
# 코루틴은 진입지점이 여러개이기 때문에 메인루틴에 종속적이지 않아 대등하게 데이터를 주고 받을 수 있다는 특징이 있습니다. 
# 코루틴은 주로 동시성을 필요로 하는 UNITY 등의 게임프로그래밍에서 많이 사용하는 개념이라고 합니다.

# 파이썬에도 코루틴이 있습니다. 코루틴의 특징과 흐름을 살펴보면 다음과 같습니다.

#   1. 파이썬에는 yield 문이라는 특수한 구문이 있습니다. return 처럼 동작하지만, 사실은 입력으로 동작합니다.
#      (메인루틴에 종속적이 아니라 대등한 상태이기 때문에)
#   2. next(coroutine)은 coroutine 함수의 첫번째 yield 까지 호출한 다음 대기합니다. 
#      두번째 next(coroutine)을 호출하면, 첫번째 yield 다음의 나머지 부분을 수행하고 다시 돌아와 그 다음 yield 까지 호출합니다.
#      iteration 이 가능한곳까지 next 함수가 수행된 뒤에는 StopIteration 에러가 발생하게 됩니다.
#   3. 만약 yield 문이 특정 변수에 할당된다면, 만들어진 코루틴 객체에서 coroutine.send(value)를 호출해 주어야 합니다. 
#      첫번째 coroutine 지점(yield)에 멈춰있는 상태에서 변수에 할당 되어야 하는데 아무런 값도 들어오지 않는다면 에러가 발생하게 됩니다. 
#      즉, yield 를 통해서 메인루틴과 서브루틴간에 서로 값이 이동하면서 특정 로직을 수행하게 되는 것입니다.

#-----------------------------------------

#-----------------------------------------
# https://soooprmx.com/archives/5622
#
# tail -f 구현
#
import time
def follow1(inFile):
    inFile.seek(0, 2) # go to the end of the file
    while True:
        line = inFile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# logfile = open('access-log')
# for line in follow(logfile):
#     print(line, end=' ')

# 1. 제너레이터를 생성하고, 한 라인의 문자열을 요청한다.
# 2. 제너레이터는 맨 처음에 파일의 끝으로 이동한 다음 한 줄을 읽는다. 이 줄을 내놓는다.
# 3. 내놓은 값은 메인루프에 의해 화면에 출력된다.
# 4. 출력 후 메인루프의 끝에 다다르면 다시 제너레이터에게 다음 줄을 요청한다.
# 5. 제너레이터는 새 줄을 읽어들인다. 만약 새 줄이 없으면 0.1초 동안 대기한 후 재시도한다. (이 과정이 없으면 CPU 사용량이 치솟는다.)
# 6. 5의 과정을 반복하다가 새로운 라인이 들어오면 이를 내놓고 for 루프로 돌아간다.
# 7. 이 과정은 명시적인 종료 지점이 없으므로 (외부 요인에 의한 예외가 발생하지 않는 이상) 계속 반복된다.

# generator로 생성된 객체는 내부적으로 __next__(), send() 두 개의 메소드를 갖게된다.
# __next__()는 next() 함수에 전달되었을 때 호출된느 메소드로 다음번 yield 구문까지 실행하라는 신호를 제너레이터에게 전달한다.
# send() method는 __next__() 와 거의 동일한데, 차이가 있다면 이 시점에서 코루틴 내부로 값을 밀어넣을 수 있다는 점이다.

# 주의해야 할 사항은 코루틴은 제너레이터와 달리 생성 후에 무조건 next()를 한 번 실행해서,
# 값을 받을 수 있는 상태로 만들어 주어야한다는 점이다. 
# 보통은 이 과정을 뺴먹기 쉬우므로 시작되지 않은 제너레이터에 send를 호출해서 에러를 만나느 실수를 범하기 쉽다.
# 코루틴은 생성직후 무조건 next() 를 한 번 호출해야하니, 이 과정을 자동으로 처리할 수 있도록 데코레이터를 만들어두는 편이 편하다.

from functools import wraps
def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

# 파이프라인
# 코루틴으로 값을 넣는 방법을 알게 되었으니 제너레이터/코루틴을 서로 연결하는 것을 만들어 보자.
# 위에서 작성한 follow를 다음과 같이 수정하고 테스트해보자.

def follow2(inFile, target=None):
    # target은 여기서 생성한 결과를 사용할 consumer coroutine이다.
    inFile.seek(0, 2)
    while True:
        line = inFile.readline()
        if not line:
            time.sleep(0.1)
            continue
        # target 이 있으면 라인을 target으로 넘기고
        # 그렇지 않으면 반환한다.
        if target:
            yield target.send(line)
        else:
            yield line

# ## tail -f | grep python
# logFile = open('access-log.txt')
# logLines = follow(logFile, prn)
# for _ in logLines:
#     pass

# 1. follow 의 기본 동작은 기존과 동일하다. 대신 타깃 코루틴이 있으면 단순히 yield 로 값을 출력하는 대신에 타깃에게 값을 전달한다.
# 2. 그리고 follow(logfile, prn)과 같이 획득되는 로그 파일의 각 라인을 프린터 객체에게 넘겨주도록 설정한다.
# 3. for _ in loglines: pass 는 아무일도 하지 않는 것 같지만, 매 라인이 들어오면 그 라인을 prn 에게 넘겨주기 때문에 이 코드는 기존과 똑같이 실행된다.

# 파이프라인을 구성하는 것의 장점은 간단한 코루틴을 라인의 중간에 삽입하여 기존 코드를 수정하지 않고 실행 흐름을 조작할 수 있다는 것이다.
# 만약 서버 로그의 각 라인에 python이라는 단어가 들어간 라인만 출력한다고 해보자.
# 그냥 함수를 쓴다면 follow() 코드를 수정해야겠지만, 이런 코루틴을 생각해보자

@coroutine
def grepper(word, target=None):
    line = yield
    while True:
        if word in line:
            if target:
                line = yield target.send(line)
            else:
                line = yield line

# 이 코루틴은 처음에 지정한 단어가 매 입력에 있으면 이를 내놓거나 타킷으로 전달한다.
# 그렇지 않은 경우에는 무시해버리는 기능을 수행한다. 이 코루틴이 있다면 파이프라인을 다음과 같이 만들 수 있다.

# follow[매라인입력] --> grepper('python') --> printer()

# prn = printer()
# ## 수정
# grep = grepper('python',prn)
# logLines = follow(logFile, grep)

# for _ in logLines:
#     pass


#-----------------------------------------


# Python Generator?
#   - 위의 myrange 함수가 수행되다가 yield를 만나게 되면 i를 반환한다. 그리고 끝나는 게 아니라 그 상태에서 머물게 된다.
#   - 보통의 함수는 호출되면 return을 만나거나 블록의 끝까지 수행되고 나면 끝이다.
#   - 하지만 제너레이터의 경우 next()로 함수를 yield까지 가게 해서 계속 함수를 수행시킬 수 있다. 그리고 더 이상 yield까지 갈 수 없을 경우 StopIteration 예외를 내며 끝난다.
# 
# Coroutine이란?
#   - 코루틴이란 위의 제너레이터처럼 진입점(Entry points)이 여러개인 함수를 말한다.
#   - 보통 우리가 작성하는 함수(Subroutine)는 처음 호출된 시점이 유일한 진입점이다.
#   - 그러나 제너레이터는 next()를 호출할 때마다 그 함수에 진입할 수 있다.


# coroutine
# 코루틴은 제너레이터와 몇가지를 제외하고 거의 비슷하다.
# generator는 데이터의 생산자이고,
# coroutine은 데이터의 소비자이다. 

def fib():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a, b

