username = input("Enter you username: ")

if len(username) > 12:
    print("username must not contain more than 12 characters!")
elif not username.find(" ") == -1:
    print("username must not contain spaces!")
elif not username.isalpha():
    print("username must not contain digits!")
else:
    print(f"Welcome {username} :)")
