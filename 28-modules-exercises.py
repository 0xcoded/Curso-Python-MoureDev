# 1. Crea un mÃ³dulo llamado "calculator" que contenga
# funciones para sumar, restar, multiplicar y dividir dos nÃºmeros.
# Importa este mÃ³dulo en otro archivo y usa sus funciones.
from calculator import add,substract,multiply,divide
print(add(1,2))
print(substract(3,1))
print(multiply(4,2))
print(divide(9,3))

# 2. Crea un mÃ³dulo llamado "converter" que tenga funciones 
# para convertir temperaturas entre Celsius y Fahrenheit. 
# Escribe un programa que importe este mÃ³dulo y realice conversiones.
import converter
print(converter.celsius_to_fahrenheit(30))
print(converter.fahrenheit_to_celsius(80))

# 3. Crea un mÃ³dulo que contenga una lista de nombres 
# de estudiantes y una funciÃ³n que imprima todos los nombres.
# Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para 
# mostrar la lista.
from alumn import get_alumns
get_alumns(["David","Noelia","Brais"])

# 4. Crea un mÃ³dulo llamado "geometry" que tenga una funciÃ³n 
# para calcular el Ã¡rea de un cÃ­rculo y un cuadrado. Usa este 
# mÃ³dulo en otro archivo para calcular Ã¡reas.
from geometry import area_circle,area_square
print(area_circle(30))
print(area_square(30))
# 5. Escribe un mÃ³dulo que contenga una funciÃ³n que acepte 
# cualquier nÃºmero de argumentos y devuelva su suma. Importa 
# y usa la funciÃ³n en otro archivo.
from sums import sum_all
print(sum_all(3,2,54,5,3))

# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con 
# propiedades como marca, modelo y aÃ±o. Importa este mÃ³dulo 
# en otro archivo y crea una instancia de la clase "Car".
import classes
my_car = classes.Car("Peugeot","306",1923)

# 7. Escribe un mÃ³dulo que contenga funciones para leer y 
# escribir en archivos de texto. Crea un programa que use estas 
# funciones para escribir y leer datos.
from files import read_file,write_file
write_file("c:\\test.txt","Hola Mundo Python!")
read_file("c:\\test.txt")

# 8. Crea un mÃ³dulo llamado "statistics" que tenga funciones
# para calcular la media y la mediana de una lista de nÃºmeros.
# Usa este mÃ³dulo para calcular estos valores en una lista dada.
import stadistics
print(stadistics.mean([12,32,11,20,4]))
print(stadistics.median([10,9,10,8]))

# 9. Crea un mÃ³dulo que contenga una funciÃ³n para contar
# cuÃ¡ntas veces aparece una palabra en un texto. Escribe un 
# programa que importe el mÃ³dulo y lo use para contar palabras 
# en una cadena.
from words import count_word
print(count_word("Esto es un texto en un texto de un texto en un texto con un texto x 2","texto"))

# 10 Crea un mÃ³dulo llamado "dates" que contenga funciones 
# para obtener la fecha actual y calcular la diferencia entre dos fechas.
# Usa este mÃ³dulo en un programa para mostrar
# la fecha actual y la diferencia entre dos fechas especÃ­ficas.
from timediff import get_current_date,date_difference
print(get_current_date())
print(date_difference("30-01-1991", "20-02-2025"))