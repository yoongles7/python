import time

def count(end, start=0):
    for i in range(start, end):
        print(i)
        
        time.sleep(1)
    
    print("DONE!")
    
count(5)