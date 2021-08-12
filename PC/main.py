from tipo_computadora import TIPO
from caracteristicas import caracteristicas

if __name__ == "__main__":
    print("Mi PC")

    print()

    tipo = TIPO("Laptop")
    print(vars(tipo))

    print()

    caracter = caracteristicas("Intel core i3 370M", "4 GB", "intel(R) HD Graphics", "Windows 10", 64)

    print(vars(caracter))