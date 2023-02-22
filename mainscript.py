from poke_api import search_for_pokemon
from pastebin_api import post_new_paste
from sys import argv

def main():
    pokemon_name = argv[1]
    print(f'Getting information for {pokemon_name}')
    pokemon = search_for_pokemon(pokemon_name)

    if pokemon:
        title, body_text = get_pokemon_data(pokemon_name, pokemon)
        paste_url = post_new_paste(title, body_text, '1M')
        print(f'Posting new paste to PasteBin...\n{paste_url}')

def get_pokemon_data(pokemon_name, pokemon):
    title = f"{pokemon_name}'s abilities".capitalize()
    pokemon_abilities = [" - "+a['ability']['name'] for a in pokemon['abilities']]
    divider = '\n'
    body_text = divider.join(pokemon_abilities)
    return title, body_text

if __name__ == '__main__':
    main()