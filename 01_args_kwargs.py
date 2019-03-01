import os
import sys

def test_var_args(fArg, *argv):
    print("First argument : ", fArg)
    for arg in argv:
        print("argValue : ", arg)

test_var_args('test1', 'python', 'arg3', 'arg4')

# **kwargs usages

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))

greet_me(name="ABS")

def test_args_kwargs(arg1, arg2, arg3):
    print("1st arg : ", arg1)
    print("2nd arg : ", arg2)
    print("3rd arg : ", arg3)

test_args_kwargs('arg1', 'arg2', 'arg3')

#>> *args 
args = ("two", 3, 5)
test_args_kwargs(*args)

#>> **kwargs
# key value have to match function's arguemnt name
kwargs = {"arg3": 5, "arg2": 3, "arg1":'two'}
test_args_kwargs(**kwargs)


# >> *arg, **kwargs, format args
#some_func(fargs, *args, **kwargs)


# 몽키패칭 시 사용할 수 있음
# 몽키패칭 : 런타임(실행) 중에 코드 일부를 수정하는 의미
#import someclass
#
#def get_info(self, *args):
#    return "TestData"
#someclass.get_info = get_info

