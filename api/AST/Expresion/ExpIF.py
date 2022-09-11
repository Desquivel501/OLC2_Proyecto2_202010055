

from AST.Expresion.Else import Else
from Entorno.Simbolo import Simbolo
from AST.misc import driver
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Tipos import definirTipo, Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno


class ExpIf(Expresion):
    def __init__(self, condicion: Expresion, instrucciones , cuerpo: Expresion, else_ : Expresion, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
        self.tipo = None
        
        
    def obtener3D(self, ts) -> Retorno:
       pass
