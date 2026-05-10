#Ejercicio 2
#Scope

global_var = "soy una variable global :)"

def fun1():
    local_var = "soy una variable local :)"

#print(local_var) no me deja invocar a la variable local desde fuera, porque no está definida

def fun2():
    global global_var
    global_var = "soy una variable global y me modificaron :("
    print(global_var)

fun2()
