from tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, nombreConsola, version, marca, voltaje, precio, eficiencia):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def calcularDescuento(self):
        descuento_eficiencia = super().calcularDescuento()  
        if self.__version.lower() == "lite":
            descuento_eficiencia += 0.05
        return descuento_eficiencia

    def imprimirCaracteristicas(self):
        super().imprimirCaracteristicas()  
        print(f"Nombre de la Consola: {self.__nombreConsola}")
        print(f"Versión: {self.__version}")

    def getNombreConsola(self):
        return self.__nombreConsola

    def getVersion(self):
        return self.__version

    def setNombreConsola(self, nuevoNombreConsola):
        self.__nombreConsola = nuevoNombreConsola

    def setVersion(self, nuevaVersion):
        self.__version = nuevaVersion