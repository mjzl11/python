import requests

def getPokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    response = requests.get(url)

    if response.status_code == 200:
        pokemonData = response.json()
        abilities = [ability["ability"]["name"] for ability in pokemonData["abilities"]]
        types = [type_info["type"]["name"] for type_info in pokemonData["types"]]

        print(f"Name: {pokemonData['name']}")
        print(f"abilities: {', '.join(abilities)}")
        print(f"Types: {', '.join(types)}")
    else:
        print("Error")

value = input('Search one pokemon: ')
getPokemon(value)