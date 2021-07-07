# A set of strings
S = {'red', 'green', 'blue'}

# A set of mixed datatypes
S = {1, 'abc', 1.23, (3+4j), True}

S = {'red', 'green', 'blue', 'red'}
print(S)
# Prints {'blue', 'green', 'red'}

# Set of items in an iterable
S = set('abc')
print(S)
# Prints {'a', 'b', 'c'}

# Set of successive integers
S = set(range(0, 4))
print(S)
# Prints {0, 1, 2, 3}

# Convert list into set
S = set([1, 2, 3])
print(S)
# Prints {1, 2, 3}

S = {'red', 'green', 'blue'}
S.add('yellow')
print(S)

S = {'red', 'green', 'blue'}
S.update(['yellow', 'orange'])
print(S)
# Prints {'blue', 'orange', 'green', 'yellow', 'red'}

# with remove() method
S = {'red', 'green', 'blue'}
S.remove('red')
print(S)
# Prints {'blue', 'green'}

# with discard() method
S = {'red', 'green', 'blue'}
S.discard('red')
print(S)
# Prints {'blue', 'green'}

# pop removes a random item from the set
S = {'red', 'green', 'blue'}
x = S.pop()
print(S)

# removed item
print(x)

# Clear Set
S = {'red', 'green', 'blue'}
S.clear()
print(S)
# Prints set()

# Find Set Size
S = {'red', 'green', 'blue'}
print(len(S))
# Prints 3

# iterate through set
S = {'red', 'green', 'blue'}
for item in S:
    print(item)
# Prints blue green red

# Check for presence
S = {'red', 'green', 'blue'}
if 'red' in S:
    print('yes')

# Check for absence
S = {'red', 'green', 'blue'}
if 'yellow' not in S:
    print('yes')

# Full Outter Union
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A | B)
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

# by method
print(A.union(B))
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

# Inner Join or Intersection
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A & B)
# Prints {'red'}

# by method
print(A.intersection(B))
# Prints {'red'}

# Set Difference, or left not in right
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A - B)
# Prints {'blue', 'green'}

# by method
print(A.difference(B))
# Prints {'blue', 'green'}

# Set Symetric Difference - Outter remove inner
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A ^ B)
# Prints {'orange', 'blue', 'green', 'yellow'}

# by method
print(A.symmetric_difference(B))
# Prints {'orange', 'blue', 'green', 'yellow'}

# Other Set Operations
# Below is a list of all set operations available in Python.

# Method	Description
# union()	Return a new set containing the union of two or more sets
# update()	Modify this set with the union of this set and other sets
# intersection()	Returns a new set which is the intersection of two or more sets
# intersection_update()	Removes the items from this set that are not present in other sets
# difference()	Returns a new set containing the difference between two or more sets
# difference_update()	Removes the items from this set that are also included in another set
# symmetric_difference()	Returns a new set with the symmetric differences of two or more sets
# symmetric_difference_update()	Modify this set with the symmetric difference of this set and other set
# isdisjoint()	Determines whether or not two sets have any elements in common
# issubset()	Determines whether one set is a subset of the other
# issuperset()	Determines whether one set is a superset of the other

# Frozen-set is an immutable (unchangable) set
S = frozenset({'red', 'green', 'blue'})
print(S)
# Prints frozenset({'green', 'red', 'blue'})

# finding size
S = frozenset({'red', 'green', 'blue'})
print(len(S))
# Prints 3

# performing union
S = frozenset({'red', 'green', 'blue'})
print(S | {'yellow'})
# Prints frozenset({'blue', 'green', 'yellow', 'red'})

# Built-in Functions with Set
# Below is a list of all built-in functions that you can use with set objects.

# Method	Description
# all()	Returns True if all items in a set are true
# any()	Returns True if any item in a set is true
# enumerate()	Takes a set and returns an enumerate object
# len()	Returns the number of items in the set
# max()	Returns the largest item of the set
# min()	Returns the smallest item of the set
# sorted()	Returns a sorted set
# sum()	Sums items of the set