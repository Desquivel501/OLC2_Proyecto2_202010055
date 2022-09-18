
from AST.misc.Program import Program
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos


class ExpCase(Expresion):

    def __init__(self, lista_exp, codigo: Expresion, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna
        self.lista_exp = lista_exp


    def obtener3D(self, ts) -> Retorno:
       pass