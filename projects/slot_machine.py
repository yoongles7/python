# This is a python slot machine game where you win a round if you spin all 3 same emojies

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '🌟']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '🌟':
            return bet * 10
    else:
        return 0
    

def main():
    balance = 100
    
    print("------------------------------")
    print("Welcome to Python Slot Machine")
    print("Symbols: 🍒 🍉 🍋 🔔 🌟")
    print("------------------------------")
    
    while balance > 0:
        print(f"\nCurrent Balance: Rs. {balance}")
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number!")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds!")
            continue
        
        if bet <= 0:
            print("Bet amount should be greater than zero!")
            continue
        
        balance -= bet
        
        row = spin_row()
        
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won Rs.{payout}")
            balance += payout
        else:
            print("Sorry! You lost this round.")
    
        if input("\nDo you want to play again? (y/n): ").lower() == 'n':
            break
    


if __name__ == "__main__":
    main()