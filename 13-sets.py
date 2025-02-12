# Declaración y tipado
my_set = set()      #Declaración de set
my_another_set = {} #¡Cuidado! Aunque se usan las llaves, lo toma como diccionario
print(type(my_set))
print(type(my_another_set))     # => Dict

my_another_set = {"david","valls",34,2.04}  #Para usar las llaves debemos definir qué contiene para no tomarlo por diccionario

print(type(my_another_set))     # => Set
print(my_another_set)

'''
Los set's no son estructuras ordenadas. Por ello
no podemos acceder a un elemento por índice, 
ya que utiliza un hash de manera interna, creando
una estructura desordenada.

Copilot:
Elementos Únicos: 
    - Los sets no permiten duplicados. Cada elemento en un set debe ser único, 
    lo que es útil para eliminar duplicados de una lista.
Operaciones de Conjunto: 
    - Puedes realizar operaciones matemáticas de conjuntos como unión, intersección, diferencia 
    y diferencia simétrica.
Rapidez en Búsquedas: 
    - Debido a su estructura basada en hash, las operaciones de búsqueda en sets son muy rápidas.
Operaciones de Comparación: 
    - Los sets permiten comparar y evaluar relaciones entre diferentes conjuntos de datos.
'''
my_another_set.add("test")      #No se agrega al final como se esperaría en otra estructura como listas o tuplas
print(my_another_set)
my_another_set.add("test")      #No admite duplicados, no se agrega pues ya existe
print(my_another_set)

#Comprobar existencia de un valor en un set
print("test" in my_another_set)     # => True
print("noelia" in my_another_set)   # => False

#Eliminar valor en un set
my_another_set.remove("test")
print(my_another_set)

#Vaciar set

'''my_another_set.clear()
print(len(my_another_set))'''

#Nos cargamos el set
del my_another_set
#print(my_another_set) => Not defined

#Conversión ¡¡PELIGRO!! La lista va a cambiar en cada ejecución debido al hash utilizador por el set
my_set = {"David",34,2.04}
#my_list = list(my_set)

#Concatenar sets
my_another_set = {"Noelia",32,1.65}
my_full_set = my_set.union(my_another_set)
print(my_full_set)

#Diferentes entradas entre un set y otro
print(my_set.difference(my_another_set))        #A my_set le hemos quitado el contenido de my_another_set e imprimimos

