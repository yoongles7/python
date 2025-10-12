# default arguments = a default value for certain parameters
#                     default is used when that argument is omitted
#                     makes functions more flexible, and reduces # of arguments
#                     1. Positional  2. DEFAULT  3. Keyword  4. arbitrary

def net_price(list_price, discount=0, tax=0.05):        # discount and tax are parameters with default arguments
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))           # this will still work since other two parameters has default values