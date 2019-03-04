import os
import sys

def new_decorator(func):
    def wrapTheFunction():
        print("before run func")
        func()
        print("after run func")
    return wrapTheFunction

def function_requiring_decoration():
    print("in function_requireing_decoration()")

function_requiring_decoration()
func_with_deco = new_decorator( function_requiring_decoration )
func_with_deco()

@new_decorator
def anotherFunction():
    print("anotherFunction")
anotherFunction()


# >>> use functools.wraps

from functools import wraps

def newDecorator(inFunc):
    @wraps(inFunc)
    def wrapTheFunction():
        print("before run inFunc")
        inFunc()
        print("after run inFunc")
    return wrapTheFunction

@newDecorator
def function_requiring_decorator():
    print("in function_requiring_decorator")
    return 'a'

print(function_requiring_decorator.__name__)


# >>>
from functools import wraps
canRun = True
def decoratorName(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not canRun:
            return "Will not run"
        return f(*args, **kwargs)
    return decorated

@decoratorName
def func():
    return("in func")

canRun = True
print(func())
canRun = False
print(func())


# example 1. : 인증
from functools import wraps
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


# example 2. : Logging
from functools import wraps
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addFunc(x):
    return x+x
result = addFunc(10)

