# the OG rock, paper, scissors game

import random

options = ("rock", "paper", "scissors")

c_score = 0
p_score = 0

running = True

print("---ROCK PAPER SCISSORS---")

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter your guess: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")
        
    if computer == player:
        print("It's a Tie!")
        c_score += 1 
        p_score += 1        
    elif computer == "rock" and player == "paper":
        print("You Win")
        p_score += 1        
    elif computer == "paper" and player == "scissors":
        print("You Win!")
        p_score += 1        
    elif computer == "scissors" and player == "rock":
        print("You Win!")
        p_score += 1       
    else:
        print("You Lose!")
        c_score += 1

    if input("Do you wanna play another round? (y/n): ").lower() == "n":
        print("Thanks for playing!")
        running = False

print(f"Player's Score = {p_score}")
print(f"Computer's Score = {c_score}")