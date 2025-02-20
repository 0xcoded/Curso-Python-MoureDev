#Declaración
my_dict = dict()
my_dict2 = {}

#{} se usa en sets, pero al ser clave-valor se interpreta como diccionario
my_dict2 = {"name":"David","age":34,"height":2.04}
print(type(my_dict2))
print(my_dict2)

#No importa el tipado de la clave
my_dict = {
    "name":"David",
    "age":34,
    "languajes": {"Python","JavaScript"},    #Tipado debil, asigna un set al valor de la clave "languajes"
    7:"test"
}
print(my_dict)
print(len(my_dict))     #Obtenemos el número de claves, no el número de valores!!
print(my_dict["languajes"])     #Contenido de la clave languajes '{'JavaScript', 'Python'}'

print(my_dict[7])       #NO ACCEDEMOS A LA POSICIÓN 7, sino a la clave int(7)
#print(my_dict[1])       #¡¡ERROR!! No existe la clave, no es la posición => KeyError: 1

my_dict["city"] = "Valencia, España"    #Podemos crear una clave aunque no exista y darle un valor posteriormente
print(my_dict)
print(my_dict["city"])

del my_dict[7]      #Eliminamos la clave 7, no el diccionario completo!
print(my_dict)

#Buscamos un dato ¡POR CLAVE! No por valor como anteriormente
print("David" in my_dict)   #False, buscamos por clave!
print("name" in my_dict)    #True

print(my_dict.keys())   #Obtenemos claves
print(my_dict.values()) #Valores
print(my_dict.items())  #Ontemos el contenido del diccionario

#Crear diccionario con las claves indicadas, pero sin valores, pero sin valores
my_new_dict = my_dict.fromkeys(("name","age"))
print(my_new_dict)
my_new_dict["name"] = "Noelia"
my_new_dict["age"] = 32
print(my_new_dict)

#Replicar valor en todas las claves de un diccionario
my_new_dict2 = my_dict.fromkeys(my_dict,"Valor asignado")
print(my_new_dict2)

#Al transformarlo en una lista, obtenemos las claves, no los valores
my_list = list(my_dict)
print(f"Lista de claves del diccionario: {my_list}")

#Para obtener una lista con los valores:
my_list = list(my_dict.values())
print(f"Lista de valores del diccionario: {my_list}")