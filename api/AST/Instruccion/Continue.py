from Entorno.Retorno import Retorno
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion

class Continue(Instruccion):

    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts):
        pass
    