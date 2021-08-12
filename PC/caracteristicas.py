class Cara:
      procesador = str
      RAM = str
      Targeta_Video = str
      Sis_OP = str
      bits = int

class caracteristicas(Cara):
    def __init__(self, procesador, RAM, Targeta_Video, Sis_OP, bits):
        self.procesador = procesador
        self.RAM = RAM
        self.Targeta_Video = Targeta_Video
        self.Sis_OP = Sis_OP
        self.bits = bits