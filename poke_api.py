import requests

POKE_URL = 'https://pokeapi.co/api/v2/pokemon/'

def search_for_pokemon(pokedex_info):
    pokedex_info = str(pokedex_info).strip().lower()
    pokedex = POKE_URL + pokedex_info
    resp_msg = requests.get(pokedex)
    if resp_msg.ok:
        info = resp_msg.json()
        real = True
        return info, real
    else:
        real = False
        return None, real
        
print(search_for_pokemon('Ninetales'))
