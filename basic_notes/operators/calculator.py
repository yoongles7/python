# this is a simple calculator written in python

print("---CALCULATOR---")
operator = input("What calculation do you want to do? (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print (f"Addition: {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"Subtraction: {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"Multiplication: {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"Divison: {round(result, 3)}")
else:
    print("Invalid command!")
    