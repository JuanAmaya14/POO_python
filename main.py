from Lector import lec
from libro import lib
from fechas import entrega
from fechas import devolver


if __name__ == "__main__":

    print("Info del lector")

    Lector = lec("Laisha Alexa", 8457689456)

    print(vars(Lector))

    print("")

    print("Info del libro")

    Libro = lib("Luna de pluton","Dross")

    print(vars(Libro))

    print("")


    print("fecha de entrega al lector")

    En = entrega("03/11/2021")

    print(vars(En))

    print("")


    print("fecha de entrega a devolver")

    De = devolver("10/11/2027")

    print(vars(De))