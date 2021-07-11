# base class
class Vehicle():
    def description(self):
        print("I'm a Vehicle!")

# base class
class Vehicle():
    def description(self):
        print("I'm a Vehicle!")

# subclass
class Car(Vehicle):
    pass

# base class
class Vehicle():
    def description(self):
        print("I'm a Vehicle!")

# subclass
class Car(Vehicle):
    pass

# create an object from each class
v = Vehicle()
c = Car()

v.description()
# Prints I'm a Vehicle!
c.description()
# Prints I'm a Vehicle!

# base class
class Vehicle():
    def description(self):
        print("I'm a Vehicle!")

# subclass
class Car(Vehicle):
    def description(self):
        print("I'm a Car!")

# create an object from each class
v = Vehicle()
c = Car()

v.description()
# Prints I'm a Vehicle!
c.description()
# Prints I'm a Car!

# a parent class
class Vehicle():
    def description(self):
        print("I'm a", self.color, "Vehicle")

# subclass
class Car(Vehicle):
    def description(self):
        print("I'm a", self.color, self.style)
    def setSpeed(self, speed):
        print("Now traveling at", speed,"miles per hour")    

# create an object from each class
v = Vehicle()
c = Car()

c.setSpeed(25)
# Prints Now traveling at 25 miles per hour
# v.setSpeed(25)
# Triggers AttributeError: 'Vehicle' object has no attribute 'setSpeed'

# base class
class Vehicle():
    def __init__(self, color):
        self.color = color
    def description(self):
        print("I'm a", self.color, "Vehicle")

# subclass
class Car(Vehicle):
    def __init__(self, color, style):
        super().__init__(color)    # invoke Vehicle’s __init__() method
        self.style = style
    def description(self):
        print("I'm a", self.color, self.style)

# create an object from each class
v = Vehicle('Red')
c = Car('Black', 'SUV')

v.description()
# Prints I'm a Red Vehicle
c.description()
# Prints I'm a Black SUV

class Car(Vehicle):
    def __init__(self, color, style):
        self.color = color
        self.style = style
    
    def description(self):
        print("I'm a", self.color, self.style)

# Multiple Inheritance
# base class 1
class GroundVehicle():
    def drive(self):
        print("Drive me on the road!")

# base class 2
class FlyingVehicle():
    def fly(self):
         print("Fly me to the sky!")

# subclass
class FlyingCar(GroundVehicle, FlyingVehicle):
    pass

# create an object of a subclass
fc = FlyingCar()

fc.drive()
# Prints Drive me on the road!
fc.fly()
# Prints Fly me to the sky!