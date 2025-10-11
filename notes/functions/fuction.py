# function = A block of reusabel code
#            place () after function_name to invoke it
# def keyword is used to create a function

def happy_birthday(name, age):          # name and age are parameters
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()
    
happy_birthday("kacchan", 25)         # kacchan and 25 are arguments matching to the above parameters  
happy_birthday("kacchan", 25)
happy_birthday("kacchan", 25)

# return = statement used to end a function
#          and send a result to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    
    return first + " " + last

full_name = create_name("katsuki", "bakugo")
print(full_name)