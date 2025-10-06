# variable = container for a value (string, integer, float, boolean)

name = "yoongles"       # string data type "" or ''
print(name)

age = 21        # integer data type, a whole number
print(f"age is {age}")      # f is fstring: used to print variables along with text

price = 1000.994     # a number with decimal places
print(f"the price is {price:.2f}")      # .2f will only show 2 decimal points and it rounds up the value same as you generally do in math

# boolean data types only have True and False
is_student = True
if is_student:
    print("you are a student")
else:
    print("you are not a student")

