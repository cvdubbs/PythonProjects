# Create a dictionary to store employee record
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev',
     'city': 'New York',
     'email': 'bob@web.com'}

# Create a dictionary with a list of two-item tuples
L = [('name', 'Bob'),
     ('age', 25),
     ('job', 'Dev')]

D = dict(L)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
# Create a dictionary with a tuple of two-item lists
T = (['name', 'Bob'],
     ['age', 25],
     ['job', 'Dev'])

D = dict(T)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

D = dict(name = 'Bob',
         age = 25,
         job = 'Dev')

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Create a dictionary with list of zipped keys/values
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']

D = dict(zip(keys, values))

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Initialize dictionary with default value '0' for each key
keys = ['a', 'b', 'c']
defaultValue = 0

D = dict.fromkeys(keys,defaultValue)

print(D)
# Prints {'a': 0, 'b': 0, 'c': 0}

# values of different datatypes
D = {'a':[1,2,3],
     'b':{1,2,3}}

# duplicate values
D = {'a':[1,2],
     'b':[1,2],
     'c':[1,2]}

# Fetch one key value's store
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print(D['name'])
# Prints Bob

# When key is present
print(D.get('name'))
# Prints Bob

# When key is absent
print(D.get('salary'))
# Prints None

# Update value for key 'name'
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D['name'] = 'Sam'
print(D)
# Prints {'name': 'Sam', 'age': 25, 'job': 'Dev'}

# Add new key and value
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D['city'] = 'New York'
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev', 'city': 'New York'}

# Merge
D1 = {'name': 'Bob',
      'age': 25,
      'job': 'Dev'}

D2 = {'age': 30,
      'city': 'New York',
      'email': 'bob@web.com'}

D1.update(D2)
print(D1)
# Prints {'name': 'Bob', 'age': 30, 'job': 'Dev',
#         'city': 'New York', 'email': 'bob@web.com'}

# Remove key and value but store value
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

x = D.pop('age')
print(D)
# Prints {'name': 'Bob', 'job': 'Dev'}

# get removed value
print(x)
# Prints 25

# Just remove no store
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

del D['age']
print(D)
# Prints {'name': 'Bob', 'job': 'Dev'}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

x = D.popitem()
print(D)
# Prints {'name': 'Bob', 'age': 25}

# get removed pair
print(x)
# Prints ('job', 'Dev')

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D.clear()
print(D)
# Prints {}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

# get all keys
print(list(D.keys()))
# Prints ['name', 'age', 'job']

# get all values
print(list(D.values()))
# Prints ['Bob', 25, 'Dev']

# get all pairs
print(list(D.items()))
# Prints [('name', 'Bob'), ('age', 25), ('job', 'Dev')]

# Iterate through dictionary
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

for x in D:
    print(x)
# Prints name age job

for x in D:
    print(D[x])
# Prints Bob 25 Dev

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print('name' in D)
# Prints True
print('salary' in D)
# Prints False

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print('Bob' in D.values())
# Prints True
print('Sam' in D.values())
# Prints False

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print(len(D))
# Prints 3

# Python Dictionary Methods
# Python has a set of built-in methods that you can invoke on dictionary objects.

# Method	Description
# clear()	Removes all items from the dictionary
# copy()	Returns a shallow copy of the dictionary
# fromkeys()	Creates a new dictionary with the specified keys and values
# get()	Returns the value of the specified key
# items()	Returns a list of key:value pair
# keys()	Returns a list of all keys from dictionary
# pop()	Removes and returns single dictionary item with specified key.
# popitem()	Removes and returns last inserted key:value pair from the dictionary.
# setdefault()	Returns the value of the specified key, if present. Else, inserts the key with a specified value.
# update()	Updates the dictionary with the specified key:value pairs
# values()	Returns a list of all values from dictionary
# Built-in Functions with Dictionary
# Python also has a set of built-in functions that you can use with dictionary objects.

# Method	Description
# all()	Returns True if all list items are true
# any()	Returns True if any list item is true
# len()	Returns the number of items in the list
# sorted()	Returns a sorted list