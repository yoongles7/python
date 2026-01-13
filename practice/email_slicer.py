# a program that slices email into it's username and domain

email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"username: {username}")
print(f"domain: {domain}")