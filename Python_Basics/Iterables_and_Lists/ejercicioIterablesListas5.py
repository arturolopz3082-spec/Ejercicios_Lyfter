my_list=[]
for i in range(10):
    print("Favor de ingresar un número a tu lista")
    numero = int(input("numero: "))
    my_list.append(numero)
print("Tu lista es: ", my_list)
print("El número más alto es", max(my_list))
