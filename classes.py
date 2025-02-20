# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con 
# propiedades como marca, modelo y aÃ±o. Importa este mÃ³dulo 
# en otro archivo y crea una instancia de la clase "Car".

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year