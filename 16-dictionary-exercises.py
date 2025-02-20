# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
my_dict = dict({"name":"David","age":34,"country":"Valencia"})
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.
print(my_dict["name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
my_dict["job"] = "Programador"
print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
my_dict["age"] = 38
print(my_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dict["country"]
print(my_dict)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
my_dict2 = {}
for x in range(1,6):
    my_dict2[x] = x**2
print(my_dict2)

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
my_dict3 = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in my_dict3)

# 8. Imprime solo las claves del diccionario.
print(my_dict3.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
my_list = list(my_dict3.keys())
print(my_list)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
my_dict4 = {}
keys = ["name", "age", "job"]
my_new_dict = my_dict4.fromkeys(keys,"Desconocido")
print(my_new_dict)