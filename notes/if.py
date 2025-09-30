# if = do some code only if the condition is True else do something else

age = int(input("What is your age? "))

if age >= 18:
    # if True condition
    print("You are signed up!")             # INDENTS (the space before print)  IS VERY IMPORTANT 
elif age < 0:                               # elif is used if we have more than one condition
    print("You haven't been born yet!")     # code to perform if second condition is true
else:
    # if False condition
    print("You must be 18+ to sign up!")