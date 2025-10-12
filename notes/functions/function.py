# function = a block of reusable code
#            place () after the fucntion_name to invoke it 

def happy_birthday(name, age):          # name and age are parameters
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    
happy_birthday(name="Katsuki", age=25)           # positional arguments matching to the parameters
happy_birthday("Katsuki", 25)
happy_birthday("Katsuki", 25)

# return = statement used to end a function and send a result back to the caller
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
    
full_name = create_name("Katsuki", "Bakugo")
print(full_name)