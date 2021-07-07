# A tuple of integers
T = (1, 2, 3)

# A tuple of strings
T = ('red', 'green', 'blue')

# A tuple with mixed datatypes
T = (1, 'abc', 1.23, True)

# Single Value Tuple
T = (4,)
print(type(T))

# Convert a list to a tuple
T = tuple([1, 2, 3])
print(T)

# Convert a string to a tuple
T = tuple('abc')
print(T)

# Nested Tuple
T = ('red', ('green', 'blue'), 'yellow')
print(T)

# Tuple Value Assignment
T = ('red', 'green', 'blue', 'cyan')
(a, b, c, d) = T

print(a)
# Prints red

print(b)
# Prints green

print(c)
# Prints blue

print(d)
# Prints cyan

# Split an email address into a user name and a domain
addr = 'bob@python.org'
user, domain = addr.split('@')

print(user)
# Prints bob

print(domain)
# Prints python.org

T = ('red', 'green', 'blue', 'yellow', 'black')

print(T[0])
# Prints red

print(T[2])
# Prints blue

T = ('red', 'green', 'blue', 'yellow', 'black')

print(T[-1])
# Prints black

print(T[-2])
# Prints yellow

T = ('a', 'b', 'c', 'd', 'e', 'f')

print(T[2:5])
# Prints ('c', 'd', 'e')

print(T[0:2])
# Prints ('a', 'b')

print(T[3:-1])
# Prints ('d', 'e')

# Delete tuple because immutatable or unchangeable
T = ('red', 'green', 'blue')
del T

# Concatenate
T = ('red', 'green', 'blue') + (1, 2, 3)
print(T)
# Prints ('red', 'green', 'blue', 1, 2, 3)

# Replicate
T = ('red',) * 3
print(T)
# Prints ('red', 'red', 'red')

T = ('red', 'green', 'blue')
print(len(T))
# Prints 3

# Check for presence
T = ('red', 'green', 'blue')
if 'red' in T:
    print('yes')

# Check for absence
T = ('red', 'green', 'blue')
if 'yellow' not in T:
    print('yes')

# iterate through tuple
T = ('red', 'green', 'blue')
for item in T:
    print(item)
# Prints red green blue

# Sort a tuple using builtin function
T = ('cc', 'aa', 'dd', 'bb')
print(tuple(sorted(T)))
# Prints ('aa', 'bb', 'cc', 'dd')

# sort by changing from tuple to list
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)    # convert tuple to list
tmp.sort()       # sort list
T = tuple(tmp)   # convert list to tuple
print(T)         # Prints ('aa', 'bb', 'cc', 'dd')

# Python Tuple Methods
# Python has a set of built-in methods that you can call on tuple objects.

# Method	Description
# count()	Returns the count of specified item in the tuple
# index()	Returns the index of first instance of the specified item
# Built-in Functions with Tuple
# Python also has a set of built-in functions that you can use with tuple objects.

# Method	Description
# all()	Returns True if all tuple items are true
# any()	Returns True if any tuple item is true
# enumerate()	Takes a tuple and returns an enumerate object
# len()	Returns the number of items in the tuple
# max()	Returns the largest item of the tuple
# min()	Returns the smallest item of the tuple
# sorted()	Returns a sorted tuple
# sum()	Sums items of the tuple
# tuple()	Converts an iterable (list, string, set etc.) to a tuple