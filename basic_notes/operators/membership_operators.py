# Membership operators = used to test whether a value exists in a sequence or not
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
    
#if letter not in word:                  |
#   print(f"{letter} was not found")     |--> this code works the same as above 
#else:                                   |
#   print(f"There is a {letter}")        |

students = {"Bakugo Katsuki", "Kirishima Eijiro", "Todoroki Shoto", "Midoriya Izuku"}

student = input("Enter a student's name: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
    
grades = {"Bakugo": "A",
          "Todoroki": "A+",
          "Midoriya": "B"}

std = input("Enter the name of a student: ")

if std in grades:
    print(f"{std}'s grade is {grades[std]}")
else:
    print(f"{std} was not found")
    
email = "katsukibakugo@hero.agency"

if "@" in email and "." in email:
    print("Valid email!")
else:
    print("Invalid email!")