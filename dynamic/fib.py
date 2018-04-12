from functools import wraps 

def cache(func):
    d = {}
    @wraps(func)
    def wrap(*args):
        if args not in d:
            d[args] = func(*args)
            print(d[args])
        return d[args]
    return wrap


@cache
def fib(i):
    if i <= 2:
        return 1 
    return fib(i-1) + fib(i-2)


fib(5)