
from AST.Expresion.Expresion import Expresion
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Retorno, Tipos


class Else(Expresion, Instruccion):
    
    def __init__(self, instruccion, expresion ):
        self.instruccion = instruccion
        self.expresion = expresion
        
        
    def obtener3D(self, ts) -> Retorno:
       return self.expresion.obtener3D(ts)