from datetime import date
from persona import Persona
class Cliente(Persona):
    '''La clase Cliente que hereda de Persona'''

    def __init__(self, idCliente: int, fechaRegistro: date, vip: bool,
                 nombre: str,cedula:int,email:str, genero: str, edad: int,ocupacion:str):
        # Llamada al constructor de Persona
        Persona.__init__(self, nombre=nombre, email=email, genero=genero
                         , edad=edad, ocupacion=ocupacion, cedula=cedula)
        self._idCliente = idCliente
        self._fechaRegistro = fechaRegistro
        self._vip = vip

    # Propiedades
    @property
    def idCliente(self):
        return self._idCliente

    @idCliente.setter
    def idCliente(self, nuevo_id):
        self._idCliente = nuevo_id

    @property
    def fechaRegistro(self):
        return self._fechaRegistro

    @fechaRegistro.setter
    def fechaRegistro(self, nueva_fecha):
        self._fechaRegistro = nueva_fecha

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, es_vip):
        self._vip = es_vip

    def __str__(self):
        return f'Cliente: {self.__dict__}'


# ----------- Ejemplo de uso -----------
if __name__ == '__main__':
    objCliente1 = Cliente(idCliente=101,fechaRegistro=date.today(),vip=True,nombre='Ana López',cedula=11244577,
        genero='F',edad=30,email='ana@gmai.com',ocupacion='cliente')

    print(objCliente1)
    print('*'.center(20, '*'))
    print(f'idCliente: {objCliente1.idCliente}')
    print(f'Nombre: {objCliente1.nombre}')
    print(f'Fecha de registro: {objCliente1.fechaRegistro}')
    print(f'Cliente VIP: {objCliente1.vip}')

