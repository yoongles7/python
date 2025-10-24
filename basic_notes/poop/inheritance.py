# inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Rabbit(Animal):
    def speak(self):
        print("PURR!")

dog = Dog("Herth")
cat = Cat("Catlana")
rabbit = Rabbit("Dash")

print(rabbit.name)
print(rabbit.is_alive)
rabbit.eat()
rabbit.sleep()

dog.speak()
cat.speak()
rabbit.speak()