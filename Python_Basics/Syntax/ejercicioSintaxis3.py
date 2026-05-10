import random
print("Ejercicio 3")
#Crear un programa con un número secreto del uno al 10
#El programa no debe cerrarse hasta que el usuario adivine el numero
random_number = random.randint(1,10)
user_number = 0
while random_number != user_number:
	user_number = int(input ("ingresa un númeo entre 1 y 10 "))
	if user_number != random_number:
		print("inténtalo de nuevo")

print("Felicidades adivinaste el número")
