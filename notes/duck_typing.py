# Duck Typing = a way to achieve polymorphism 
#               object can be treated as a type as long as it meets the minimum attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
    
    def speak(self):
        print("HONK!")
        
animals = [Dog(), Cat(), Car()]     # car can be considered animal since it has the necessary attribute and method

for animal in animals:
    animal.speak()
    print(animal.alive)