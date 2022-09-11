
from api.Entorno.Retorno import Retorno
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_


class If(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, else_ : Statement, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts):
        pass
            
            