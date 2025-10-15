# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# from math import e    # e is built-in variable
#x = 3                  # x is global variable
def func1():
    #x = 1              # x is local to func1 and func2 cannot use it
    print(x)
    
    # x above is enclosed version of x and func1 and func2 both can use it
    #def func2():
        #x = 2          # x func2 will first use this value instead of the enclosed one
        #print(x)
        
def func2():
    #x = 2              # x is local to func2 and func1 cannot use it
    print(x)
    
func1()
func2()
