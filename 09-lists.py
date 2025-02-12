# Listas
'''
Las listas son "arrays", una estructura de datos (pilas y colas de datos)
'''

my_list = list()        # Puede usarse para vaciar una lista, se recomienda clear()
another_list = []

my_test_string = "valls"
my_list = ["david",my_test_string,34,2.04] #Independiente el tipo de dato, se agrega a la lista. Pueden ser variables

print(f"La lista contiene {my_list} y tiene una longitud de {len(my_list)} elementos.")         #¿Cuantos elementos tiene la lista? (Longitud de la lista) (3)

my_list = list()            # Vaciamos la lista, diciendo que es una nueva lista
print(f"La lista contiene {my_list} y tiene una longitud de {len(my_list)} elementos.")         #¿Cuantos elementos tiene la lista? (Longitud de la lista) (3)

print(type(my_list))
print(type(another_list))

my_list = ["david",my_test_string,34,2.04]
print(f"{my_list[0]} {my_list[1]} mide {my_list[3]} metros y tiene {my_list[2]} años")
# print(my_list[9]) => IndexError  !!

# Acceso invertido (índice negativo)
print(my_list[-2])  #Accede a la posición -2, la segunda desde el final, y lo imprime (A diferencia de otros lenguajes)
print(f"{my_list[-4]} {my_list[-3]} mide {my_list[-1]} metros y tiene {my_list[-2]} años")

#¿Cuantas veces aparece?
print(my_list.count(34))

#Desestructuración
name,surname,age,height = my_list   #Orden específico, longitud necesaria
print(name,surname,age,height)

        #NO RECOMENDADO => age,surname,height,name = my_list[2], my_list[1], my_list[3], my_list[0] #Orden no específico, sólo se asigna el elemento elegido
        #print(name,surname,age,height)
        
#Concatenar listas
my_list2 = [10,1.5,"test"]
my_concat_list = my_list + my_list2
print(f"Lista concatenada: {my_concat_list}")

''' ¡Python utiliza tipado dinámico!
my_list = "Hola Mundo!"
print(f"my_list ahora es del tipo:\n\t{type(my_list)}")'''

# Insertar elemento en la lista
my_list.insert(4,"Posicion 4")
print(f"En la posición 4 esta el contenido: {my_list[4]}")
print(my_list)
my_list.insert(0,"Noelia")      # Podemos alterar el valor insertando un nuevo contenido en la posición indicada, desplazando los valores
my_list.insert(3,32)
my_list.insert(4,"1.65")
print(f"{my_list[0]} {my_list[2]} mide {my_list[4]} metros y tiene {my_list[3]} años")  #Se han desplazado los valores, "David" sigue existiendo en la lista
print(my_list)
print(f"En la posición 4 esta el contenido: {my_list[4]}")  #Recordar, se desplaza si existe el índice, no se sustituye

# Eliminar un elemento (el primero hallado en la lista)
my_list.remove("david")     # Sólo elimina la primera coincidencia
print(my_list)

# Eliminar último elemento (pop())
print(f"Se ha eliminado el valor \"{my_list.pop()}\"")
print(my_list)
        #Podemos indicar el índice a desapilar
        #Se recomienda el uso de del
#print(f"Se ha eliminado el índice 2 con el valor \"{my_list.pop(2)}\"")

#del (delete), alternativa a pop()
#del elimina por índice, remove por valor
del my_list[-1]     #Eliminamos el último elemento
print(f"Se ha eliminado el último elemento (-1). El uso de \"del\" no puede almacenar el valor en variable")
print(my_list)

my_list.clear()
print(my_list)      #Lista vaciada

my_list = ["david",my_test_string,34,2.04]
my_list[0] = "Noelia"   #En lugar de insertar desplazando, podemos reasignar su valor sin desplazar, eliminando el previo valor en ese índice
print(my_list)

#Copiar listas
my_new_list_copy = my_list.copy()
my_list.clear()
print(my_new_list_copy)
print(my_list)
print(type(my_new_list_copy))

#Invetir lista
my_reversed_list = my_new_list_copy.copy()  #No necesario, pero si para reasignar la lista revertida a una nueva variable
'''
¡¡ERROR!! =>
my_reversed_list = my_new_list_copy.reverse()
'''
my_reversed_list.reverse()
print(my_reversed_list)

#Ordenar lista
my_new_list = ["z","david","cadena"]
my_new_list.sort()          #Puede ordenar números caracteres o strings, siempre y cuando no varia el tipo de dato
print(my_new_list)

#Capturar trozo de lista
print(my_new_list[0:1])