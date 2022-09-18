
import copy
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos


class Clone(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = copy.deepcopy(expresion);
        self.linea = linea
        self.columna = columna
            
    def obtener3D(self, ts) -> Retorno:
       pass
        
