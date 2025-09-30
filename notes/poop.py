# object = a bundle of related atrributes (variables) and methods (functions)
#          Ex. phone, book, cup
#          you need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from bike import Bike       # we can either import the classes like this or just code it in the main program

bike1 = Bike("Kawasaki", "2025", "Black", False)
bike2 = Bike("Honda", "2024", "Orange", "True")

print(bike1)
print(bike1.model)      # to access one of the attribute 
print(bike1.year)
print(bike1.color)
print(bike1.for_sale)

bike1.ride()            # this is how methods are accessed
bike2.stop()

bike1.describe()
bike2.describe()
