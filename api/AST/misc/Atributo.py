
from AST.Expresion.Expresion import Expresion
from Entorno.Tipos import Tipo

class Atributo():
    
    def __init__(self, identificador: str, valor: Expresion):
        self.identificador = identificador
        self.valor = valor
        self.tipo = None
