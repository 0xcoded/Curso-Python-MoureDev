# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un nÃºmero entero que represente tu edad.
# â€¢	height: un nÃºmero flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.
name = "David Valls Da Costa"
age = 37
height = 2.04
print(name)
print(age)
print(height)
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
age = str(age)
print('Tienes',age,"años")
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
is_studen = True
print(is_studen)
# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
len_name = len(name)
print(len_name)
# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name,age,city = "David",37,"Valencia"
print(name,"es de",city,"y tiene",age,"años")
# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
favorite_color = input("Color favorito: ")
print(favorite_color)
# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Manzaña"
print(fruit)
fruit = True
print(fruit)
# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price = 8.90
price = int(price)
print("El precio es",price)
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address = "Calle inventada, 29, 18 b, Berlin, Rusia"
print(address)
address_len = len(address)
print(address_len)
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone: int = 654321012
print(type(phone))
phone = "¡NO ENTERO!"       #Da igual que lo asignes como un tipo, python puede cambiar el tipo
print(type(phone))