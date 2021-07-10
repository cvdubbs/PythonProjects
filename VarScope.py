def myfunc():
    x = 42      # local scope x
    print(x)

myfunc()        # prints 42

# global scope x
x = 42          # global scope x

def myfunc():
    print(x)    # x is 42 inside def

myfunc()
print(x)        # x is 42 outside def

verbose = True

def op1():
    if verbose:
        print('Running operation 1')

x = 42          # global scope x
def myfunc():
    x = 0
    print(x)    # local x is 0

myfunc()
print(x)        # global x is still 42

x = 42          # global scope x
def myfunc():
    global x    # declare x global
    x = 0
    print(x)    # global x is now 0

myfunc()
print(x)        # x is 0

x = 42          # global scope x

def myfunc():
    global x
    x = x + 1   # global x is now 43
    print(x)

myfunc()
print(x)        # x is 43

# enclosing function
def f1():
    x = 42
    # nested function
    def f2():
        x = 0
        print(x)    # x is 0
    f2()
    print(x)        # x is still 42
    
f1()

# enclosing function
def f1():
    x = 42
    # nested function
    def f2():
        nonlocal x
        x = 0
        print(x)    # x is now 0
    f2()
    print(x)        # x remains 0
    
f1()

# Built in -> Globals() -> locals() -> builtins()