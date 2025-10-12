menu = {"Popcorn": 300,
        "Coffee": 260,
        "Lemonade": 150,
        "Ice-cream": 200,
        "Chips": 110,
        "Pizza": 500}

cart = []
total = 0

print("-----MENU-----")
for key, value in menu.items():
    print(f"{key:10}: Rs.{value}")
print("--------------")

while True:
    food = input("Enter what you want (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---YOUR ORDER---")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Total is: Rs.{total}")