from enum import Enum
from Entorno.Tipos import Tipos

class Retorno:
    
    def __init__(self, tipo = Tipos.NULL):
        self.codigo = ""
        self.etiqueta = ""
        self.temporal = ""
        self.tipo = tipo