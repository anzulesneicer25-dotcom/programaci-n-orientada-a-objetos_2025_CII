
class Vehiculo:
    """
    Superclase Vehiculo:
    """
    def __init__(self, marca: str, modelo: str, anio: int, motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, n_marca):
        self._marca = n_marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, m_modelo):
        self._modelo = m_modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, a_anio):
        self._anio = a_anio

    @property
    def motor(self):
        return self._motor

    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} se está encendiendo...")
        self._motor.encender_motor()

    def apagar(self):
        print(f"El vehículo {self.marca} {self.modelo} se está apagando...")
        self._motor.apagar_motor()

    def __str__(self):
        return f"Vehiculo(marca={self.marca}, modelo={self.modelo}, año={self.anio}, motor={self.motor})"







