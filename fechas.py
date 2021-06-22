class Entrega:
    Ent = str

class Devolver:
    Dev = str

class entrega (Entrega):
    def __init__(self, Ent):
        self.Ent = Ent

class devolver (Devolver):
    def __init__(self, Dev):
        self.Dev = Dev