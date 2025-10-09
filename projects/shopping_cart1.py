foods = []
prices = []
total = 0

while True: 
    food = input("Enter any food you like (q to quit): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of {food}: Rs."))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")
for food in foods:
    print(f"{food}", end=" ")

print()

for price in prices:
    total += price
    print(f"{price}", end=" ")

print()

print(f"Your total = Rs.{total}")