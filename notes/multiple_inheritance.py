# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multi-level inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A

class Animal:           # grandparents
    def eat(self):
        print("This animal is eating.")
        
    def sleep(self):
        print("This animal is sleeping.")
        
class Prey(Animal):             # parents
    def flee(self):
        print("This animal is fleeing.")
        
class Predator(Animal):         # parents
    def hunt(self):
        print("This animal is hunting.")
        
class Rabbit(Prey):             # child
    pass

class Hawk(Predator):           # child
    pass

class Fish(Prey, Predator):     # this is multiple inheritance
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
# rabbit.hunt() error

# hawk.flee() error
hawk.hunt()

fish.flee()
fish.hunt()
fish.eat()
fish.sleep()