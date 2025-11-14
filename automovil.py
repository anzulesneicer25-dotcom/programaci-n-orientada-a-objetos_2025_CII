from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, numero_puertas: int):
        super().__init__(marca, modelo, anio, motor)
        self._numero_puertas = numero_puertas

    @property
    def numero_puertas(self):
        return self._numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, n_numero):
        self._numero_puertas = n_numero

    def abrir_maletero(self):
        print("El maletero ha sido abierto.")

    def tocar_claxon(self):
        print("¡Piiiiip! El automóvil toca el claxon.")

    def __str__(self):
        return f"Automovil(marca={self.marca}, modelo={self.modelo}, año={self.anio}, puertas={self.numero_puertas}, motor={self.motor})"


