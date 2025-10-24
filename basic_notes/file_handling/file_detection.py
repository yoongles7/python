# python file detection
import os

file_path = '/home/yoongles/python/assets/hello.txt'

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
    
    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("That is a directory.")
else:
    print("That file doesn't exist.")