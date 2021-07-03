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
