# A list of integers
L = [1, 2, 3]
print(L)

# A list of strings
L = ['red', 'green', 'blue']
print(L)

# Convert a string to a list
L = list('abc')
print(L)

# Nested list example
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L)

# Print Third item in the third item
print(L[2][2])

# Print the first item in the third item in the thrid item
print(L[2][2][0])

# Sample List
L = ['red', 'green', 'blue', 'yellow', 'black']

# Print the first item in the list
print(L[0])

# Print the third item in the list
print(L[2])

# Print the last item in the list
print(L[-1])

# Sample List
L = ['a', 'b', 'c', 'd', 'e', 'f']

# Slice List
print(L[2:5])

print(L[0:2])

print(L[3:-1])

# Sample List
L = ['red', 'green', 'blue']

# Change the first item in the list
L[0] = 'orange'
print(L)

# Change the last item in the list
L[-1] = 'violet'
print(L)

# Sample List
L = ['red', 'green', 'yellow']

# Add an Item at the end of the list
L.append('blue')
print(L)

# Add an item into a specific spot
L.insert(1,'blue')
print(L)

# Append a List to the List
L.extend(['green', 'yellow'])
print(L)

# Remove the second item from a list
del L[1]
print(L)

# Remove the first Item by value. If there's two will only remove the first
L.remove('green')
print(L)

# Remove more than one item
del L[1:4]
print(L)

# Clear out list
L.clear()
print(L)

# Replicate a list multiple times
L = ['red', 'green']
L = L * 3
print(L)

# Check List Length
print(len(L))

# Check if in list
if 'red' in L:
    print('yes')

# Check for absence
if 'yellow' not in L:
    print('yes')

# Iterate through a list
for item in L:
    print(item)

# Loop through the list and double each item
L = [1, 2, 3, 4]
for i in range(len(L)):
    L[i] = L[i] * 2

print(L)

# Python List Methods
# Python has a set of built-in methods that you can call on list objects.

# Method	Description
# append()	Adds an item to the end of the list
# insert()	Inserts an item at a given position
# extend()	Extends the list by appending all the items from the iterable
# remove()	Removes first instance of the specified item
# pop()	Removes the item at the given position in the list
# clear()	Removes all items from the list
# copy()	Returns a shallow copy of the list
# count()	Returns the count of specified item in the list
# index()	Returns the index of first instance of the specified item
# reverse()	Reverses the items of the list in place
# sort()	Sorts the items of the list in place

# Built-in Functions with List
# Python also has a set of built-in functions that you can use with list objects.

# Method	Description
# all()	Returns True if all list items are true
# any()	Returns True if any list item is true
# enumerate()	Takes a list and returns an enumerate object
# len()	Returns the number of items in the list
# list()	Converts an iterable (tuple, string, set etc.) to a list
# max()	Returns the largest item of the list
# min()	Returns the smallest item of the list
# sorted()	Returns a sorted list
# sum()	Sums items of the list