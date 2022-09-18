

from Entorno.Retorno import Retorno, Tipos
from Entorno.Simbolo import Simbolo

from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from AST.misc.error import Error_


class ToString(Expresion):
    def __init__(self, exp: Expresion, linea, columna):
        self.exp = exp;
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
       pass