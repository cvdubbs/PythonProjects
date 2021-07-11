def hello1():
    print("Hello World")

def hello2():
    print("Hello Universe")

def greet(func):
    func()

greet(hello1)
# Prints Hello World
greet(hello2)
# Prints Hello Universe

def outer_func():
    def inner_func():
        print("Running inner")
    inner_func()

outer_func()
# Prints Running inner

def greet():
    def hello(name):
        print("Hello", name)
    return hello

greet_user = greet()

greet_user("Bob")
# Prints Hello Bob

def decorate_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def hello():
    print("Hello world")

hello = decorate_it(hello)

hello()
# Prints Before function call
# Prints Hello world
# Prints After function call

def decorate_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorate_it
def hello():
    print("Hello world")

hello()
# Prints Before function call
# Prints Hello world
# Prints After function call

def decorate_it(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@decorate_it
def hello(name):
    print("Hello", name)

hello("Bob")
# Prints Before function call
# Prints Hello Bob
# Prints After function call

def decorate_it(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorate_it
def hello(name):
    return "Hello " + name

result = hello("Bob")

print(result)
# Prints Before function call
# Prints After function call
# Prints Hello Bob

from functools import wraps

def decorate_it(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorate_it
def hello():
    '''function that greets'''
    print("Hello world")

print(hello.__name__)
# Prints hello
print(hello.__doc__)
# Prints function that greets
print(hello)
# Prints <function hello at 0x02DC5BB8>

# Unwrap a wrapped function
from functools import wraps

def decorate_it(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorate_it
def hello():
    print("Hello world")

original_hello = hello.__wrapped__

original_hello()
# Prints Hello world

from functools import wraps

def double_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

def square_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

@double_it
@square_it
def add(a,b):
    return a + b

print(add(2,3))
# Prints 50

@square_it
@double_it
def add(a,b):
    return a + b

print(add(2,3))
# Prints 100

from functools import wraps

def double_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

double_the_sum = double_it(sum)

print(double_the_sum([1,2]))
# Prints 6

from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return wrapper

@debug
def hello(name):
    return "Hello " + name

hello("Bob")
# Prints Running function: hello
# Prints Positional arguments: ('Bob',)
# Prints keyword arguments: {}
# Prints Result: Hello Bob

sum = debug(sum)
sum([1, 2, 3])
# Prints Running function: sum
# Prints Positional arguments: ([1, 2, 3],)
# Prints keyword arguments: {}
# Prints Result: 6

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Finished in {:.3f} secs".format(end-start))
        return result
    return wrapper

@timer
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000)
# Prints Finished in 0.005 secs
countdown(1000000)
# Prints Finished in 0.178 secs