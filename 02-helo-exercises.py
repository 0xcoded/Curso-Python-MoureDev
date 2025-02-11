# 1. Imprime "Â¡Hola Mundo!" por consola.
print("¡Hola Mundo!")

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.

#Este código trata de crear un Hola Mundo, en este fichero estamos con los ejercicios

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.

print("David, 34 años")

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.
print(type("Hola Mundo"))
print(type(11))
print(type(9.23))
# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.
'''
    Los tipos de datos hacen referencia a con qué tipo de valor vas a trabajar, el tipo del dato
    que se va a
    manejar, aunque en Python no es necesario declararlo,
    en ocasiones es necesario
'''
print("Fin del comentario en múltiples lineas")
# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print('Hola ' + 'Mundo')
# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.
name = "David"
age = 34
print(name + " tiene " + str(age) + " años")
# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
userName = input("Introduce tu nombre: ")
print("Hola, " + userName)
# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.
num1 = 10
num2 = 20
result = num1 + num2
print(result)
print("El dato es de tipo \"" + str(type(result)) + "\"")
# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.
#Asignamos valores a las variables
num1 = 10
num2 = 20
#usamos el operador + para realizar la suma y almacenarlo en la variable "result"
#+ suma
#- resta
#* multiplicación
#/ división
#% resto
#** exponente
result = num1 + num2
#imprimimos el resultado de la suma
print(result)
#con \ podemos escribir una comilla doble sin que el prorama falle, es un caracter de "escape" "\"" => "
print("El dato es de tipo \"" + str(type(result)) + "\"")