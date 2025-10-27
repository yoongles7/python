# How to connect to an API using Python

import requests


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
poekemon_info = get_pokemon_info(pokemon_name)

if poekemon_info:
    print(f"Name: {poekemon_info["name"].capitalize()}")
    print(f"ID: {poekemon_info["id"]}")
    print(f"Height: {poekemon_info["height"]}")
    print(f"Weight: {poekemon_info["weight"]}")