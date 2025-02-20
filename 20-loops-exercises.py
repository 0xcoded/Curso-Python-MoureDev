# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
num = 1
while num <= 10:
    print(num)
    num+=1
# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
my_list = [10, 20, 30, 40, 50]
for number in my_list:
    print(number)
# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
counter = 1
result = 0
while counter <=100:
    counter+=1
    result += counter
else:
    print(result)
# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
my_string = "Python"
for x in range(0,len(my_string)):
    print(my_string[x])
# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
counter = 1
while counter <= 50:
    counter+=1
    if(counter % 7 == 0):
        print(f"El primer número divisible por 7 es {counter}")
        break
else:
    print("No se a hallado!")
# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
for key in my_dict:
    print(key)
# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
counter = 1
while counter <= 20:
    if counter % 2 == 0:
        print(counter)
    counter += 1
# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.
for x in range (10,0,-1):
    print(x)
# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].
my_list = [30, 10, 30, 20, 30, 40]
counter = 0
for number in my_list:
    if number == 30:
        counter += 1
else:
    print(counter)
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
name_list = ["david","alberto","brais","paco"]
for name in name_list:
    if name == "brais":
        break
    print(name)