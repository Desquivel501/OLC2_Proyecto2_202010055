

from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

class Llamada(Expresion, Instruccion):
    
    def __init__(self, identificador: str, listaExpresiones, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        self.listaExpresiones = listaExpresiones
        
    
    def ejecutar3D(self, ts: TablaSimbolos):
        self.getValor(ts)
    

    def obtener3D(self, ts) -> Retorno:
       pass