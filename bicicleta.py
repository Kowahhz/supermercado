class Bicicleta:
    def __init__(self, aro, peso, precio, marca):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def calcularDespacho(self):
        costo_despacho_base = 4000  
        costo_por_kilogramo = 400  

        costo_despacho_total = costo_despacho_base + (self.__peso * costo_por_kilogramo)
        return costo_despacho_total

    def getAro(self):
        return self.__aro

    def getPeso(self):
        return self.__peso

    def getPrecio(self):
        return self.__precio

    def getMarca(self):
        return self.__marca
    
    def setAro(self, nuevoAro):
        self.__aro = nuevoAro

    def setPeso(self, nuevoPeso):
        self.__peso = nuevoPeso

    def setPrecio(self, nuevoPrecio):
        self.__precio = nuevoPrecio

    def setMarca(self, nuevaMarca):
        self.__marca = nuevaMarca