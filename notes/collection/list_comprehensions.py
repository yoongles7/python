# List comprehension = a concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#doubles = []
#for x in range(1, 11):
#    doubles.append(x * 2)
    
doubles = [x * 2 for x in range(1, 11)]     # above code can be written as this
print(doubles)

fruits = ["apple", "banana", "coconuct", "orange"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6, 7]
positive_num = [num for num in numbers if num >= 0]
print(positive_num)