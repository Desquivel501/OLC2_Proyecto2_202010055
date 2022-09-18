from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos

class Break(Instruccion):

    def __init__(self, expresion: Expresion, linea, columna):
        self.linea = linea
        self.columna = columna
        self.expresion = expresion


    def ejecutar3D(self, ts) -> Retorno:
        pass
    
    