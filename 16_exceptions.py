
# try/except
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print("An IOError occured. {}".format(e.args[-1]))

#-------------------------------
# 1. 여러가지 예외처리를 함께하는 법
#-------------------------------
try:
    file = open("test.txt", 'rb')
except (IOError, EOFError) as e:
    print("An error occured. {}".format(e.args[-1]))


try:
    file = open("test.txt", 'rb')
except EOFError as e:
    print("An EOF Error occured")
    #raise e
except IOError as e:
    print("An error occured")
    #raise e

#---------------------
# 2. finally 
#---------------------
# finally 문에 감싸진 코드는 예외 발생 여부와 상관없이 실행된다. 
try:
    file = open('test.txt','rb')
except IOError as e:
    print("An IOError occured. {}".format(e.args[-1]))
finally:
    print("Always print")

#---------------------
# 3. try/else
#---------------------
# else : 예외가 발생하지 않았을때 실행하기 원하는 코드는 else 문에 넣으면 된다.
# else 문은 예외가 없을 경우에만 실행되고, finally 문이 실행되기 전에 실행된다.

try:
    print("try 문")
except:
    print("except")
else:
    print("if no exception, it will be printed")
finally:
    print("finally")