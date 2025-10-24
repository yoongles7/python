import random

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

num = random.randint(1, 6)      # generates a random integer between 1 and 6
#num = random.randint(a, b)      # same result as above if a, b = 1, 6
print(num)

option = random.choice(options)     # random element from a collection or sequence
print(option)

number = random.random()            # random floating number between 0 and 1
print(number)

random.shuffle(cards)               # to shuffle a list
print(cards)