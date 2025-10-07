# while loop = execute some code WHILE the condition remains true

name = input("Enter your name: ")

while name == "":
    print("you did not enter anything!")
    name = input("Enter your name: ")       # if we do not put this prompt here, we will get stuck in an infinite loop
    
print(f"Hello {name}!")