

from api.Entorno.Retorno import Retorno
from Entorno.Simbolo import Simbolo
from AST.misc import driver
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Tipos import definirTipo, Tipos
from AST.misc.error import Error_


class ToString(Expresion):
    def __init__(self, exp: Expresion, linea, columna):
        self.exp = exp;
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
       pass