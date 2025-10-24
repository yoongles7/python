# this tells you how much do you need to pay for the selected item(s)

item = input("What item would you like to buy? ")
price = float(input("what is the price? "))
quantity = int(input("How many of this item would you like? "))

total = price * quantity

print(f"you have bought {quantity} {item}/s.")
print(f"your total is: ${round(total, 2)}")