from tecnologia import Tecnologia
from transporte import Transporte
class Scooter(Tecnologia, Transporte):
    COSTODESPACHOBASE = 4000

    def __init__(self, marca, voltaje, precio, eficiencia, aro, velocidad, peso):
        
        Tecnologia.__init__(self, marca, voltaje, precio, eficiencia)
        Transporte.__init__(self, peso, marca)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

    def calcularDespacho(self):
        costo_por_kilogramo = 300
        
        costo_despacho_total = self.COSTODESPACHOBASE + (self.getPeso() * costo_por_kilogramo)
        return costo_despacho_total

    def getMarcaTecnologia(self):
        return self.getMarca()

    def getAro(self):
        return self.__aro
    
    def getPeso(self):
        return self.__peso

    def getVelocidad(self):
        return self.__velocidad

    def setAro(self, nuevoAro):
        self.__aro = nuevoAro

    def setVelocidad(self, nuevaVelocidad):
        self.__velocidad = nuevaVelocidad

    def __str__(self):
        return f"Scooter de marca {self.getMarcaTecnologia()}, aro {self.getAro()}, velocidad {self.getVelocidad()} km/h, peso {self.getPeso()} kg"
