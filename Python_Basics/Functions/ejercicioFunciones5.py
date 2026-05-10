#Ejercicio5
#Crear una funcion que imprima el número de mayúsculas y minúsculas en un string

string1 = "I love Nacion Sushi"

def contarLetras(text):
    lowerCase = 0
    upperCase = 0
    for element in text:
        if element.isupper():
            upperCase += 1
        elif element.islower():
            lowerCase += 1
    return print(f"There is {upperCase} uppercase letters and {lowerCase} lowercase letters.")

contarLetras(string1)
