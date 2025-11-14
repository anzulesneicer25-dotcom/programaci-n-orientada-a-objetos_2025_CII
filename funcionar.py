from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

def main():

    # Motores
    motor1 = Motor("gasolina", 120)
    motor2 = Motor("diesel", 140)
    motor3 = Motor("gasolina", 30)
    motor4 = Motor("gasolina", 40)

    # Automóviles
    auto1 = Automovil("Toyota", "Corolla", 2021, motor1, 4)
    auto2 = Automovil("Chevrolet", "Onix", 2022, motor2, 5)

    # Motocicletas
    moto1 = Motocicleta("Yamaha", "FZ", 2020, motor3, 150)
    moto2 = Motocicleta("Honda", "CBR", 2023, motor4, 300)

    print("=== AUTOMÓVILES ===")
    auto1.encender()
    auto1.abrir_maletero()
    auto1.tocar_claxon()
    auto1.apagar()
    print()

    auto2.encender()
    auto2.abrir_maletero()
    auto2.tocar_claxon()
    auto2.apagar()
    print()

    print("=== MOTOCICLETAS ===")
    moto1.encender()
    moto1.hacer_caballitos()
    moto1.usar_patada_arranque()
    moto1.apagar()
    print()

    moto2.encender()
    moto2.hacer_caballitos()
    moto2.usar_patada_arranque()
    moto2.apagar()
    print()

    print("=== OBJETOS COMPLETOS ===")
    print(auto1)
    print(auto2)
    print(moto1)
    print(moto2)

if __name__ == "__main__":
    main()










