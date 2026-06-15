#Ejercicio 3
#Crear una funcion que reciba como parámetro una lista y devuelva la suma de la misma
from logging import raiseExceptions

#list1 = [1,2,3,4,5,6,7]
list1 = []

def sum_list(list):
    sum = 0
    try:
        if len(list) == 0:
            return "La lista está vacía"
        else:
            for elem in list:
                sum += elem
            return sum

    except TypeError:
        return "Error"


print("la suma de la lista es: ", sum_list(list1))

