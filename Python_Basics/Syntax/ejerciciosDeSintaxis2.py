print("Ejercicio 2")
#Crear un programa que pida al usuario Nombre, Apellido y edad.
#Mostrar si es un bebé, niño, preadolescente, adulto joven, adulto, adulto mayor

name = input("ingresa tu nombre: ")
lastname = input("ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))

if age < 0:
	print("la edad no puede ser negativa")
elif age < 3:
	age_moment = "bebe"
elif age < 10:
	age_moment = "niño"
elif age < 13:
	age_moment = "preadolescente"
elif age < 17:
	age_moment = "adolescente"
elif age < 30:
	age_moment = "adulto joven"
elif age < 70:
	age_moment = "adulto"
else:
	age_moment = "adulto mayor"

print(f"{name} {lastname} está en la etapa {age_moment}")
