try:
    x = 1/0
except:
    print('Something went wrong.')
# Prints Something went wrong.

def this_fails():
    x = 1/0

try:
    this_fails()
except Exception as e:
    print(e)
# Prints division by zero

# Print one message for ZeroDivisionError and another for all other errors
try:
	x = 1/0
except ZeroDivisionError:
	print('Attempt to divide by zero')
except:
	print('Something else went wrong')
# Prints Attempt to divide by zero

# Execute same block of code for multiple exceptions
try:
    x = 1/0
except (ZeroDivisionError, ValueError):
    print('ZeroDivisionError or ValueError is raised')
except:
    print('Something else went wrong')
# Prints ZeroDivisionError or ValueError is raised

try:
    x = 1/1
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
# Prints Nothing went wrong

# finally clause is always executed
try:
	x = 1/0
except:
	print('Something went wrong')
finally:
	print('Always execute this')
# Prints Something went wrong
# Prints Always execute this

# Exception handling during file manipulation
# f = open('myfile.txt')
# try:
# 	print(f.read())
# except:
# 	print("Something went wrong")
# finally:
# 	f. close()

# Raise built-in exception 'NameError'
# raise NameError('An exception occured!')

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: An exception occured!

# Create and raise Custom exception 'InputError'
# class InputError(Exception):
#     pass

# raise InputError('Custom exception')

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# InputError: Custom exception