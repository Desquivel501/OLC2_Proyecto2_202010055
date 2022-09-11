
from Entorno.Simbolo import Simbolo
from AST.misc import driver
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Tipos import definirTipo, Tipos, Tipo
from AST.misc.error import Error_
from Entorno.Retorno import Retorno


class Casteo(Expresion):
    def __init__(self, nuevo_tipo: Tipo,  exp: Expresion, linea, columna):
        self.exp = exp;
        self.linea = linea
        self.columna = columna
        self.nuevo_tipo = nuevo_tipo
        
        
    def obtener3D(self, ts) -> Retorno:
       pass