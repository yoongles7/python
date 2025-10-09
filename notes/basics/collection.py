# collection = single "variables" used to store multiple values and these are iterable
# List  = [] ordered and changeable. duplicates are OK
# Set   = {} unodered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates are OK. Faster

fruits1 = ['apple', 'banana', 'orange', 'coconut']
#fruits2 = {'apple', 'banana', 'orange', 'coconut'}
#fruits3 = ('apple', 'banana', 'orange', 'coconut')

#print(dir(fruits))      # returns a list of methods that can be performed
#print(help(fruits))
print(fruits1)
print('apple' in fruits)        # checks if certain value is inside the list