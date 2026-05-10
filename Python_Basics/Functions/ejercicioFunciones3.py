#Ejercicio 3
#Crear una funcion que reciba como parámetro una lista y devuelva la suma de la misma

list1 = [1,2,3,4,5,6,7]

def sum_list(list):
    sum = 0
    for elem in list:
        sum += elem
    return sum

print("la suma de la lista es: ", sum_list(list1))

