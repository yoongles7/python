# a program to convert kilograms to grams and vice-versa.
unit = int(input("Choose an option: \n1) kilogram -> gram \n2) gram -> kilogram \n"))

if unit == 1:
    weight = float(input("Enter your weight in kilogram: "))
    weight = weight * 1000
    print(f"Weight in gram is {round(weight, 3)}.")
elif unit == 2:
    weight = float(input("Enter your weight in gram: "))
    weight = weight / 1000
    print(f"Weight in kilogram is {round(weight, 3)}.")
else:
    print("Invalid unit!")