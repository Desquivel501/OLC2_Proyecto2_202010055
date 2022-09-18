from enum import Enum
from re import T

class Tipos(Enum):
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    STR = 4
    STRING = 5
    CHAR = 6
    VOID = 7
    STRUCT = 8
    ARRAY_DATA = 9
    ARRAY = 10
    VECTOR_DATA = 11
    VECTOR = 12
    NULL = 13


class Retorno:
    
    def __init__(self, tipo = Tipos.NULL):
        self.codigo = ""
        self.etiqueta = ""
        self.temporal = ""
        self.tipo = tipo
        self.etiquetaV = ""
        self.etiquetaF = ""
        
    def iniciarRetorno(self, codigo, etiqueta, temporal, tipo):
        self.codigo = codigo
        self.temporal = temporal
        self.etiqueta = etiqueta
        self.tipo = tipo