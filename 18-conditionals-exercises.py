# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
my_int = -10
if my_int > 0:
    print("Positivo")
elif my_int == 0:
    print("Cero")
else:
    print("Negativo")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
my_string = ""
if(my_string):
    print(my_string)
else:
    print("Cadena vacía")
# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
num1, num2 = int(input("Núnero 1: ")),int(input("Núnero 2: "))
if num1>num2:
    print(f"{num1} es mayor")
elif num1==num2:
    print("Son el mismo numero")
else:
    print(f"{num2} es mayor")
# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
my_int = 15
if my_int % 3 == 0 and my_int % 5 == 0:
    print("Divisible por 5 y 3")
else:
    print("No divisible")
# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
my_int = int(input("Ingrese un número: "))
if my_int % 2 == 0:
    print("Par")
else:
    print("Impar")
# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
age = 17
if age >= 18:
    print("Puede votar")
elif age >= 16 and age <= 17:
    print("Puede votar con permiso especial")
else:
    print("No puede votar")
# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
user,password = input("Ingrese usuario: "),input("Ingrese la clave: ")

if user == "david" and password == str(1234) :
    print("Login correcto!")
elif user == "tester" and password == "tester":
    print("Tester login!")
else:
    print("Error al iniciar sesión")
    
# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
my_int = 15
if my_int >=10 and my_int <= 20:
    print("Mayor o igual a 10 y menor o igual a 20")
else:
    print("Menor que 10 o mayor que 20")
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
traffic_light = input("Color de semáforo: ")
if traffic_light == "verde" or traffic_light == "ambar":
    print("Puedes pasar")
elif traffic_light == "rojo":
    print("Pisa el freno, macareno")
else:
    print("Color inválido")