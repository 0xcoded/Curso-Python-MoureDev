def sum(a: int,b):
    return a+b

print(sum(10,13))
print(sum("a","b"))

def hello(name="Default name",surname="Default surname"):
    return f"Hola {name} {surname}"

print(hello(surname="valls",name="David"))  #Podemos asignar un valor sin seguir órden de argumentos
print(hello())

#lista de argumentos, por ejemplo pasar todo a mayusculas (u otro elemento iterable)
#Similar a punteros en python
def upper_texts(*texts:str):
    for text in texts:
        print(text.upper())
        
upper_texts("hola","DaVid","VALEncIA")
    