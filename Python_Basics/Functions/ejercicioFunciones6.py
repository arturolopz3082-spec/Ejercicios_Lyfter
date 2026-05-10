#Ejercicio 6
#Crear una funcion que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabeticamente

string1 = "python-variable-funcion-computadora-monitor"

def order_words(string):
    word_list = string.split('-')
    ordered_list = sorted(word_list)
    ordered_string = '-'.join(ordered_list)
    return ordered_string

print(order_words(string1))

