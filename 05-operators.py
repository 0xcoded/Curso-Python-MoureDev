print(10 + 2)   #También utilizado para concatenar strings, asegurarse del tipo que tiene asignado para saber cómo va a operar y qué
print(10 - 2)
print(10 * 2)   #También sirve para multiplicar un string! Ver abajo
print(10 / 3)
print(10 % 2)   #Resto, (módulo)
print(10 // 3)  #División aproximada, entero
print(2 ** 3)

#print("Hola" + 5)   #No se puede concatenar un string a un integer!!
print("Forma correcta de concatenar este string a",5,"que es un entero y esto otro string")     #Alternativa correcta a la línea anterior
print("Valido si transformamos " + str(5) + " a string: " + str(type(str(5))))
print("Hola Multiplicado 3 veces " * 3) #Sólo valido un Integer, de lo contario no tendría sentido

my_float_mult = (2.5*2)
print(type(my_float_mult))
print(str(my_float_mult))
#print("Hola " * int(my_float_mult))
#print("Multiplicado",int(my_float_mult),"veces")
my_int_mult = int(my_float_mult)
print("Hola "*my_int_mult)
print("Multiplicado \"Hola\"",my_int_mult,"veces")


# Operadores Comparativos

'''
Devuelve un booleano
Puede asignarse a una variable booleana'''
print(3==4)
print(4 > 3)
print(4 < 3)
print(4 >= 4)
print(4 <= 3)
print(4 != 3)

my_bool_result = 4!=3
print(type(my_bool_result))
print("El resultado de 4!=4 es:",my_bool_result)

#Podemos comparar strings igualmente, pero por ordenación alfabética, también ordena por mayúscula o minúscula
print("Hola">"david")
print("Hola"<"david")
print("Hola">="david")
print("Hola"<="david")
print("Hola"=="david")
print("Hola"!="david")

#Para comparar por longitud, hay que utilizar la función de python len()
print(len("david")>len("hola"))
print(len("david")<len("hola"))


# Operadores lógicos
        #AND & NOT
print(3==3 and 4!=4)        #La segunda condición no se cumple, False
print(3==3 or 4!=4)         #La segunda condición no se cumple pero la primera si, True

'''Los operadores pueden utilizar los paréntesis
como se de una operación matemática se tratase'''

print(4==3 or ("david"=="david" and 4==4))  
'''4==3 or (true)
false or true -> True'''

print(4==3 or ("david"=="David" and 4==4))  
'''4==3 or (false)
false or false -> False'''

print(4==4 and ("david"=="David" and 4==4))  #true and false => False
        
        #NOT (Negación, True->False, False->True)
print(4==4 and not("david"=="David" and 4==4))  #true and !false(True) => True