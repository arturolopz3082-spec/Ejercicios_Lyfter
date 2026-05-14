
import csv


def save_games_ranking(file_path, data):
    if not data :
        print ("No hay videojuegos para guardar")
        return

    with open(file_path, 'w', newline='') as csv_file:
        headers = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def type_game():
    name = input('Nombre del juego: ')
    genre = input('Genero del juego: ')
    developer = input('Desarrollador del juego: ')
    clasification = input('Clasificacion del juego: ')

    videogame = {
        'nombre': name,
        'genero': genre,
        'desarrollador': developer,
        'clasificacion': clasification,
    }

    return videogame

def request_videogames(quantity):
    videogames = []
    for i in range(quantity):
        print(f'El videojuego #{i+1}')
        videogame = type_game()
        videogames.append(videogame)
    return videogames

def main():
    file_path = "top_games.csv"

    quantity = int(input('cuantos juegos deseas agregar?: '))
    videogames = request_videogames(quantity)
    save_games_ranking(file_path, videogames)
    print("El archivo fue creado con exito")


if __name__ == '__main__':
    main()
