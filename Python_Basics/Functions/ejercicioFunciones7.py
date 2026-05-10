#Ejercicio 7
'''
Crear una funcion que acepte una lista de números y retorne una lista con los
numeros primos de la misma
'''

List1 = [1,4,6,7,13,9,67]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def return_prime_number(lista):
    prime_numbers = []
    for n in lista:
        if is_prime(n):
            prime_numbers.append(n)
    return prime_numbers

result = return_prime_number(List1)
print(result)
