class Car:
    pass

# Will run first time object is created
class Car:
    
    # initializer
    def __init__(self):
        pass

# A class with two instance attributes
class Car:

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

# A class with one class attribute
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

# Create an object from the 'Car' class by passing style and color
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

c = Car('Sedan', 'Black')

# Access and modify attributes of an object
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

c = Car('Black', 'Sedan')

# Access attributes
print(c.style)
# Prints Sedan
print(c.color)
# Prints Black

# Modify attribute
c.style = 'SUV'
print(c.style)
# Prints SUV

class Car:

    # class attribute
    wheels = 4

    # initializer / instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

    # method 1
    def showDescription(self):
        print("This car is a", self.color, self.style)

    # method 2
    def changeColor(self, color):
        self.color = color

c = Car('Black', 'Sedan')

# call method 1
c.showDescription()
# Prints This car is a Black Sedan

# call method 2 and set color
c.changeColor('White')

c.showDescription()
# Prints This car is a White Sedan

del c.color

del c