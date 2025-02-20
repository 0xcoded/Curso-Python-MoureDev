#Definición
class Person:
    def __init__(self,name,age,alias="\"Undefined alias\""):
        self.name = name  
        self.age = age
        self.__alias = alias    #__ define la variable como privada, no se puede editar desde fuera
        self.hellotext = f"Hola {self.name}, tienes {self.age} años."
    
    def hello(self):
        #hellotext está definido en el constructor de Person, tenemos acceso estableciendo self (la propia clase)
        
        #print(f"Hola {self.name}, tienes {self.age} años")
        print(self.hellotext)
    
    def walk(self):
        print(f"{self.__alias} está caminando")
        
    # Getters y Setters para propiedades privadas
    def setalias(self,newalias):
        self.__alias = newalias
        
    def getalias(self):
        return self.__alias

print(Person)   #Nos muestra un objeto, que parte del "main" (inicio, __main__.Person)

person1 = Person("David",34)
person2 = Person("Noelia",32,"Noe")  #Creamos dos "Personas", construidas en la clase Person con diferente nombre y edad

person1.hello()
person2.hello()        #Ambas personas saludan, pero cada persona tiene un nombre y edad que no tienen porqué ser iguales
person1.walk()
person2.walk()

#person2.__alias = "MoureDev"      ¡¡Hemos definido alias como privado!!
person2.walk()

person2.setalias("MoreDev")
print(person2.getalias())
person2.walk()