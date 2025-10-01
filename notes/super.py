# super = function within child class to call methods from parent class (superClass)
#         allows to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")
        
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2} square units.")
        super().describe()      # this is how the method of child can be extended otherwise only child's method will be excessed

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
square = Square("green", False, 5)
triangle = Triangle("blue", False, 3, 4)

circle.describe()