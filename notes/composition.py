# Composition = composed objet directly owns it's components, which cannot exist independently.
#               "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Bike:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)       # Bike owns the engine and wheel objects
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
        
    def display(self):
        return f"{self.make} {self.model} {self.engine.horse_power}hp {self.wheels[0].size}in"

bike = Bike("Kawasaki", "NinjaZX-10R", 200, 17)

print(bike.display())