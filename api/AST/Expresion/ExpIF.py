

from AST.Expresion.Else import Else
from Entorno.Simbolo import Simbolo

from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos


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
