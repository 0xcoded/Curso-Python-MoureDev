#Buenas prácticas: Nombre de variable en minúsculas
myvariable = "test"
print(myvariable)

my_bool_variable = False
#Para concatenar deben ser strings (str)
print("Longitud: " + str(len(myvariable)))

#EVITAR STR:
print("(sin la función str), Longitud:", len(myvariable))

#Prueba rara de brais
print(type(print("Test")))  #NoneType, una función no es un tipo de dato

#Variables en una línea
'''Puede ser confuso asignar el valor a la variable correcta
Usar con cuidado'''
name,age = "david",34
print("Hola", name + ",", age,"años")

#Input (RECORDAR NO ABUSAR de las variables en múltiples líneas, pero es válido)
name,age = input("Nombre: "),input("Edad: ")
print("Hola", name + ",", age,"años")