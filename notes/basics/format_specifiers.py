# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# .(number) = round to that many decimal places (fixed pint)
print(f"price1 is {price1:.2f}")
print(f"price2 is {price2:.2f}")
print(f"price3 is {price3:.2f}")

# :(number) = allocate that many spaces 
print(f"price1 is {price1:10}")
print(f"price2 is {price2:10}")
print(f"price3 is {price3:10}")

# :03 = allocate and zero pad that many spaces
print(f"price1 is {price1:010}")
print(f"price2 is {price2:010}")
print(f"price3 is {price3:010}")

# :< = left justify
print(f"price1 is {price1:<}")
print(f"price2 is {price2:<}")
print(f"price3 is {price3:<}")

# :> = right justify
print(f"price1 is {price1:>}")
print(f"price2 is {price2:>}")
print(f"price3 is {price3:>}")

# :^ = center align
print(f"price1 is {price1:^}")
print(f"price2 is {price2:^}")
print(f"price3 is {price3:^}")

# :+ = use a plus sign to indicate positive value
print(f"price1 is {price1:+}")
print(f"price2 is {price2:+}")
print(f"price3 is {price3:+}")

# := = place a sign to leftmost position
print(f"price1 is {price1:=}")
print(f"price2 is {price2:=}")
print(f"price3 is {price3:=}")

# : = insert a space before positive numbers
print(f"price1 is {price1: }")
print(f"price2 is {price2: }")
print(f"price3 is {price3: }")

# :, = comma separator
print(f"price1 is {price1:,}")
print(f"price2 is {price2:,}")
print(f"price3 is {price3:,}")

# we can mix and match multiple specifiers
print(f"price1 is {price1:+,.2f}")
print(f"price2 is {price2:+,.2f}")
print(f"price3 is {price3:+,.2f}")