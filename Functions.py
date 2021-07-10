def hello():
    print('Hello, World!')
  
hello()
# Prints Hello, World!

# Pass single argument to a function
def hello(name):
    print('Hello,', name)

hello('Bob')
# Prints Hello, Bob
hello('Sam')
# Prints Hello, Sam

# Pass two arguments
def func(name, job):
    print(name, 'is a', job)

func('Bob', 'developer')
# Prints Bob is a developer

def func(name, job):
    print(name, 'is a', job)

func('Bob', 'developer')
# Prints Bob is a developer

# Keyword arguments can be put in any order
def func(name, job):
    print(name, 'is a', job)

func(name='Bob', job='developer')
# Prints Bob is a developer

func(job='developer', name='Bob')
# Prints Bob is a developer

# Set default value 'developer' to a 'job' parameter
def func(name, job='developer'):
    print(name, 'is a', job)

func('Bob', 'manager')
# Prints Bob is a manager

func('Bob')
# Prints Bob is a developer

# Captures all in a tuple
def print_arguments(*args):
    print(args)

print_arguments(1, 54, 60, 8, 98, 12)
# Prints (1, 54, 60, 8, 98, 12)

# Collects into a dictionary
def print_arguments(**kwargs):
    print(kwargs)

print_arguments(name='Bob', age=25, job='dev')
# Prints {'name': 'Bob', 'age': 25, 'job': 'dev'}

# Return sum of two values
def sum(a, b):
    return a + b

x = sum(3, 4)
print(x)
# Prints 7

# Return addition and subtraction in a tuple
def func(a, b):
    return a+b, a-b

result = func(3, 2)

print(result)
# Prints (5, 1)

# Unpack returned tuple
def func(a, b):
    return a+b, a-b

add, sub = func(3, 2)

print(add)
# Prints 5
print(sub)
# Prints 1

# Docustring or notation for a funcion
def hello():
    """This function prints
       message on the screen"""  
    print('Hello, World!')

# Print docstring in rich format
help(hello)

# Help on function hello in module __main__:
# hello()
#    This function prints
#    message on the screen

# Print docstring in a raw format
print(hello.__doc__)

# Prints This function prints message on the screen

import math
x = math.sin(360*2*math.pi)
print(x)
# Prints -3.133115067780141e-14

import math
x = math.exp(math.log(3.14))
print(x)
# Prints 3.1399999999999997

# Nested Functions
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

result = outer(2, 4)

print(result)
# Prints 6

# Recursive Function
def countdown(num):
    if num <= 0:
        print('Stop')
    else:
        print(num)
        countdown(num-1)

countdown(5)
# Prints 5
# Prints 4
# Prints 3
# Prints 2
# Prints 1
# Prints Stop

def hello():
    print('Hello, World!')
  
hi = hello
hi()
# Prints Hello, World!

def findSquare(x):
    return x ** 2

def findCube(x):
    return x ** 3

# Create a dictionary of functions
exponent = {'square': findSquare, 'cube': findCube}

print(exponent['square'](3))
# Prints 9
print(exponent['cube'](3))
# Prints 27

x = 0
if x:
    def hello():
        print('Hello, World!')
else:
    def hello():
        print('Hello, Universe!')

hello()
# Prints Hello, Universe!
