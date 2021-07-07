D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print(D)

D = dict(emp1 = {'name': 'Bob', 'job': 'Mgr'},
         emp2 = {'name': 'Kim', 'job': 'Dev'},
         emp3 = {'name': 'Sam', 'job': 'Dev'})

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'}}


IDs = ['emp1','emp2','emp3']

EmpInfo = [{'name': 'Bob', 'job': 'Mgr'},
           {'name': 'Kim', 'job': 'Dev'},
           {'name': 'Sam', 'job': 'Dev'}]

D = dict(zip(IDs, EmpInfo))

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'}}

# Create nested dict with default values
IDs = ['emp1','emp2','emp3']
Defaults = {'name': '', 'job': ''}

D = dict.fromkeys(IDs, Defaults)

print(D)
# Prints {'emp1': {'name': '', 'job': ''},
#         'emp2': {'name': '', 'job': ''},
#         'emp3': {'name': '', 'job': ''}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print(D['emp1']['name'])
# Prints Bob

print(D['emp2']['job'])
# Prints Dev

# key present
print(D['emp1'].get('name'))
# Prints Bob

# key absent
print(D['emp1'].get('salary'))
# PrintsNone

# Change Nested Item
D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3']['name'] = 'Max'
D['emp3']['job'] = 'Janitor'

print(D['emp3'])
# Prints {'name': 'Max', 'job': 'Janitor'}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3'] = {'name': 'Max', 'job': 'Janitor'}

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Max', 'job': 'Janitor'}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp4'] = {'name': 'Max', 'job': 'Janitor'}

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'},
#         'emp4': {'name': 'Max', 'job': 'Janitor'}}

# Merge two nested dicts
D1 = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
      'emp2': {'name': 'Kim', 'job': 'Dev'}}

D2 = {'emp2': {'name': 'Sam', 'job': 'Dev'},
      'emp3': {'name': 'Max', 'job': 'Janitor'}}

D1.update(D2)

print(D1)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Sam', 'job': 'Dev'},
#         'emp3': {'name': 'Max', 'job': 'Janitor'}}

# Remove item by key
D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

x = D.pop('emp3')

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}

# get removed value
print(x)
# Prints {'name': 'Sam', 'job': 'Dev'}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

del D['emp3']

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

x = D.popitem()

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}

# get removed pair
print(x)
# Prints ('emp3', {'name': 'Sam', 'job': 'Dev'})

# iterate through nested dict
D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])