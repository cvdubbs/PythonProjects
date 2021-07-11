def doubler(x):
    return x*2

print(doubler(2))
# Prints 4

print(doubler(5))
# Prints 10

# Same as above but in lambda format
doubler = lambda x: x*2

print(doubler(2))
# Prints 4

print(doubler(5))
# Prints 10

evenOdd = (lambda x:
           'odd' if x%2 else 'even')

print(evenOdd(2))
# Prints even

print(evenOdd(3))
# Prints odd

# Immediate Invoked Lambda Function
print((lambda x: x*2)(3))
# Prints 6

# A lambda function that multiplies two values
mul = lambda x, y: x*y
print(mul(2, 5))
# Prints 10

# A lambda function that adds three values
add = lambda x, y, z: x+y+z
print(add(2, 5, 10))
# Prints 17

# Positional arguments
add = lambda x, y, z: x+y+z
print(add(2, 3, 4))
# Prints 9

# Keyword arguments
add = lambda x, y, z: x+y+z
print(add(2, z=3, y=4))
# Prints 9

# Default arguments
add = lambda x, y=3, z=4: x+y+z
print(add(2))
# Prints 9

# *args
add = lambda *args: sum(args)
print(add(2, 3, 4))
# Prints 9

# **args
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3, z=4))
# Prints 9

# Double each item of the list using map function
def doubler(x):
    return x*2

L = [1, 2, 3, 4, 5, 6]
mod_list = map(doubler, L)
print(list(mod_list))
# Prints [2, 4, 6, 8, 10, 12]

# Double each item of the list
L = [1, 2, 3, 4, 5, 6]
doubler = map(lambda x: x*2, L)
print(list(doubler))
# Prints [2, 4, 6, 8, 10, 12]

# Filter the values above 18
def checkAge(age):
    if age > 18:
        return True
    else:
        return False

age = [5, 11, 16, 19, 24, 42]
adults = filter(checkAge, age)
print(list(adults))
# Prints [19, 24, 42]

# Filter the values above 18
age = [5, 11, 16, 19, 24, 42]
adults = filter(lambda x: x > 18, age)
print(list(adults))
# Prints [19, 24, 42]

# sum all items in a list
from functools import reduce

def summer(a, b):
    return a + b

L = [10, 20, 30, 40]
result = reduce(summer, L)
print(result)
# Prints 100

from functools import reduce

L = [10, 20, 30, 40]
result = reduce(lambda a, b: a + b, L)
print(result)
# Prints 100

# Return multiple values by packing them in a tuple
findSquareCube = lambda num: (num**2, num**3)
x, y = findSquareCube(2)
print(x)
# Prints 4
print(y)
# Prints 8

# A lambda function that returns the smallest item
findMin = lambda x, y: x if x < y else y

print(findMin(2, 4))
# Prints 2

print(findMin('a', 'x'))
# Prints a

# Flatten a nested list with lambda
flatten = lambda l: [item for sublist in l for item in sublist]

L = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print(flatten(L))
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

L = [['a', 'b', 'c'], ['d', 'e']]
print(flatten(L))
# Prints ['a', 'b', 'c', 'd', 'e']

# dictionary of functions
exponent = {'square':lambda x: x ** 2,
            'cube':lambda x: x ** 3}

print(exponent['square'](3))
# Prints 9

print(exponent['cube'](3))
# Prints 27

# dictionary of functions
exponent = {'square':lambda x: x ** 2,
            'cube':lambda x: x ** 3}

print(exponent['square'](3))
# Prints 9

print(exponent['cube'](3))
# Prints 27

# list of functions
exponent = [lambda x: x ** 2,
            lambda x: x ** 3]

print(exponent[0](3))
# Prints 9

print(exponent[1](3))
# Prints 27

# Sort the list of taples by the age of students
L = [('Sam', 35),
    ('Max', 25),
    ('Bob', 30)]
x = sorted(L, key=lambda student: student[1])
print(x)
# Prints [('Max', 25), ('Bob', 30), ('Sam', 35)]

from functools import wraps

# Defining a decorator
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        print(f"[DEBUG] Calling {func.__name__} with argument {args} | Result: {result}")
        return result
    return wrapper

# Applying decorator to hello()
@debug
def hello(name):
    return "Hello " + name

# Calling the decorated function
print(hello("Bob"))
# Prints [DEBUG] Calling hello with argument ('Bob',) | Result: Hello Bob
# Prints Hello Bob

print((debug(lambda x: x ** 2))(3))
# Prints [DEBUG] Calling <lambda> with argument (3,) | Result: 9
# Prints 9

print(list(map(debug(lambda x: x*2), range(3))))
# Prints [DEBUG] Calling <lambda> with argument (0,) | Result: 0
# Prints [DEBUG] Calling <lambda> with argument (1,) | Result: 2
# Prints [DEBUG] Calling <lambda> with argument (2,) | Result: 4
# Prints [0, 2, 4]

# Closures
def multiplier(x):
    def inner_func(y):
        return x*y
    return inner_func

doubler = multiplier(2)
print(doubler(10))
# Prints 20

tripler = multiplier(3)
print(tripler(10))
# Prints 30

# Lambda Closures
multiplier = (lambda x: (lambda y: x*y))

doubler = multiplier(2)
print(doubler(10))
# Prints 20

tripler = multiplier(3)
print(tripler(10))
# Prints 30