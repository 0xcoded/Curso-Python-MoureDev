#While (condiciónes o bucle infinito (while True:))
my_int = 0

while my_int < 50:   #Comprobamos que se inferior a 50
    if my_int == 15: #Comprobamos que valga 15
        print("Fin de la ejecución, se ha detectado el valor 15")
        break       #Rompemos el bucle y salimos
    print(my_int)   #Si no se rompe, muestra el número
    my_int += 1     #De lo contrario siempre vale 0 y esto sería infinito!

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 3
else:                       #Cuando no se cumple la condición del while...
    print("Se ha finalizado el bucle")
    
#For (iterar elementos)
my_list = [1,2,3,4]
my_tuple = (5,6,7,8)
my_set = {1,2,3,4,5,6,7,8}
my_dict = {"name":"david","age":34,"country":"Valencia"}

for element in my_list:
    print(element)
for element in my_tuple:
    print(element)
for element in my_set:
    print(element)
for element in my_dict:
    if element == "country":    #¿El elemento de la lista vale "country"?
        break                   #Detenemos al detectar "country" en el diccionario
        #continue                #Continuar (Volviendo el for de nuevo, nunca mostraría "contry")
    print(element)              #Después de la condición, mientras no se rompa por el break
else:
    print("El FOR ha finalizado sin detenerse") #¡¡Break rompe el for, incluyendo el else!!