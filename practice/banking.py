def show_balance(balance):
    print("--------------------------------")
    print(f"Your balance is Rs.{balance:.2f}")
    print("--------------------------------")

def deposit():
    print("--------------------------------")
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount!")
        return 0
    else:
        return amount

    print("--------------------------------")

def withdraw(balance):
    print("--------------------------------")
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount < 0:
        print("That's not a valid amount!")
        return 0
    elif amount > balance:
        print("Insufficient balance!")
        return 0
    else:
        return amount 
    
    print("--------------------------------")

balance = 0

def main():
    balance = 0
    is_running = True
    while is_running:
        print("---------BANKING PROGRAM--------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("--------------------------------")
        choice = int(input("Enter your choice (1-4): "))
    
        match choice:
            case 1:
                show_balance(balance)
            case 2:
                deposited_amount = deposit()
                if deposited_amount > 0:
                    balance += deposited_amount    
                    print(f"You deposited Rs.{deposited_amount}")  
                    print(f"New Balance: Rs.{balance}")  
            case 3:
                withdrawn_amount = withdraw(balance)
                if withdrawn_amount > 0:
                    balance -= withdrawn_amount
                    print(f"You withdrew Rs.{withdrawn_amount}")
                    print(f"Remaining Balance: Rs.{balance}")
            case 4:
                is_running = False
                print("Thank you! Have a nice day.")
            case _:
                print("That is not a valid choice!")
            

if __name__ == "__main__":
    main()        