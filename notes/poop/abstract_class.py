# Abstract calss: A class that cannot be instantiated on its own; meant to be subclassed.
#                 can contain abstract method, which are declared but have no implementation.
#                 benefits:
#                 1) prevents instantiation of the class itself
#                 2) requires children to use inherited abstract methods

from abc import ABC, abstractmethod # abc = abstract base class

class Vehicle(ABC):         # i don't want myself or any other developers to be able to create a vehicle object
    
    @abstractmethod         # decorator to be able to declare abstract method
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
# vehicle = Vehicle()       # throws an error

class Car(Vehicle):
    def go(self):
        print("You drive the car.")
    
    def stop(self):
        print("You stop the car.")

car = Car()
car.go()
car.stop()

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle.")
        
    def stop(self):
        print("You stop the motorcycle.")
        
motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()