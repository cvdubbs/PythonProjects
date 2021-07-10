S = 'Hello, World!'   # single quotes
print(S)
S = "Hello, World!"   # double quotes
print(S)
# No Difference between the two

# Multi line string
S = """String literals can
span multiple lines."""
print(S)

# an integer to a string
S = str(42)
print(S)
# Prints '42'

# a complex number to a string
S = str(3+4j)
print(S)
# Prints '(3+4j)

# a list to a string
S = str([1,1])
print(S)
# Prints '[1, 1]'

# Indexing
S = 'ABCDEFGHI'
print(S[0])    # Prints A
print(S[4])    # Prints E

# Negative Indexing
S = 'ABCDEFGHI'
print(S[-1])    # Prints I
print(S[-6])    # Prints D

# Slicing a string
S = 'ABCDEFGHI'
print(S[2:5])      # Prints CDE
print(S[5:-1])     # Prints FGH
print(S[1:6:2])    # Prints BDF

# Change a string (strings are immutable)
S = 'Hello, world!'
new_S = 'J' + S[1:]
print(new_S)
# Prints Jello, world!

# concatenation operator
S = 'Hello,' + ' World!'
print(S)
# Hello, World!

# augmented assignment operator
S = 'Hello,'
S += ' World!'
print(S)
# Prints Hello, World!

# Implicit Concatenation
S = 'Hello,' " World!"
print(S)
# Prints Hello, World!

# the hard way
S = '--------------------'

# the easy way
S = '-' * 20

# String Length
S = 'Supercalifragilisticexpialidocious'
print(len(S))
# Prints 34

# Replace text within string
S = 'Hello, World!'
x = S.replace('World', 'Universe')
print(x)
# Prints Hello, Universe!

# Split the string on comma
S = 'red,green,blue,yellow'
x = S.split(',')
print(x)
# Prints ['red', 'green', 'blue', 'yellow']
print(x[0])
# Prints red

# Join the list of substrings
L = ['red', 'green', 'blue', 'yellow']
S = ','.join(L)
print(S)
# Prints red,green,blue,yellow

# Case conversion
S = 'Hello, World!'
print(S.lower())
# Prints hello, world!

S = 'Hello, World!'
print(S.upper())
# Prints HELLO, WORLD!

S = 'Hello, World!'
print(S.capitalize())
# Prints Hello, world!

S = 'Hello, World!'
print(S.swapcase())
# Prints hELLO, wORLD!

S = 'hello, world!'
print(S.title())
# Prints Hello, World!

# Check if string is in the string
S = 'Hello, World!'
print('Hello' in S)
# Prints True

# Search for 'Foolish' within a string
S = 'Stay Hungry, Stay Foolish'
x = S.find('Foolish')
print(x)
# Prints 18

# Iterate over the string
# Print each character in a string
S = 'Hello, World!'
for letter in S:
    print(letter, end=' ')
# H e l l o ,   W o r l d ! 

S = "We're open"		# Escape single quote
S = "I said 'Wow!'"		# Escape single quotes
S = 'I said "Wow!"'		# Escape double quotes

# Escaping
S = "Bob told me, \"Sam said, 'This won't work.'\""
print(S)
# Prints Bob told me, "Sam said, 'This won't work.'"

S = str('First line.\n\tSecond line.')
print(S)
# First line.
#     Second line.

S = 'C:\new\text.txt'
print(S)
# C:
# ew	ext.txt
S = r'C:\new\text.txt'
print(S)
# C:\new\text.txt

# printf-style % string formatting
S = '%s is %d years old.' % ('Bob', 25)
print(S)
# Prints Bob is 25 years old.

# format() Built-in Method
S = '{1} is {0} years old.'.format(25, 'Bob')
print(S)
# Prints Bob is 25 years old.

# f-String Formatter
name = 'Bob'
age = 25
S = f"{name} is {age} years old."
print(S)
# Prints Bob is 25 years old.

# Python String Methods
# Python has a set of built-in methods that you can call on string objects.

# Method	Description
# capitalize()	Capitalizes first character of the string
# casefold()	Returns a casefolded string
# center()	Returns center-aligned string
# count()	Counts occurrences of a substring in a string
# encode()	Return an encoded version of the string as a bytes object
# endswith()	Determines whether the string ends with a given suffix
# expandtabs()	Replaces tabs with spaces
# find()	Searches the string for a given substring
# format()	Perform a string formatting operation
# format_map()	Perform a string formatting operation
# index()	Searches the string for a given substring
# isalnum()	Determines whether the string contains alphanumeric characters
# isalpha()	Determines whether the string contains alphabetic characters
# isdecimal()	Determines whether the string contains decimal characters
# isdigit()	Determines whether the string contains digits
# isidentifier()	Determines whether the string is a valid Python identifier
# islower()	Determines whether string contains lowercase characters
# isnumeric()	Determines whether the string contains numeric characters
# isprintable()	Determines whether string contains printable characters
# isspace()	Determines whether the string contains only whitespace characters
# istitle()	Determines whether the string is a titlecased string
# isupper()	Determines whether string contains uppercase characters
# join()	Joins all items in an iterable into a single string
# ljust()	Returns left-aligned string
# lower()	Converts all characters in a string to lowercase
# lstrip()	Strips characters from the left end of a string
# maketrans()	Returns a translation table to be used in translations
# partition()	Divides a string based on a separator
# replace()	Replaces occurrences of a substring within a string
# rfind()	Searches the string for a given substring
# rindex()	Searches the string for a given substring
# rjust()	Returns right-aligned string
# rpartition()	Divides a string based on a separator
# rsplit()	Splits a string into a list of substrings
# rstrip()	Strips characters from the right end of a string
# split()	Splits a string into a list of substrings
# splitlines()	Splits the string at line breaks
# startswith()	Determines whether the string starts with a given substring
# strip()	Strips leading and trailing characters
# swapcase()	Swaps case of all characters in a string
# title()	Converts string to “Title Case”
# translate()	Returns a translated string
# upper()	Converts all characters in a string to uppercase
# zfill()	Pads a string on the le with zeros