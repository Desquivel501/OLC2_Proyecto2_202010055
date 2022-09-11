from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion


class Statement(Instruccion):

    def __init__(self, codigo, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, entorno):
        pass

    