
class Lib:
    id = int
    genero = str
    autor = str

class lib(Lib):
    def __init__(self, genero, autor):
        self.genero = genero
        self.autor = autor
