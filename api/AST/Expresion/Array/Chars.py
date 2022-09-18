from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos



class Chars(Expresion):

    def __init__(self, expresion, linea:int, columna: int):
        self.expresion = expresion
        self.valores = []
        self.linea = linea
        self.columna = columna
    
    def obtener3D(self, ts) -> Retorno:
        pass
        
        