from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from AST.misc.Program import Program


class Print_(Instruccion):

    def __init__(self, cadena: Expresion, list_exp, linea, columna):
        self.columna = columna
        self.linea = linea
        self.cadena = cadena
        self.list_exp = list_exp

    def ejecutar3D(self, ts):
        pass