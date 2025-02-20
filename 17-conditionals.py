user,password = input("Ingrese usuario: "),input("Ingrese la clave: ")

#Recordar: Input devuelve un string!

if user == "david" and password == str(1234) :
    print("Login correcto!")
elif user == "tester" and password == "tester":
    print("Tester login!")
else:
    print("Error al iniciar sesión")
  
#Condicionales con cadenas  
my_string = input("Ingrese una cadena, puede estar vacía: ")
if not my_string:                   #Con not invertimos la condición, ahora valida False
    print("La cadena es verdadera") #Una cadena vacia es interpretada como False
else:
    print(my_string)