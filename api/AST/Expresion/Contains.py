

from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno


class Contains(Expresion):
    def __init__(self, id, expresion, linea, columna):
        self.id = id
        self.expresion = expresion;
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
       pass
