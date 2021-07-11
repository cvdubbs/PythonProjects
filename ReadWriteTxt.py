f = open('myfile.txt')

f = open(r'C:\Python33\Scripts\myfile.txt')

# Specify File Mode
# Here are five different modes you can use to open the file:

# Character	Mode	Description
# ‘r’	Read (default)	Open a file for read only
# ‘w’	Write	Open a file for write only (overwrite)
# ‘a’	Append	Open a file for write only (append)
# ‘r+’	Read+Write	open a file for both reading and writing
# ‘x’	Create	Create a new file
# You can also specify how the file should be handled.

# Character	Mode	Description
# ‘t’	Text (default)	Read and write strings from and to the file.
# ‘b’	Binary	Read and write bytes objects from and to the file.This mode is used for all files that don’t contain text (e.g. images).

# Open a file for reading
f = open('myfile.txt')

# Open a file for writing
f = open('myfile.txt', 'w')

# Open a file for reading and writing
f = open('myfile.txt', 'r+')

# Open a binary file for reading
f = open('myfile.txt', 'rb')

# Read entire file
f = open('myfile.txt')
print(f.read())

# Prints:
# First line of the file.
# Second line of the file.
# Third line of the file.

f = open('myfile.txt')

print(f.read(3))
# Prints Fir

print(f.read(5))
# Prints First

f = open('myfile.txt')
print(f.readline())
# Prints First line of the file.

# Call it again to read next line
print(f.readline())
# Prints Second line of the file.

# Loop print whole file this way
f = open('myfile.txt')
for line in f:
    print(line)

# Prints:
# First line of the file.
# Second line of the file.
# Third line of the file.

# Read all the lines in a file into a list of strings
f = open('myfile.txt')
print(f.readlines())

# Prints:
# ['First line of the file.\n', 'Second line of the file.\n', 'Third line of the file.']

# Write
f = open('myfile.txt', 'w')
f.write('Overwrite existing data.')

# Append
f = open('myfile.txt', 'a')
f.write(' Append this text.')

# Overwrite
f = open('myfile.txt', 'r+')
f.write('---Overwrite content---')

# Write Multiple Lines
f = open('myfile.txt', 'w')
lines = ['New line 1\n', 'New line 2\n', 'New line 3']
f.writelines(lines)

# Flush output buffer to disk without closing
f = open('myfile.txt', 'a')
f.write('Append this text.')
f.flush()

f = open('myfile.txt')
f.close()

# check closed status
print(f.closed)
# Prints True

with open('myfile.txt') as f:
    print(f.read())

f = open('myfile.txt')
try:
    # File operations goes here
finally:
    f.close()

# Create a file and open it for writing

# write mode
f = open('newFile.txt', 'w')

# append mode
f = open('newFile.txt', 'a')

# read + write mode
f = open('newFile.txt', 'r+')

# Create a file exclusively
f = open('newFile.txt', 'x')

# Delete File
import os
os.remove('myfile.txt')

# Check if file exists
import os
if os.path.isfile('myfile.txt'):
	f = open('myfile.txt')
else:
	print('The file does not exist.')	

f = open('myfile.txt', 'rb+')

# go to the 7th character and read one character
f.seek(6)
print(f.read(1))
# Prints G

# go to the 3rd character from current position (letter G)
f.seek(3, 1)
print(f.read(1))
# Prints K

# go to the 3rd character before the end
f.seek(-3, 2)
print(f.read(1))
# Prints X

f = open('myfile.txt')

# initial position
print(f.tell())
# Prints 0

# after reading 5 characters
f.read(5)
print(f.tell())
# Prints 5