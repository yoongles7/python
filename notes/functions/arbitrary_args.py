# *args = allows to pass multiple non-key arguments
# **kwargs = allows to pass multiple keyword arguments
#            * unpacking operator
#            1. positional   2. default   3. keyword   4. ARBITRARY

def add(*args):         # args are a tuple
    total = 0
    for arg in args:
        total += arg
    return total

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()
    
print(add(1, 2, 3, 5, 6, 8))
display_name("Great", "Explosion", "Murder", "God", "DYNAMIGHT")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_address(street="123 Fake St.",
              apt="100",
              city="Kathmandu",
              state="Bagmati",
              zip="46000")