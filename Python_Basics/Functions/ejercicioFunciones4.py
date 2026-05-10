#Ejercicio4
#Crear una funcion que le dé la vuelta a un string y lo retorne
string1 = "hola, mundo!"

def reverse_string(text):
    reversed_text = ""
    for i in range(len(text)-1, -1, -1):
        reversed_text += text[i]
    return reversed_text

print(reverse_string(string1))
