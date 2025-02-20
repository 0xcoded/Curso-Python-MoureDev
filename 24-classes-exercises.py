# 1. Crea una clase llamada "Animal" que tenga una propiedad 
# "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
class Animal:
    def __init__(self,species):
        self.species = species
        
    def make_sound(self):
        if self.species == "perro":
            print("Los perros ladran")
        else:
            print("Si no es un perro, emite otro sonido")

perro = Animal("perro")
perro.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al 
# crear un objeto y almacÃ©nala en una propiedad pÃºblica. 
# AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo 
# de la especie.

#OK!

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas 
# "brand" y "model". AdemÃ¡s, debe tener una propiedad privada 
# "_speed" que inicialmente serÃ¡ 0.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.__speed = 0
    
    def accelerate(self):
        if self.__speed > 0:
            self.__speed += 10
        else:
            self.__speed = 0

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate"
# que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un 
# mÃ©todo "brake" que reduzca la velocidad en 10 unidades.
# AsegÃºrate de que la velocidad no sea negativa.

#OK

# 5. Crea una clase "Book" que tenga propiedades como "title" 
# (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener 
# el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__(self,title,author):
        self.title = title
        self.__author = author
    
    def getauthor(self):
        return self.__author
    
    def setauthor(self,author):
        self.__author = author


# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre,
# apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver 
# la nota media del estudiante.
class Estudiante:
    def __init__(self,nombre,apellido,notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas
        
    def notamedia(self):
        media = 0
        for i in range(0,len(self.notas)):
            media += int(self.notas[i])
        media = media / len(self.notas)
        print(f"Nota media: {int(media)}")

david = Estudiante("David","Valls",[10,9,10,3])
david.notamedia()

# 7. Crea una clase "BankAccount" con propiedades como "owner"
# y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero,
# asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAcccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def depositar(self,cantidad):
        self.balance += int(cantidad)
        print(f"Depositados {cantidad}. Tienes {self.balance}")
    
    def retirar(self,cantidad):
        if cantidad > self.balance:
            print(f"No dispone de suficiente dinero, no puedes retirar {cantidad}. Tienes {self.balance}")
        else:
            self.balance -= int(cantidad)
            print(f"Retirados {self.balance}")

bankaccount1 = BankAcccount("David",300)
bankaccount1.depositar(100)
bankaccount1.retirar(500)   #No hay 500, marca aviso y no hace nada
bankaccount1.retirar(100)   #Esta cantidad si es posible

# 8. Crea una clase "Point" que represente un punto en el 
# espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que 
# calcule la distancia entre dos puntos.
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self):
        print(f"{abs(int(self.x - self.y))}")

point = Point(200,500)
point.distance()

# 9. Crea una clase "Employee" que tenga propiedades
# como "name", "hourly_wage" (pago por hora) y "hours_worked".
# AÃ±ade un mÃ©todo que calcule el pago total basado en las
# horas trabajadas y el salario por hora.
class Employee:
    def __init__(self,name,hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def payment(self):
        print(f"A {self.name} le corresponden {self.hourly_wage * self.hours_worked}$")

david = Employee("David",11,8)
david.payment()

# 10. Crea una clase "Store" que tenga una propiedad
# "inventory" (una lista de productos). AÃ±ade un mÃ©todo
# para agregar un producto al inventario y 
# otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self,inventory:list):
        self.inventory = inventory
    
    def add_product(self,product):
        self.inventory.append(product)
    
    def show_products(self):
        for i in range(0,len(self.inventory)):
            print(f"Producto {i}: {self.inventory[i]}")

my_store = Store(["manzanas","serpientes"])
my_store.add_product("teclados")
my_store.show_products()