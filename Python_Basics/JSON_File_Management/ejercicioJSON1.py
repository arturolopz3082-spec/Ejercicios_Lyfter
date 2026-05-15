import json

path = "/Users/arturolopez/Documents/lyfter/pythonBasico/ejercicioJSON/"
file_name = "modify-.json"


def open_file(file_path):
    with open(file_path, "r", encoding="utf-8") as json_file:
        pokemon_list = json.load(json_file)

    return pokemon_list


def write_file(file_path, pokemon_list):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(pokemon_list, json_file, indent=4, ensure_ascii=False)


def create_pokemon():
    name = input("Ingrese el nombre del Pokémon: ")
    pokemon_type = input("Ingrese el tipo del Pokémon: ")
    level = int(input("Ingrese el nivel del Pokémon: "))
    weight_kg = float(input("Ingrese el peso del Pokémon en kg: "))

    is_shiny_input = input("¿El Pokémon es shiny? si/no: ").lower()
    is_shiny = is_shiny_input == "si"

    held_item = input("Ingrese el held item. Déjelo vacío si no tiene: ")

    if held_item == "":
        held_item = None

    skills = []

    print("Ingrese 4 habilidades:")
    for i in range(4):
        skill = input(f"Habilidad {i + 1}: ")
        skills.append(skill)

    stats = create_stats()

    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

    return new_pokemon


def create_stats():
    hp = int(input("Ingrese HP: "))
    attack = int(input("Ingrese attack: "))
    defense = int(input("Ingrese defense: "))
    sp_attack = int(input("Ingrese special attack: "))
    sp_defense = int(input("Ingrese special defense: "))
    speed = int(input("Ingrese speed: "))

    stats = {
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed
    }

    return stats


def main():
    file_path = path + file_name

    pokemon_list = open_file(file_path)

    new_pokemon = create_pokemon()

    pokemon_list.append(new_pokemon)

    write_file(file_path, pokemon_list)

    print("Pokémon agregado correctamente.")


if __name__ == "__main__":
    main()