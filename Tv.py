from tecnologia import Tecnologia  
class Tv(Tecnologia):
    def __init__(self, marca, voltaje, precio, eficiencia, tamano):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__tamano = tamano

    def getTamano(self):
        return self.__tamano

    def setTamano(self, nuevoTamano):
        self.__tamano = nuevoTamano