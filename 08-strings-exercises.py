# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(f"La cadena {text} tiene una longitud de {len(text)}.")
# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
concat_string = "Hola" + "Python"
print(concat_string)
# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
my_new_line_text = "Este es un mensaje\nEn varias líneas"
print(my_new_line_text)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = "David", "Valls", 34
print(f"Hola {name} {surname}, tienes {age} años")
# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
unpacked_text = "Python"
a,b,c,d,e,f = unpacked_text
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a,b,c,d,e,f)
# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres 
# desde la posiciÃ³n 3 hasta la 7.
my_string = "Programación"
print(my_string[3:8])       # La posición 7 es el octavo caracter

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
my_reversed_string = my_string[::-1]
print(my_reversed_string)
# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
print(text.upper())
# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
text = "Programación en Python"
print(text.count("n"))

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
my_numeric_var = "12345"
print(f"La cadena {my_numeric_var} es un número: {my_numeric_var.isnumeric()}")