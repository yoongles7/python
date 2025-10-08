# for loops = execute a block of code a fixed number of times.
#             can iterate over a range, string, sequence, etc. ( anything that is iterable )

for i in range(1, 10):      # range(start, stop, step)
    print(i)

for x in range(1, 10):
    if x == 5:
        continue       # continues the loop skipping that number
    else:
        print(x)
        
for y in range(1, 10):
    if y == 5:
        break         # breaks out of the loop 
    else:
        print(y)