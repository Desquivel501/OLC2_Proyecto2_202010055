
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from Entorno.Retorno import Retorno, Tipos

class Identificador(Expresion):
    
    def __init__(self, identificador: str, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        pass