my_string ="Este es un string\nEn dos líneas"
print(my_string)

my_tab_string = "\tEste es un mensaje \n\ttabulado"
print(my_tab_string)

#Formateo de cadenas
'''
%s => string
%d => integer
%f => float
'''
        #Se recomienda formatear antes que concatenar, a Python le cuesta más y puede resultar confuso y tedioso
name, surname, age = "david","valls",34
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))    #format => {}, cuando no especificamos el tipo
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))         #Tipado => %, asignar tipo de la variable que va a tomar

my_full_string = "Mi nombre es %s %s y mi edad es %d" %(name,surname,age)
print(my_full_string)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")              #Formateo más simple y mejor opción

# Desempaquetado de caracteres
name = "David"
a,b,c,d,e = name    #Cada variable (a-e) toma un caracter,
                    #no es habitual y puede ocasionar problemas si se modifica la variable
print(a,b,c,d,e)

# Divisón de cadena
my_short_name = name[0:4]       # => "David" - "Davi" (Inicia en posición 0, 4 caracteres)
my_short_name2 = name[2:]       # De la posición (char) 2 hasta el final de la cadena
my_last_chars = name[-3]        # 3er último caracter "David" => ( "v" )
print(my_short_name)
print(my_short_name2)           # => vid ( [2:len(var)] )
print(my_last_chars)

# Revertir cadena
reversed_name = name[::-1]      # Revertir cadena, toma toda la cadena y la revierte (salto -1, órden inverso)
print(reversed_name)

# Funciones de cadena
print(name.capitalize())        #Primera letra en mayúscula
print(name.upper())             #Mayúsculas
print(name.count("v"))          #Contar apariciones de un caracter en la cadena
print(name.isnumeric())         #¿Es un número?
print(name.lower())             #Minúsculas
print(name.isupper())           #¿Está en mayúsculas? (No, no toda la cadena)
print(name.upper().isupper())   #Está en mayúsculas porque previamente la hemos transformado a ello (True)
my_test_number = "38"
print(f"El {my_test_number} es un número: {my_test_number.isnumeric()}")  #Recordar pasar a string, los números no tienen los mismo métodos

        # Case sensitive! (print("Da"=="da") => False)
print(f"El nombre {name} empieza con \"Da\": {name.startswith("Da")}")  #True
print(f"El nombre {name} empieza con \"da\": {name.startswith("da")}")  #False