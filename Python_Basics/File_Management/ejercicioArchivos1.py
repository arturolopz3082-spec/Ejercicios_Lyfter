#Ejercicio1
'''
Cree un programa que lea nombres de canciones en un archivo
y lo guarde ordenado en otro
'''
file_path = '/Users/arturolopez/Documents/lyfter/pythonBasico/ejercicioManejoArchivos/'
file_name = 'canciones.txt'
ordered_file_name = 'cancionesOrdenadas.txt'

def open_file():
    with open(file_path+file_name, 'r') as file:
        lines = file.readlines()
        return sorted(lines)

def save_file():
    lines = open_file()
    with open(file_path+ordered_file_name, 'w') as file:
        for elem in lines:
            file.write(elem)

save_file()
