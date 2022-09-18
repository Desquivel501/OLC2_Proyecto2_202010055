
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos

class Capacidad(Expresion):
    
    def __init__(self, expresion):
        self.expresion = expresion
        
    def obtener3D(self, ts):
        pass
    

    
