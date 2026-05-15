import json


def load_pokemon(file_path):
    with open(file_path, "r", encoding="utf-8") as json_file:
        pokemon_list = json.load(json_file)

    return pokemon_list


def save_pokemon(file_path, data):
    if not data:
        print("No hay Pokémon para guardar")
        return

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def type_stats():
    hp = int(input("HP: "))
    attack = int(input("Ataque: "))
    defense = int(input("Defensa: "))
    sp_attack = int(input("Special attack: "))
    sp_defense = int(input("Special defense: "))
    speed = int(input("Speed: "))

    stats = {
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed
    }

    return stats


def type_skills(quantity):
    skills = []

    for i in range(quantity):
        skill = input(f"Skill #{i + 1}: ")
        skills.append(skill)

    return skills


def type_pokemon():
    name = input("Nombre del Pokémon: ")
    pokemon_type = input("Tipo del Pokémon: ")
    level = int(input("Nivel del Pokémon: "))
    weight_kg = float(input("Peso del Pokémon en kg: "))

    is_shiny_input = input("¿Es shiny? si/no: ").lower()
    is_shiny = is_shiny_input == "si"

    held_item = input("Held item. Déjelo vacío si no tiene: ")

    if held_item == "":
        held_item = None

    print("Ingrese 4 habilidades:")
    skills = type_skills(4)

    print("Ingrese las estadísticas:")
    stats = type_stats()

    pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

    return pokemon


def add_pokemon(pokemon_list):
    new_pokemon = type_pokemon()
    pokemon_list.append(new_pokemon)

    return pokemon_list


def main():
    file_path = "modify-.json"

    pokemon_list = load_pokemon(file_path)
    pokemon_list = add_pokemon(pokemon_list)

    save_pokemon(file_path, pokemon_list)

    print("Pokémon agregado correctamente.")


if __name__ == "__main__":
    main()