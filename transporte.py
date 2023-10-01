class Transporte:
    COSTODESPACHOBASE = 4000  
    COSTOPORKG = 300  

    def __init__(self, peso, marca):
        self.__peso = peso
        self.__marca = marca
      

    def calcularDespacho(self):
        costo_despacho = self.COSTODESPACHOBASE + (self.__peso * self.COSTOPORKG)
        return costo_despacho