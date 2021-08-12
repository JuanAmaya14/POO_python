class Lector:
    id = int
    nombre = str
    documento = int

class lec(Lector):
    def __init__(self, nombre, documento):
        #super.__init__(nombre, documento)
        self.nombre = nombre
        self.documento = documento
