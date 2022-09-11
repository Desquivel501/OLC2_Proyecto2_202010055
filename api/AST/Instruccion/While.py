from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_


class While(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, entorno):
        pass
        
