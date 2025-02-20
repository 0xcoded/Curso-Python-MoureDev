# 7. Escribe un mÃ³dulo que contenga funciones para leer y 
# escribir en archivos de texto. Crea un programa que use estas 
# funciones para escribir y leer datos.

def read_file(path):
    file = open(path,"r")
    print(file.readlines())
    
def write_file(path,text):
    file = open(path,"w")
    file.write(text)