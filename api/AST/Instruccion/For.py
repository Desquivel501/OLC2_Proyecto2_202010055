from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Tipos import Tipo
from Entorno.Simbolo import Simbolo
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno


class For(Instruccion):

    def __init__(self, iterador, cuerpo: Statement, linea, columna, rango = None, lista = None):
        self.rango = rango
        self.lista = lista
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
        self.iterador = iterador


    def ejecutar3D(self, ts):
        pass
        
                    