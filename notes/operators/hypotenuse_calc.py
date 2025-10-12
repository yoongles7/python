# calculates hypotenuse (longest side) of the right triangle
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Hypotenuse of the triangle is {c} units.")