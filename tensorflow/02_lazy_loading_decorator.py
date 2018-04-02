"""
Example of lazy loading with decorator
Created by uni xu (uniwow@sina.com) 2017/10/09
tensorflow research
"""

#function decorator
import time

def cost_time(method):

    def inner(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print("Method Name - '{0}', Args - '{1}', Kwargs - '{2}', Execution Time - '{3}'".format(
            method.__name__,
            args,
            kwargs,
            end_time - start_time
        ))
        return result
    return inner


@cost_time
def ticktock(*args, **kwargs):
    time.sleep(1)
    print("tick tock...")
    print(args, kwargs)

ticktock(["hello, tensor"], tick=0, tock=1)


#method decorator
def method_decorator(method):

    def inner(user_instance):
        if user_instance.name == "Uni":
            print("I just waiting you for a long time.")
        else:
            method(user_instance)
    return inner


class User(object):

    def __init__(self, name):
        self.name = name

    @method_decorator
    def print_test(self):
        print("hello " + self.name)

p1 = User("Uni")
p1.print_test()
p2 = User("Tensor")
p2.print_test()



# class Decorator
class DecoClass(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        # before f actions
        print('decorator initialised')
        self.f(*args, **kwargs)
        print('decorator terminated')
        # after f actions

@DecoClass
def class_decorator():
    print('class decorator')

class_decorator()



#decorator chain

def decorator_1(f):
    def inner(*args,**kwargs):
        print("<h>" + f(*args,**kwargs) + "</h>")
    return inner
def decoretor_2(f):
    return lambda *args,**kwargs: "<p>" + f(*args,**kwargs) + "</p>" 

@decorator_1
@decoretor_2
def say():
    return "Hello"

say()



# function tools

from functools import wraps

def wrapped_decorator(arg1):
    """wrapped decorator docstring"""
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """inner function docstring """
            print(func.__name__ + " " + arg1 +" was wrapped")
            return func(*args, **kwargs)
        return wrapper
    return inner_function


@wrapped_decorator("uni")
def wrapped(x):
    """foobar docstring"""
    return x*x

print(wrapped.__name__,wrapped.__doc__,wrapped(4))



# functools class decorator with args

class ClassDecorator(object):

    def __init__(self, arg1, arg2):
        print("Arguements passed to decorator %s and %s" % (arg1, arg2))
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, foo, *args, **kwargs):

        def inner_func(*args, **kwargs):
            print(" Args passed inside decorated function .%s and %s" % (self.arg1, self.arg2),sep='------->')
            return foo(*args, **kwargs)
        return inner_func


@ClassDecorator("arg 1", "arg 2")
def print_args(*args):
    for arg in args:
        print(arg)


print_args("python", "tensor")




