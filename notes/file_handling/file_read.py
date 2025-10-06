# python reading files (.txt, .json, .csv)

import json
import csv 

# file_path = 'hello.txt' would be relative file path and the file will be created in same folder as this program
file_path = '/home/yoongles/python/assets/hello.txt' # this is absolute file path

# in case you didn't put the file path correctly, there will be errors 
try:
    with open(file_path, 'r') as file:      # r is mode (r for read mode)
        content = file.read()
        print(content)
except FileNotFoundError:       # error related to wrong file path or no file found
    print("That file was not found!")
except PermissionError:         # if you try to open a file with no permission
    print("You do not have the permission to open that file!")

# reading of .json file
file_path = '/home/yoongles/python/assets/sample.json'

try:
    with open(file_path, 'r') as file:     
        content = json.load(file)       # for .json file json.load() is used to read
        print(content)
        print(content["name"])          # a value can be accessed with key like this in .json file
except FileNotFoundError:      
    print("That file was not found!")
except PermissionError:         
    print("You do not have the permission to open that file!")
    
# for a .csv file
file_path = '/home/yoongles/python/assets/sample.csv'

try:
    with open(file_path, 'r') as file:     
        content = csv.reader(file)      # for .csv file csv.reader() is used
        print(content)
        for line in content:
            print(line)                 # you can use index for specific value of the content
except FileNotFoundError:      
    print("That file was not found!")
except PermissionError:         
    print("You do not have the permission to open that file!")