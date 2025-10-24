# a game to guess a random number generated
import random

a, b = 1, 100
num = random.randint(a, b)
guesses = 0
is_running = True

print("Welcome to the number guessing game :)")
print(f"Select a number between {a} and {b}")

while is_running:
    
    guess = input(f"Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < a or guess > b:
            print(f"{guess} is out of range!")
        elif guess < num:
            print(f"{guess} is too low.")
        elif guess > num: 
            print(f"{guess} is too high.")
        else:
            print(f"{guess} is correct!")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess!")
        guess = input(f"Please enter a number between {a}-{b}: ")
        