'''
Concepto tupla:
    Conjunto de valores no repetidos, a diferencia de las listas son inmutables.
    Permiten un acceso más rapido a memoria, evitando sobrecargas en ciertos casos
    Es una colección de elementos ordenados
    Las tuplas no admiten reasignación de elementos por índice. Es un conjunto de valores
    "cerrado"
    No se recomienda cambiar de tupla a lista o de lista a tupla, casos muy específicos donde
    necesitemos manipular valores (Las listas son mutables)
'''
# Definición de la tupla
my_tuple = tuple()
my_tuple2 = ()

#Asignación
my_tuple = ("David",34,2.04)

print(my_tuple)
print(type(my_tuple))

#Acceso a elemento
print(my_tuple[0])  #Elemento 1, posición 0
print(my_tuple[-1]) #Elemento -1, posición última (posición 1 desde el final)
#my_tuple[3] = "David"  ¡Es inmutable! No se pueden insertar elementos por índice

#Métodos
to_search = "test"      #Si el índice no existe, lanza el error "x not in tuple"
to_search = 34
print(f"El valor {to_search} está en el índice {my_tuple.index(to_search)}")    #Índice donde se encuenta el string "David"
print(f"Aparece {to_search} {my_tuple.count(to_search)} veces")    #¿Y cuantas veces aparece?

#Unir tuplas
my_tuple2 = ("Noelia",32,1.65)
my_new_tuple = my_tuple + my_tuple2
print(my_new_tuple)

#"Slice"
my_short_tuple = my_tuple2[0:2]
print(my_short_tuple)

#Tupla a lista
my_list_from_tuple = list(my_tuple2)
print(type(my_list_from_tuple))     #Tipo lista
print(my_list_from_tuple)           # ['1','2',....] => lista
my_list_from_tuple.append("test")
print(my_list_from_tuple)           #Recordar que ahora es una lista! Podemos trabajarla como tal

#Revertimos tupla a lista
my_new_tuple2 = tuple(my_list_from_tuple)
print(my_new_tuple2)                #Previamente, trabajando como lista hemos podido insertar un elemento

#Eliminar variable (No es un clear, elimina la variable)
#del my_new_tuple2[0]   No podemos eliminar un elemento! 'tuple' object doesn't support item deletion
del my_new_tuple2
#Ahora no existe la variable de tipo tupla, no solo la vacía
#print(my_new_tuple2)        name 'my_new_tuple2' is not defined.