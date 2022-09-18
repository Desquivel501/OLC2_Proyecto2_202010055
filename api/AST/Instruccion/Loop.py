from xmlrpc.client import Boolean
from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_


class Loop(Instruccion):

    def __init__(self, cuerpo: Statement, expresion: Boolean ,linea, columna):
        self.expresion = expresion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts):
        pass
            
        