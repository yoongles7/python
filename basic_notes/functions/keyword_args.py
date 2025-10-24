# keyword arguments = an argument preceeded by an identifier
#                     helps with readability
#                     order of arguments does not matter
#                     1. positional  2. default   3. KEYWORD   4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Bakugo", first="Katsuki")

for i in range(1, 11):
    print(i, end=" ")           # end is a keyword argument built-in inside the print function
    