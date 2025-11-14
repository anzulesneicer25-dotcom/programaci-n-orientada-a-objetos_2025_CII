from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje: int):
        super().__init__(marca, modelo, anio, motor)
        self._cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, n_cilindraje):
        self._cilindraje = n_cilindraje

    def hacer_caballitos(self):
        print("La motocicleta está haciendo un caballito.")

    def usar_patada_arranque(self):
        print("Usando patada de arranque... ¡Motor listo!")

    def __str__(self):
        return f"Motocicleta(marca={self.marca}, modelo={self.modelo}, año={self.anio}, cc={self.cilindraje}, motor={self.motor})"



