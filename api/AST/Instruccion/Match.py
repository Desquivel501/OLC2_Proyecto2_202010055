
from operator import truediv
from Entorno.Retorno import Retorno
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from AST.Instruccion.Case import Case
from Entorno.Tipos import Tipos
from AST.misc.error import Error_


class Match(Instruccion):

    def __init__(self, condicion: Expresion, case_list, default, linea, columna):
        self.condicion = condicion
        self.case_list = case_list
        self.default = default
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts):
        pass
            
            
        