#  module = a file containing code you want to include in your program
#           use 'import' to include a module (bilt-in or self-made)
#           useful to break up a large program into reusable smaller files

import math             # this will give access to all the stuff available in math module
#import math as m       # nickname for the module
#from math import pi

print(math.pi)          # if using nickname, it will be m.pi

#print(help('modules'))      # information about the built-in modules
                            # help("module_name") can be used to know about specific module