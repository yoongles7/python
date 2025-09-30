import math     # math module to use constants like pi 

# arithmetic operators
friends = 10        # = is assignment operator not "equal to", == is used for "equal to"

friends = friends + 1       # addition
# friends += 1              # same as above line, it is called augmented assignment operator
print(friends)

friends = friends - 1       # subtraction [friends -= 1]
print(friends)

friends = friends * 2       # multiplication [friends *= 2]
print(friends)

friends = friends / 2       # division [friends /= 2]
print(friends)

friends = friends ** 2       # exponent or power [friends **= 2]
print(friends)

friends = friends % 3      # modulus -> gives the remainder after division [friends %= 3]
print(friends)

# built-in math functions
x = 3.14
y = -4
z = 5

result = round(x)       # rounds the decimal points to nearest integer
print(result)

result = abs(y)         # absolute value of a number
print(result)

result = pow(4, 2)      # power or same as exponent (4^2)
print(result)

result = max(x, y, z)   # max between given values
print(result)

result = min(x, y, z)   # min between given values
print(result)

print(f"value of pi is {math.pi}")

result = math.sqrt(9)       # gives square root of a value
print(result)

result = math.ceil(9.1)     # always rounds value to higher value
print(result)

result = math.floor(9.9)    # always rounds value to lower value
print(result)