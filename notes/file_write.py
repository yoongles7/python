# python writting files (.txt, .json, .csv)

import json
import csv

text_data = "I love Rabbits!"

file_path = '/home/yoongles/python/assets/output.txt'

# mode = 'w' or 'x' or 'a'
#         w will overwrite the file if exists already
#         x will throw an error if file already exits
#         a will keep adding the data to the file

with open(file_path, 'w') as file:   
    file.write(text_data)
    print(f"txt file '{file_path}' was created.")
    
# writting a .json file
employee = {
    "name": "Katsuki", 
    "age": "25",
    "job": "professional_motoGP_rider"
}
file_path = '/home/yoongles/python/assets/output.json'

with open(file_path, 'w') as file:   
    json.dump(employee, file, indent=4)
    print(f"json file '{file_path}' was created.")
    
# writting a .csv file
employees = [["Name", "Age", "Job"],

             ["Spongebob", 30, "Cook"],

             ["Patrick", 37, "Unemployed"],

             ["Sandy", 27, "Scientist"]]

file_path = '/home/yoongles/python/assets/output.csv'

with open(file_path, 'w', newline="") as file:   
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
        
    print(f"csv file '{file_path}' was created.")