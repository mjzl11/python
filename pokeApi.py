import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
        types = [type_info["type"]["name"] for type_info in pokemon_data["types"]]

        print(f"Nombre: {pokemon_data['name']}")
        print(f"Habilidades: {', '.join(abilities)}")
        print(f"Tipos: {', '.join(types)}")
    else:
        print("Error al obtener la información del Pokémon.")

# Ejemplo de uso
get_pokemon_info("pikachu")