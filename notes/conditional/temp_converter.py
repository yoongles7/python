# a program to convert temperature units from celsius to farenheit and vice-versa.

temp = float(input("Enter the temperature: "))
unit = input("what is the unit of current temperature? (C/F): ")

if unit == "C":
    temp = round((temp * 1.8) + 32, 2)
    print(f"Temperature: {temp}F.")
elif unit == "F":
    temp = round((temp - 32) / 1.8, 2)
    print(f"Temperature: {temp}C.")
else:
    print("Invalid unit!")
    