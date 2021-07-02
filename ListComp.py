# All square numbers 0 to 4
L = []
for x in range(5):
    L.append(x**2)
print(L)

# List Comprehension
L = [x**2 for x in range(5)]
print(L)

# Filter list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
L = [x for x in vec if x >= 0]
print(L)

# From Nested Lists to single List
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = [number for list in vector for number in list]
print(L)

# Transpose Rows and Columns
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
L = [[row[i] for row in matrix] for i in range(3)]
print(L)

# With list comprehension
L = [ord(x) for x in 'foo']
print(L)

# With map() function, same result as above. Map is faster here
L = list(map(ord, 'foo'))
print(L)

# With list comprehension
L = [x ** 2 for x in range(5)]
print(L)

# With map() function. Same result as above. Here Map is slower.
L = list(map((lambda x: x ** 2), range(5)))
print(L)

# With list comprehension
L = [x for x in range(10) if x % 2 == 0]
print(L)

# With filter() function. Same result as above but filter is faster.
L = list(filter((lambda x: x % 2 == 0), range(10)))
print(L)