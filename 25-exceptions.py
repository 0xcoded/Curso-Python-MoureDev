def restar(a,b):
    try:
        result =  a - b
    except:
        print("¡Ha ocurrido una excepción!")
    else:
        print("No ha ocurrido ninguna excepción")
        return result
    finally:
        print("Fin del control de errores")
        
print(restar(9,8))

#Captura de errores por tipo de error (Capturar errores muy concretos)
#print("j"-4)   =>  TypeError
try:
    result = "a"-4
except TypeError:
    print("Error de tipado! TypeError")
except ValueError:
    print("Error de valor! ValueError")
else:
    print(f"Tipado correcto! {result}")
finally:
    print("Fin de la comprobación")

#Capturar la excepción
try:
    result = "a"-4
except TypeError as error:
    print(f"Error de tipo! {error}")
except Exception as error:
    print(f"Excepción desconocida! {error}")
else:
    print(f"Tipado correcto! {result}")
finally:
    print("Fin de la comprobación")