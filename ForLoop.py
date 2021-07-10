# Iterate through a list
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)
# Prints red green blue yellow

# Iterate through a string
S = 'python'
for x in S:
    print(x)
# Prints p y t h o n

# Break the loop at 'blue'
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        break
    print(x)
# Prints red green

# Skip 'blue'
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        continue
    print(x)
# Prints red green yellow

colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)
else:
    print('Done!')
# Prints red green blue yellow
# Prints Done!

# If Break execute the else clause will not be executed.
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        break
    print(x)
else:
    print('Done!')
# Prints red green

# Generate a sequence of numbers from 0 6
for x in range(7):
    print(x)
# Prints 0 1 2 3 4 5 6

# Print 'Hello!' three times
for x in range(3):
    print('Hello!')
# Prints Hello!
# Prints Hello!
# Prints Hello!

# Generate a sequence of numbers from 2 to 6
for x in range(2, 7):
    print(x)
# Prints 2 3 4 5 6

for x in range(-5,0):
    print(x)
# Prints -5 -4 -3 -2 -1

# Increment the range with 2
for x in range(2, 7, 2):
    print(x)
# Prints 2 4 6

# Flatten a nested list
list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
for sublist in list:
    for number in sublist:
        print(number)
# Prints 1 2 3 4 5 6 7 8 9

colors = ['red', 'green', 'blue']
for index in range(len(colors)):
    print(index, colors[index])
# Prints 0 red
# Prints 1 green
# Prints 2 blue

# enumerate instead of index
colors = ['red', 'green', 'blue']
for index, value in enumerate(colors):
    print(index, value)
# Prints 0 red
# Prints 1 green
# Prints 2 blue

# Tuple unpacking
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)
# Prints 1 2
# Prints 3 4
# Prints 5 6

# Dictionary unpacking
D = {'name': 'Bob', 'age': 25}
for x, y in D.items():
	print(x, y)
# Prints age 25
# Prints name Bob

# Insert item while looping through list
colors = ['red', 'green', 'blue']
for x in colors[:]:
	if x == 'red':
		colors.insert(0, 'orange')
print(colors)
# Prints ['orange', 'red', 'green', 'blue']

# Loop through two lists at once
name = ['Bob', 'Sam', 'Max']
age = [25, 35, 30]
for x, y in zip(name, age):
    print(x, y)
# Prints Bob 25
# Prints Sam 35
# Prints Max 30