# logical operators -> used on conditional statements
#                      and -> True if two or more conditions are True
#                      or -> True if at least one condition is True
#                      not -> True if condition is False and vice-versa

temp = 25
sunny = True

if temp > 0 and temp < 30:
    print("Temperature is good.")
else:
    print("Temperature is bad.")
    
if temp <= 0 or temp >= 30:         # this statement works the same as above if statement logically
    print("Temperature is bad.")
else:
    print("Temperature is good.")

if not sunny:
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")
    