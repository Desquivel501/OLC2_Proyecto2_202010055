

from AST.Expresion.Else import Else
from Entorno.Simbolo import Simbolo

from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos



class ExpMatch(Expresion):
    def __init__(self, condicion: Expresion, case_list, default, linea, columna):
        self.condicion = condicion
        self.case_list = case_list
        self.default = default
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
       pass