# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20
print(15+25)
print(50 - 22)
print(8 * 7)
print(100 / 20)
# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.
remainder_int = 37//5
remainder_float = 37/5
print("Integer result:",remainder_int)
print("Float decimal result:",remainder_float)
# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.
number = str(7)
print(number,"es mi número favorito")

# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.
print("Python " * 10)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
result = a>b
print("El resultado de la operación",a,">",b,"es",result)
# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.
print("apple">"banana") #Alfabéticamente banana está después de apple, retorna falso
print("apple"<"banana") #Comparamos si está después, retorna verdadero, ver comentario anterior

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5
# y menor que 20. Imprime el resultado.
print(10>5 and 10<20)   #True, 10 es mayor a 5 y menor que 20, se cumple la condición

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.
print(7<3 or 7>5)   #True, se cumple la segunda al menos
# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
print(not(15>20))   #False, pero al realizar la negación obtenemos True
# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: 
# Verifica si el nÃºmero resultante de la expresiÃ³n 
# (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
print(((5*3) + 2) > 10 and ((5*3) + 2) < 20)    
'''17>10, True
17<20, True
True and True => True
'''

print(10%3 + 4 ** 2)