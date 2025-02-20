# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre 
# como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, 
# debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name="Desconocido"):
    print(f"Hola {name}")
personalized_greeting()

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos 
# y retorne el resultado de multiplicarlos.
def multiply(a,b):
    return a*b

print(multiply(2,10))

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento 
# y retorne True si es par y False si es impar.
def is_even(number:int):
    if number%2==0:
        return True
    else:
        return False
print(is_even(19))
# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de 
# texto y la retorne en mayÃºsculas.
def convert_to_uppercase(*texts:str):
    my_list = list()
    for text in texts:
        my_list.append(text.upper())
    return my_list

name_list = ["David","alberto","brais","jorge"]
print(convert_to_uppercase(*name_list))
# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario 
# de nÃºmeros como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers:int):
    result = 0
    for num in numbers:
        result += num
    return result

num_list = [1,23,1,33,2]
print(arbitrary_sum(*num_list))

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos:
# nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>".
# Los argumentos deben ser pasados por clave.
def generate_full_greeting(name,surname):
    return f"Hola, {name} {surname}"

print(generate_full_greeting("David","valls"))

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: 
# base y exponente, y retorne el resultado de elevar la base al exponente.
def power(a,b):
    return a**b

print(power(2,8))

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros 
# y retorne su promedio.
def calculate_average(a,b,c):
    return (a+b+c)/3
print(calculate_average(10,10,7))

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto 
# y retorne el nÃºmero de caracteres que contiene.
def count_characters(text:str):
    return len(text)

print(count_characters("David valls"))

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero 
# indefinido de cadenas y las imprima en mayÃºsculas, una por una, 
# tal como se hizo en el archivo proporcionado.
def display_messages(*texts:str):
    for text in texts:
        print(text.upper())
        
display_messages("hola","david","moureDev")