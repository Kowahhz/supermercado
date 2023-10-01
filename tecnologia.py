class Tecnologia:
    def __init__(self, marca, voltaje, precio, eficiencia):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia

    def calcularDescuento(self):
        descuento_eficiencia = 0.0  

        
        if self.__eficiencia in ['A', 'B']:
            descuento_eficiencia = 0.5
        elif self.__eficiencia in ['C', 'D']:
            descuento_eficiencia = 0.3
        elif self.__eficiencia in ['E', 'F']:
            descuento_eficiencia = 0.1

        return descuento_eficiencia

    def getMarca(self):
        return self.__marca

    def getVoltaje(self):
        return self.__voltaje

    def getPrecio(self):
        return self.__precio

    def getEficiencia(self):
        return self.__eficiencia

    def setMarca(self, nuevaMarca):
        self.__marca = nuevaMarca

    def setVoltaje(self, nuevoVoltaje):
        self.__voltaje = nuevoVoltaje

    def setPrecio(self, nuevoPrecio):
        self.__precio = nuevoPrecio

    def setEficiencia(self, nuevaEficiencia):
        self.__eficiencia = nuevaEficiencia