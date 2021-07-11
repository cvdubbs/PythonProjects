class Person():
    def __init__(self, value):
        self.hidden_name = value

    # getter function
    def get_name(self):
        print('Getting name:')
        return self.hidden_name
    
    # setter function
    def set_name(self, value):
        print('Setting name to', value)
        self.hidden_name = value
    
    # make a property
    name = property(get_name, set_name)

p = Person('Bob')
print(p.name)
# Prints Getting name: Bob

p.name = "Sam"
# Prints Setting name to Sam

print(p.name)
# Prints Getting name: Sam

class Person():
    def __init__(self, value):
        self.hidden_name = value
    
    # getter function
    def get_name(self):
        print('Getting name:')
        return self.hidden_name

    # setter function
    def set_name(self, value):
        print('Setting name to', value)
        self.hidden_name = value
        
    # deleter function
    def del_name(self):
        print('Deleting name')
        del self.hidden_name

    # make a property
    name = property(get_name, set_name, del_name, doc='name of the person')

p = Person('Bob')

# calls the getter
print(p.name)
# Prints Getting name: Bob

# calls the setter
p.name = 'Sam'
# Prints Setting name to Sam

# docstring
print('Docstring:', Person.name.__doc__)
# Prints Docstring: name of the person

# calls the deleter
del p.name
# Prints Deleting name

class Person():
    def __init__(self, value):
        self.hidden_name = value
    
    @property
    def name(self):
        print('Getting name:')
        return self.hidden_name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        self.hidden_name = value
        
    @name.deleter
    def name(self):
        print('Deleting name')
        del self.hidden_name

p = Person('Bob')

# calls the getter
print(p.name)
# Prints Getting name: Bob

# calls the setter
p.name = 'Sam'
# Prints Setting name to Sam

# calls the deleter
del p.name
# Prints Deleting name

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(2, 5)

print(r.area)
# Prints 10

r.width = 3
r.height = 6

print(r.area)
# Prints 18

class Person():
    def __init__(self, value):
        self.hidden_name = value
    
    @property
    def name(self):
        print('Getting name:')
        return self.hidden_name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        self.hidden_name = value
        
    @name.deleter
    def name(self):
        print('Deleting name')
        del self.hidden_name

class SubPerson(Person):
    @property
    def name(self):
        print('Inside subperson getter')
        return super().name

    @name.setter
    def name(self, value):
        print('Inside subperson setter')
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Inside subperson deleter')
        super(SubPerson, SubPerson).name.__delete__(self)

s = SubPerson('Bob')

# calls the getter
print(s.name)
# Prints Inside subperson getter
# Prints Getting name: Bob

# calls the setter
s.name = 'Sam'
# Prints Inside subperson setter
# Prints Setting name to Sam

# calls the deleter
del s.name
# Prints Inside subperson deleter
# Prints Deleting name

class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Inside subperson getter')
        return super().name

class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Inside subperson setter')
        super(SubPerson, SubPerson).name.__set__(self, value)
