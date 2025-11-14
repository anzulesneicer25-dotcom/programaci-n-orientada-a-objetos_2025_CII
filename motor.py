class Motor:
    def __init__(self, tipo: str, potencia: int):
        self._tipo = tipo
        self._potencia = potencia

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, n_tipo):
        self._tipo = n_tipo

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, n_potencia):
        self._potencia = n_potencia

    def encender_motor(self):
        print("El motor se ha encendido.")

    def apagar_motor(self):
        print("El motor se ha apagado.")

    def __str__(self):
        return f"Motor(tipo={self.tipo}, potencia={self.potencia})"












