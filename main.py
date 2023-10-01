from transporte import Transporte
from tecnologia import Tecnologia
from scooter import Scooter
from bicicleta import Bicicleta
from consola import Consola
from Tv import Tv

class Main:
    def __init__(self):
        self.listaScooters = []
        self.listaBicicletas = []
        self.listaConsolas = []
        self.listaTvs = []

    def menu(self):
        while True:
            print("=======! -Menú- !=======")
            print("1. Registrar Scooter")
            print("2. Registrar Bicicleta")
            print("3. Registrar Consola")
            print("4. Registrar TV")
            print("5. Cotizar Scooters")
            print("6. Cotizar Bicicletas")
            print("7. Cotizar Consolas")
            print("8. Cotizar TV")
            print("9. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrarScooter()
            elif opcion == "2":
                self.registrarBicicleta()
            elif opcion == "3":
                self.registrarConsola()
            elif opcion == "4":
                self.registrarTv()
            elif opcion == "5":
                self.cotizarScooters()
            elif opcion == "6":
                self.cotizarBicicletas()
            elif opcion == "7":
                self.cotizarConsolas()
            elif opcion == "8":
                self.cotizarTvs()
            elif opcion == "9":
                print("Hasta la próxima.")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

     

    def registrarScooter(self):
        marca = input("Marca del Scooter: ")
        voltaje = int(input("Voltaje del Scooter: "))
        precio = float(input("Precio del Scooter: "))
        eficiencia = input("Eficiencia del Scooter (A/B/C/D/E/F): ")
        aro = float(input("Tamaño del aro del Scooter: "))
        velocidad = int(input("Velocidad del Scooter (km/h): "))
        peso = float(input("Peso del Scooter (kg): "))

        scooter = Scooter(marca, voltaje, precio, eficiencia, aro, velocidad, peso)
        self.listaScooters.append(scooter)
        print("Scooter registrado con éxito.")

    def registrarBicicleta(self):
        aro = float(input("Tamaño del aro de la Bicicleta: "))
        peso = float(input("Peso de la Bicicleta (kg): "))
        precio = float(input("Precio de la Bicicleta: "))
        marca = input("Marca de la Bicicleta: ")

        bicicleta = Bicicleta(aro, peso, precio, marca)
        self.listaBicicletas.append(bicicleta)
        print("Bicicleta registrada con éxito.")

    def registrarConsola(self):
        nombre = input("Nombre de la Consola: ")
        version = input("Versión de la Consola: ")
        marca = input("Marca de la Consola: ")
        voltaje = int(input("Voltaje de la Consola: "))
        precio = float(input("Precio de la Consola: "))
        eficiencia = input("Eficiencia de la Consola (A/B/C/D/E/F): ")

        consola = Consola(nombre, version, marca, voltaje, precio, eficiencia)
        self.listaConsolas.append(consola)
        print("Consola registrada con éxito.")

    def registrarTv(self):
        marca = input("Marca del TV: ")
        voltaje = int(input("Voltaje del TV: "))
        precio = float(input("Precio del TV: "))
        eficiencia = input("Eficiencia del TV (A/B/C/D/E/F): ")
        tamano = float(input("Tamaño del TV (en pulgadas): "))

        tv = Tv(marca, voltaje, precio, eficiencia, tamano)
        self.listaTvs.append(tv)
        print("TV registrado con éxito.")

    def cotizarScooters(self):
        print("Cotización de Scooters:")
        for scooter in self.listaScooters:
            descuento = scooter.calcularDescuento()
            costo_despacho = scooter.calcularDespacho()
            valor_total = scooter.getPrecio() * (1 - descuento) + costo_despacho
            print(f"Scooter de marca {scooter.getMarca()}:")
            print(f"- Descuento aplicado: {descuento * 100}%")
            print(f"- Costo de despacho: ${costo_despacho:.2f}")
            print(f"- Valor total: ${valor_total:.2f}")
            print()

    def cotizarBicicletas(self):
        print("Cotización de Bicicletas:")
        for bicicleta in self.listaBicicletas:
            costo_despacho = bicicleta.calcularDespacho()
            valor_total = bicicleta.getPrecio() + costo_despacho  
            print(f"Bicicleta de marca {bicicleta.getMarca()}:")
            print(f"- Costo de despacho: ${costo_despacho:.2f}")
            print(f"- Valor total: ${valor_total:.2f}")
            print()

    def cotizarConsolas(self):
        print("Cotización de Consolas:")
        for consola in self.listaConsolas:
            descuento = consola.calcularDescuento()
            valor_total = consola.getPrecio() * (1 - descuento)
            print(f"Consola de marca {consola.getMarca()}:")
            print(f"- Descuento aplicado: {descuento * 100}%")
            print(f"- Valor total: ${valor_total:.2f}")
            print()

    def cotizarTvs(self):
        print("Cotización de TVs:")
        for tv in self.listaTvs:
            descuento = tv.calcularDescuento()
            valor_total = tv.getPrecio() * (1 - descuento)
            print(f"TV de marca {tv.getMarca()}:")
            print(f"- Tamaño: {tv.getTamano()} pulgadas")
            print(f"- Descuento aplicado: {descuento * 100}%")
            print(f"- Valor total: ${valor_total:.2f}")
            print()

    
    
if __name__ == "__main__":
    programa = Main()
    programa.menu()