# Polymorphism = a greek word meaning "have many faces or forms"
#               poly = many
#               morphe = form

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inhaeritance -> an object could be treated as the same type as a parent class
#               2. Duck Typing -> object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):            # it is a circle and a shape
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):            # It is a square and a shape
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):          # it is a triangle and a shape
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):            # it is a pizza, a circle, and a shape
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
        
shapes = [Circle(3), Square(5), Triangle(3, 4), Pizza("Pepproni", 15)]

for shape in shapes:
    print(shape.area())