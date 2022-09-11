from Entorno.Simbolos.Struct import Struct
from AST.Expresion.Expresion import Expresion
from Entorno.Tipos import Tipo

class Rango():
    
    def __init__(self, inicio: Expresion, fin: Expresion):
        self.inicio = inicio
        self.fin = fin
        
