# name = input("Enter your full name: ")

# result = len(name)      # no of characters (length) of the string including spaces
# result = name.find(" ")          # first occurance of the character
# result = name.rfind(" ")         # last occurance of the character and returns -1 for any character that is not in the string
# result = name.capitalize()       # first letter is capitalized
# result = name.upper()            # all the letter will be in uppercase
# result = name.lower()            # all the letter will be in lowercase
# result = name.isdigit()          # true if the string contains only digits false otherwise
# result = name.isalpha()          # true if the string contains only alphabets false otherwise not even a space is allowed

phone_number = input("Enter you phone number #: ")

result = phone_number.count("-")            # counts the number of a given character in the string
result = phone_number.replace("-", " ")     # replaces all occurance of a character in the string

# print(result)

print(help(str))        # help(data_type) gives the informations related to it