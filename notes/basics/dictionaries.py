# dictionary = a collection of {key:value} pairs
#              ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C", 
            "Japan": "Tokyo",
            "Nepal": "Kathmandu", 
            "South Korea": "Seoul"}

#print(capitals.get("Japan"))                # to get value associated with a key
#capitals.update({"China": "Beijing"})       # to add a value pair or change a value pair
#capitals.update({"USA": "Detroit"})
#capitals.pop("USA")                         # to remove a value
#capitals.popitem()                          # to remove the last or latest added value

#keys = capitals.keys()                       # returns all the keys of the dictionary as a list
#print(keys)

#values = capitals.values()                   # returns all the values of the dictionary
#print(values)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")