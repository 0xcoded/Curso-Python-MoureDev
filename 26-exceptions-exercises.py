import math
# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros 
# proporcionados por el usuario. Usa try-except para capturar 
# cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
def division(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Has intendado dividir por 0!")
    else:
        print(result)

#a = input("Número 1: ")
#b = input("Número 2: ")
#division(int(a),int(b))

# 2. Crea una funciÃ³n que tome una cadena e intente convertirla 
# en un nÃºmero entero. Usa try-except para capturar cualquier 
# error en la conversiÃ³n.
def str_to_int(text):
    try:
        result = int(text)
    except Exception as error:
        print(error)
    else:
        print(result)

#str_to_int("Python")

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido
# y maneje posibles errores (por ejemplo, archivo no encontrado).
# Usa try-except para gestionar las operaciones de archivos de forma segura.
def read_file(path):
    try:
        file = open(path)
        print(file.readlines())
    except Exception as error:
        print(error)

#read_file("c:\\NoExiste este_Archivo.exe")

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones 
# (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. 
# Usa try-except-else-finally para manejar errores y asegurar 
# que se imprima un mensaje final, independientemente de los errores.
def multiple_operations(a,b):
    try:
        print(a+b)
        print(a-b)
        print(a*b)
        print(a/b)
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print("Todo correcto")
    finally:
        print("Fin de la comprobación de errores")

#multiple_operations(10,20)

# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError
# si la entrada no es un nÃºmero entero positivo.
# Usa el manejo de excepciones para gestionar la entrada y lanzar 
# excepciones personalizadas cuando sea necesario.
def age_ask():
    try:
        age = int(input("Ingresa tu edad: "))
        if age <= 0:
            raise ValueError("La edad no puede ser negativa o cero")
    except ValueError as error:
        print(f"Error: {error}")

#age_ask()
# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista 
# por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© 
# fuera de rango.
def index_five(my_list):
    try:
        result = my_list[5]
    except IndexError as error:
        print(f"Error! {error}")

#index_five([12,32,"david"])

# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples 
# excepciones: ZeroDivisionError, ValueError y TypeError.

def division_two(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print("Error de valor")
    except TypeError:
        print("Error de tipo")

#division_two(12,[34.123,13,"hola"])

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una 
# excepciÃ³n personalizada llamada InsufficientFundsError si el 
# saldo es menor que la cantidad a retirar.
class InsufficientFundsError(Exception):
    pass

def transaction(remove_money):
    try:
        balance = 300
        if balance < remove_money:
            raise InsufficientFundsError("Saldo insuficiente")
    except InsufficientFundsError as error:
        print(error)

# transaction(700)

# 9. Crea una funciÃ³n que intente convertir una lista de cadenas 
# en enteros. Maneja cualquier error que surja cuando una cadena no 
# pueda convertirse.

def list_to_int(text):
    my_list = list()
    try:
        for element in text:
            my_list.append(int(element))
    except ValueError:
        print(f"{element} no se puede transformar en texto")

list_to_int([12.3,"david",34])

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. 
# Lanza un ValueError si el nÃºmero es negativo.
def square(num):
    try:
        if num <= 0:
            raise ValueError("Error al obtener la raíz cuadrada. Valor negativo o cero")
        result = math.sqrt(num)
    except ValueError as error:
        print(error)
    else:
        return result

print(square(-12))