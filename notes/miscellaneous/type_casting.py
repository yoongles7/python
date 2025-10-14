# type_casting: converting one data type into another data type

name = "yoongles"
age = 21
gpa = 3.25
student = True

# type(variable_name) gives the data type of the variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# explicit conversion: manual using keywords like int, float, bool, str
age = float(age)
print(type(age))

gpa = int(gpa)
print(type(gpa))

name = bool(name)       # when casted to a boolean, anything other than 0 and '' or "" will result in True
print(name)

# implicit conversion: automatic conversion
x = 2
y = 2.0 
x = x / y       # x will be converted to float here due to the arithmetic operation
print(f"x = {x} and type: {type(x)}")