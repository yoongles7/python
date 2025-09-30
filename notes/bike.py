class Bike:     # bike is the ClassName
    def __init__(self, model, year, color, for_sale):       # __init__ is dunder(double underscore) method, self is already provided as the syntax and model, year, color, etc. are attributes here.
        self.model = model      # this is an object
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def ride(self):         # methods = actions that objects can perform
        print(f"You ride the {self.color} {self.model}!")
        
    def stop(self):
        print(f"You stop the {self.color} {self.model}!")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")